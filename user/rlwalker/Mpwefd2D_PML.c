/* Short description line
Comments here blablabla lorem ipsum dolores sit amet...

You can use several paragraphs for comments, no problem.*/

/* Copyright notice */
#include <rsf.h>
#ifdef _OPENMP
#include <omp.h>
#include "omputil.h"
#endif
#include "fdutil.h"
#include <stdlib.h>
#include <math.h>

#define PI 3.14159265358979323846

/* ========================================================================== */
/* FD Coefficients                                                            */
/* ========================================================================== */
#define NOP 4 /* derivative operator half-size */
#define mPML 100 /* max value of the PML*/

/* Coefficients are:  (-1)^(k+1)/k * (n!)^2 / (n+k)!(n-k)!
for n = order of approximation i.e. eighth order
and k = coefficient number */

/* CENTERED derivatives */
#define C1 +0.800000   /* +4/5    */
#define C2 -0.200000   /* -1/5    */
#define C3 +0.038095   /* +4/105  */
#define C4 -0.003571   /* -5/280  */
#define Dx(a,ix,iz,s) (C4*(a[ix+4][iz] - a[ix-4][iz]) +		\
C3*(a[ix+3][iz] - a[ix-3][iz]) +		\
C2*(a[ix+2][iz] - a[ix-2][iz]) +		\
C1*(a[ix+1][iz] - a[ix-1][iz])  )*s
#define Dz(a,ix,iz,s) (C4*(a[ix][iz+4] - a[ix][iz-4]) +		\
C3*(a[ix][iz+3] - a[ix][iz-3]) +		\
C2*(a[ix][iz+2] - a[ix][iz-2]) +		\
C1*(a[ix][iz+1] - a[ix][iz-1])  )*s


enum AniType {ORTHORHOMBIC=0,TRICLINIC=1};
enum SourceType {STRESS=2, DISPLACEMENT=1, ACCELERATION=0, TENSOR=3};
/* ========================================================================== */
/* Aid Functions                                                              */
/* ========================================================================== */
void zero2d(int n1, int n2, float **array)
{
	int i1, i2;
	for (i2 = 0; i2 < n2; i2++){
		for (i1 = 0; i1 < n1; i1++){
			array[i2][i1] = 0.0;
		}
	}
	return;
}


/* ========================================================================== */
/* Main Loop                                                                  */
/* ========================================================================== */

int main(int argc, char* argv[])
{
	/* Opening Message */
	fprintf(stderr,"*********************************************************\n");
	fprintf(stderr,"******************* Commencing pwefd2D_PML***************\n");
	fprintf(stderr,"*********************************************************\n");
	/* Declare RSF params */
	bool verb,fsrf,snap,dabc,debug,abcone,cfl,opot,abcpml;
	bool USE_PML_LEFT, USE_PML_RIGHT, USE_PML_TOP, USE_PML_BOTTOM;
	int  jsnap,ntsnap,jdata,nbell;
	enum AniType type;
	enum SourceType srctype;
	float fmax,safety;

	/* I/O files */
	sf_file Fwav=NULL; /* wavelet   */
	sf_file Fsou=NULL; /* sources   */
	sf_file Frec=NULL; /* receivers */
	sf_file Ffro=NULL; /* fluid density   */
	sf_file Fsro=NULL; /* solid grain density   */
	sf_file Fdat=NULL; /* data      */
	sf_file Fwfl=NULL; /* wavefield */
	sf_file Fphi=NULL; /* porosity  */
	sf_file Fkdr=NULL; /* Drained Bulk Modulus */
	sf_file Fkfl=NULL; /* Fluid Bulk Modulus */
	sf_file Fksg=NULL; /* solid grain modulus */
	sf_file Fprm=NULL; /* permeability (tensor, or should be) */
	sf_file Ffvs=NULL; /* fluid viscosity */
	sf_file Fshm=NULL; /* shear modulus */
	sf_file Ftor=NULL; /* tortuosity */

	int     nt,nz,nx,ns,nr,nc,nb;
	int     it,iz,ix;
	float   dt,dz,dx,idz,idx;
	/* Debug values below */
	float t, vnormtotal = 0.0f, vnormmax=0.0f, pnormtotal = 0.0f, pnormmax=0.0f;
	float stability_threshold = 1.0e25f;
	int vnormmax_ix = 0, vnormmax_iz = 0, pnormmax_ix = 0, pnormmax_iz = 0;
	int mpx = 97, mpz = 255;
	/* End debug values */

	sf_axis at,ax,az;
	sf_axis as,ar,ac;

	/* init RSF */
	sf_init(argc,argv);

	/* ------------------------------------------------------------------------ */
	/* OpenMP parameters*/

	int ompchunk;
	#ifdef _OPENMP
	int ompnth,ompath;
	#endif

	if (! sf_getint("ompchunk",&ompchunk)) ompchunk=1;
	/* OpenMP data chunk size */
	#ifdef _OPENMP
	if (! sf_getint("ompnth",  &ompnth))     ompnth=0;
	/* OpenMP available threads */
	#pragma omp parallel
	ompath=omp_get_num_threads();
	if (ompnth<1) ompnth=ompath;
	omp_set_num_threads(ompnth);
	sf_warning("using %d threads of a total of %d",ompnth,ompath);
	#endif

	/* ------------------------------------------------------------------------ */
	/* Source parameters */
	int tsrc;
	if (! sf_getint("srctype",&tsrc)) tsrc=0; /* source type, see comments */

	srctype = tsrc;

	/* MAKE SURE USER HAS DECLARED ANISOTROPY TYPE*/
	int ttype;
	if (! sf_getint("ani", &ttype)) ttype=-1;/* Anisotropy type, see comments */
	if (ttype == -1 || ttype >2 || ttype < 0) sf_error("Invalid Anisotropy type");
	type = ttype;

	/* I/O arrays */
	float***ww=NULL;           /* wavelet   */
	float **dd=NULL;           /* data      */
	/* ====================================================================== */
	/* --------------2d code---------------- */
	/* IO Arrays */
	pt2d   *ss=NULL;           /* sources   */
	pt2d   *rr=NULL;           /* receivers */
	/* FDM structure */
	fdm2d    fdm=NULL;
	/*------------------------------------------------------------*/
	/* linear interpolation weights/indices */
	lint2d cs,cr;
	/* wavefield cut params */
	float     **uc=NULL;

	/*-------------- material parameters -------------------------------------*/
	float **tt=NULL;            /* work array */
	float **fro=NULL;           /* fluid density   */
	float **sro=NULL;           /* solid grain density */
	float **bro=NULL;           /* bulk density   */
	float **mro=NULL;           /* momentum added density */
	float **kdr=NULL;           /* drained bulk modulus */
	float **kud=NULL;           /* undrained bulk modulus */
	float **kfl=NULL;           /* fluid modulus */
	float **ksg=NULL;           /* solid grain modulus */
	/*float **fud=NULL; */          /* undrained bulk modulus */
	float **fvs=NULL;           /* fluid viscosity */
	float **alpha=NULL;         /* biot coefficient */
	float **biotmod=NULL;       /* biod modulus */
	float **skem=NULL;          /* skempton coefficient */
	float **lambdau=NULL;       /* undrained lame #1 */
	float **lambda=NULL;        /* solid matrix lame #1 */
	float **shm=NULL;           /* shear modulus */
	float **fmo=NULL;           /* fluid mobility */
	float **phi=NULL;           /* porosity */
	float **tor=NULL;           /* tortuosity */
	float **prm=NULL;           /* permeability (tensor?) */
	float **r_bar=NULL;
	float **qp=NULL,**qs=NULL;

	/*------------------------------------------------------------*/
	/* particle displacement: um = U @ t-1; uo = U @ t; up = U @ t+1 */
	float **umz,**uoz,**upz,**uaz,**utz;
	float **umx,**uox,**upx,**uax,**utx;
	/* particle velocity: vm = V @ t-1; vo = V @ t; vp = V @ t+1 */
	float **vmz,**voz,**vpz,**vaz,**vtz;
	float **vmx,**vox,**vpx,**vax,**vtx;
	/* filtration displacement: wm = W @ t-1; wo = W @ t; wp = W @ t+1 */
	float **wmz,**woz,**wpz,**waz,**wtz;
	float **wmx,**wox,**wpx,**wax,**wtx;
	/* filtration velocity: qm = Q @ t-1; uo = Q @ t; up = Q @ t+1 */
	float **qmz,**qoz,**qpz,**qaz,**qtz;
	float **qmx,**qox,**qpx,**qax,**qtx;
	/* */
	/* stress/strain tensor */
	float **tzz, **txz, **tzx, **txx;
	/* pore pressure */
	float **p;

	/*----------------------PML Parameters-------------------------*/
	/* 2D */
	float **gamma11, **gamma22, **gamma12_1, **xi_1, **xi_2;
	float **memory_dx_vx1, **memory_dx_vx2, **memory_dz_vx;
	float **memory_dx_vz, **memory_dz_vz1, **memory_dz_vz2;
	float **memory_dx_sigmaxx, **memory_dx_sigmazz, **memory_dx_sigmaxz;
	float **memory_dx_sigma2vx, **memory_dx_sigma2vxf, **memory_dz_sigma2vz;
	float **memory_dz_sigma2vzf, **memory_dz_sigmaxx, **memory_dz_sigmazz;
	float **memory_dz_sigmaxz;

	float **R, **ga, **S, **rho_11, **rho_12, **rho_22, **c1, **b1, **a1, **delta;
	float **Vp, **Vps, **Vs;
	float **CFL_LHS, **CFL_RHS;

	/* 1D */
	float *d_x, *K_x, *alpha_x, *a_x, *b_x, *d_x_half_x, *K_x_half_x;
	float *alpha_x_half_x, *a_x_half_x, *b_x_half_x;
	float *d_z, *K_z, *alpha_z, *a_z, *b_z, *d_z_half_z, *K_z_half_z;
	float *alpha_z_half_z, *a_z_half_z, *b_z_half_z;
	/* 0D */
	float thickness_PML_x, thickness_PML_z, xoriginleft, xoriginright;
	float zoriginbottom, zorigintop;
	float Rcoef, d0_x, d0_z, xval, zval, abscissa_in_PML, abscissa_normalized;
	float c33_half_z;
	float co,c1a, c2, K_MAX_PML, NPOWER, ALPHA_MAX_PML, Vp_max, Vs_max;
	float value_dx_sigmaxx, value_dz_sigmaxx, value_dx_sigma2vxf, value_dz_sigma2vzf;
	float value_dx_sigmaxz, value_dz_sigmaxz, value_dx_vx1, value_dx_vx2, value_dz_vx;
	float value_dx_vz, value_dz_vz1, value_dz_vz2;
	int NPOINTS_PML;

	/* ======================================================================== */
	/* End variable declarations */
	/* ======================================================================== */
	/*------------------------------------------------------------*/
	/* Temp values for solid strain */
	/*  float    szz,   sxx,   syy,   sxy,   syz,   szx;*/
	/* Temp values for relative strain */
	/*  float    ezz,   exx,   eyy,   exy,   eyz,   ezx;*/
	/*------------------------------------------------------------*/
	/* ======================================================================== */
	/* execution flags - parse command line */
	if (! sf_getbool("verb",&verb))     verb=true; /* verbosity flag */
	if (! sf_getbool("snap",&snap))     snap=false; /* wavefield snapshots flag */
	if (! sf_getbool("free",&fsrf))     fsrf=false; /* free surface flag */
	if (! sf_getbool("dabc",&dabc))     dabc=true; /* use sponge absorbing BC */
	if (! sf_getbool("abcone",&abcone)) abcone=false; /* use sharp brake at end of boundary layer */
	if (! sf_getbool("debug",&debug))   debug=true; /* print debugging info */
	if (! sf_getbool("cfl",&cfl))       cfl=true; /* use CFL check, will cause program to fail if not satisfied */
	if (! sf_getbool("opot",&opot))     opot=false; /* output potentials */
	if (! sf_getbool("abcpml",&abcpml))    abcpml=false; /* "PML ABC" */
	if (! sf_getbool("USE_PML_TOP",&USE_PML_TOP))    USE_PML_TOP=false; /* "PML ABC" */
	if (! sf_getbool("USE_PML_BOTTOM",&USE_PML_BOTTOM))    USE_PML_BOTTOM=false; /* "PML ABC" */
	if (! sf_getbool("USE_PML_LEFT",&USE_PML_LEFT))    USE_PML_LEFT=false; /* "PML ABC" */
	if (! sf_getbool("USE_PML_RIGHT",&USE_PML_RIGHT))    USE_PML_RIGHT=false; /* "PML ABC" */
	if (snap) {  /* save wavefield every *jsnap* time steps */
		if (! sf_getint("jsnap",&jsnap)) jsnap=nt;
	}
	/*---------------Read in PML Parameters-----------------------*/
	if (! sf_getint("NPOINTS_PML",&NPOINTS_PML)) NPOINTS_PML=10;
	if (! sf_getfloat("Rcoef",&Rcoef)) Rcoef=0.001f;/* Reflection coefficient */
	if (! sf_getfloat("NPOWER",&NPOWER)) NPOWER=2.0f;/* power to compute d0 profile */
	if (! sf_getfloat("K_MAX_PML",&K_MAX_PML)) K_MAX_PML=1.0f;/* ! from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-11 */

	/*------------------------------------------------------------*/
	/* I/O files */
	Fwav = sf_input ("in" ); /* wavelet   */
	Fsro = sf_input ("sro"); /* solid grain density   */
	Ffro = sf_input ("fro"); /* fluid density   */
	Fphi = sf_input ("phi"); /* porosity  */
	Fkdr = sf_input ("kdr"); /* drained bulk modulus */
	Fkfl = sf_input ("kfl"); /* fluid modulus */
	Fksg = sf_input ("ksg"); /* solid grain modulus */
	Fprm = sf_input ("prm"); /* permeability (tensor?) */
	Ffvs = sf_input ("fvs"); /* fluid viscosity */
	Fshm = sf_input ("shm"); /* shear modulus */
	Ftor = sf_input ("tor"); /* tortuosity */
	Fsou = sf_input ("sou"); /* sources   */
	Frec = sf_input ("rec"); /* receivers */
	Fwfl = sf_output("wfl"); /* wavefield */
	Fdat = sf_output("out"); /* data      */

	/* print debugging information */

	/*-------------------------------------------------------------*/
	/* Wavefield cut parameters */
	sf_axis   acz=NULL,acx=NULL;
	int       nqz,nqx;
	float     oqz,oqx;
	float     dqz,dqx;

	/* ------------------------------------------------------------------------ */
	/* axes */
	at = sf_iaxa(Fwav,3); sf_setlabel(at,"time");
	sf_setunit(at,"s");
	if (verb) {
		printf("time axis\n"); sf_raxa(at); /* time */
	}

	az = sf_iaxa(Fshm,1); sf_setlabel(az,"space z");
	sf_setunit(az,"m");if (verb) sf_raxa(az); /* depth */

	ax = sf_iaxa(Fshm,2); sf_setlabel(ax,"space x");
	sf_setunit(ax,"m");if (verb) sf_raxa(ax); /* space x */

	as = sf_iaxa(Fsou,2); sf_setlabel(as,"sources");
	sf_setunit(as,"m");if (verb) sf_raxa(as); /* sources */

	ar = sf_iaxa(Frec,2); sf_setlabel(ar,"receivers");
	sf_setunit(ar,"m");if (verb) sf_raxa(ar); /* receivers */

	/* number and increments */
	nt = sf_n(at); dt = sf_d(at);
	nz = sf_n(az); dz = sf_d(az);
	nx = sf_n(ax); dx = sf_d(ax);

	/* number of sources and receivers */
	ns = sf_n(as);
	nr = sf_n(ar);

	/* if wavefield snapshots are requested */
	if (snap){
		printf("wavefield snapshots requested\n");
		if (!sf_getint  ("nqz",&nqz)) nqz=sf_n(az);
		if (!sf_getint  ("nqx",&nqx)) nqx=sf_n(ax);

		if (!sf_getfloat("oqz",&oqz)) oqz=sf_o(az);
		if (!sf_getfloat("oqx",&oqx)) oqx=sf_o(ax);
	}

	/*------------------------------------------------------------*/
	/* other execution parameters */
	if (! sf_getint("nbell",&nbell)) nbell=1;  /* bell size */
	if (verb) sf_warning("nbell=%d",nbell);
	if (! sf_getint("jdata",&jdata)) jdata=1;

	/* Absorbing Boundary */
	if ( !sf_getint("nb",&nb)) nb=100; /* padding size for absorbing boundary */
	if (nb < NOP) nb = NOP;


	/*--------------------------------------------------------------------------*/
	/* expand domain for FD operators and ABC */
	if (verb) sf_warning("initialing finite difference parameters\n");
	fdm = fdutil_init(verb,fsrf,az,ax,nb,ompchunk);
	fdbell_init(nbell);

	if (verb) sf_warning("expanding domain to include boundaries\n");

	sf_setn(az,fdm->nzpad); sf_seto(az,fdm->ozpad);
	if (verb) {
		sf_warning("information on axis z\n"); sf_raxa(az);
	}
	sf_setn(ax,fdm->nxpad); sf_seto(ax,fdm->oxpad);
	if (verb) {
		sf_warning("information on axis x\n"); sf_raxa(ax);
	}
	float *sigma=NULL;
	sigma=sf_floatalloc(fdm->nb);

	/*--------------------------------------------------------------------------*/
	/* 2D vector components */
	nc = 2;
	ac = sf_maxa(nc,0,1);

	/*-------------------Data Output Setup--------------------------------------*/

	/* setup output data header */
	sf_oaxa(Fdat,ar,1);
	sf_oaxa(Fdat,ac,2);
	sf_setn(at,nt/jdata);
	sf_setd(at,dt*jdata);
	sf_oaxa(Fdat,at,3);
	/* setup output wavefield header */
	if (snap) {
		dqz=sf_d(az);
		dqx=sf_d(ax);

		acx = sf_maxa(nqx,oqx,dqx); sf_raxa(acx);
		acz = sf_maxa(nqz,oqz,dqz); sf_raxa(acz);
		/* TODO: check if the imaging window fits in the wavefield domain */

		uc=sf_floatalloc2(sf_n(acz),sf_n(acx));

		ntsnap=0;
		for (it=0; it<nt; it++) {
			if (it%jsnap==0) ntsnap++;
		}
		sf_setn(at,  ntsnap);
		sf_setd(at,dt*jsnap);
		if (verb) sf_raxa(at);

		sf_oaxa(Fwfl,acz,1);
		sf_oaxa(Fwfl,acx,2);
		sf_oaxa(Fwfl,ac, 3);
		sf_oaxa(Fwfl,at, 4);
	}

	/*------------------------------------------------------------*/
	/* source array */
	/* Source wavelet is generated externally and input into sim */
	if (srctype == TENSOR) {
		ww=sf_floatalloc3(ns,3,nt);
		sf_floatread(ww[0][0],nt*3*ns,Fwav);
	} else {
		ww=sf_floatalloc3(ns,nc,nt);
		sf_floatread(ww[0][0],nt*nc*ns,Fwav);
	}

	/* data array */
	dd = sf_floatalloc2(nr,nc);
	/*------------------------------------------------------------*/
	/* setup source/receiver coordinates */
	ss = (pt2d*) sf_alloc(ns,sizeof(*ss));
	rr = (pt2d*) sf_alloc(nr,sizeof(*rr));

	/* read in source/receiver data */
	pt2dread1(Fsou,ss,ns,2); /* read (x,z) coordinates */
	pt2dread1(Frec,rr,nr,2); /* read (x,z) coordinates */

	cs = lint2d_make(ns,ss,fdm); /* setup linear interpolation */
	cr = lint2d_make(nr,rr,fdm);

	/*------------------------------------------------------------*/
	/* setup FD coefficients */

	idz = 1.0/dz;
	idx = 1.0/dx;

	/* ====================================================================== */
	/* Begin variable memory allocation */
	/* ====================================================================== */


	/* ---------------allocate space for material parameters ---------------- */
	tt = sf_floatalloc2(nz,nx);

	fro =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input fluid density */
	sro =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input solid grain density */
	kdr =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input drained bulk modulus */
	kfl =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input fluid bulk modulus */
	ksg =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input solid grain bulk modulus */
	fvs =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input fluid viscosity */
	shm =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input shear modulus */
	tor =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input tortuosity */
	prm =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input permeability (tensor?) */
	phi =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* input porosity */

	/* --------------read in material parameters ---------------------------- */
	sf_floatread(tt[0],nz*nx,Ffro);     expand(tt,fro ,fdm);
	sf_floatread(tt[0],nz*nx,Fsro);     expand(tt,sro ,fdm);
	sf_floatread(tt[0],nz*nx,Fkdr);     expand(tt,kdr ,fdm);
	sf_floatread(tt[0],nz*nx,Fkfl);     expand(tt,kfl ,fdm);
	sf_floatread(tt[0],nz*nx,Fksg);     expand(tt,ksg ,fdm);
	sf_floatread(tt[0],nz*nx,Ffvs);     expand(tt,fvs ,fdm);
	sf_floatread(tt[0],nz*nx,Fshm);     expand(tt,shm ,fdm);
	sf_floatread(tt[0],nz*nx,Ftor);     expand(tt,tor ,fdm);
	sf_floatread(tt[0],nz*nx,Fprm);     expand(tt,prm ,fdm);
	sf_floatread(tt[0],nz*nx,Fphi);     expand(tt,phi ,fdm);

	/* ---------------allocate space for derived parameters------------------ */
	kud     =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* undrained bulk modulus */
	alpha   =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* biot coefficient */
	biotmod =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* biot modulus */
	bro     =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* bulk density */
	lambdau =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* undrained lame #1 */
	lambda  =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* solid matrix lame #1 */
	skem    =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* skempton coefficient */
	mro     =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	r_bar   =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	fmo     =sf_floatalloc2(fdm->nzpad,fdm->nxpad); /* fluid mobility */

	/* -----------------Memory variables - 2D---------------------------------- */
	gamma11 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	gamma22 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	xi_1    =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	xi_2    =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_vx1 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_vx2 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_vx =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_vz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_vz1 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_vz2 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_sigmaxx =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_sigmazz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_sigmaxz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_sigma2vx =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dx_sigma2vxf =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_sigma2vz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_sigma2vzf =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_sigmaxx =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_sigmazz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	memory_dz_sigmaxz =sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	/* ----------------damping profiles - 1D-------------------------------------*/
	d_x =sf_floatalloc(fdm->nxpad);
	K_x =sf_floatalloc(fdm->nxpad);
	alpha_x =sf_floatalloc(fdm->nxpad);
	a_x =sf_floatalloc(fdm->nxpad);
	b_x =sf_floatalloc(fdm->nxpad);
	d_x_half_x =sf_floatalloc(fdm->nxpad);
	K_x_half_x =sf_floatalloc(fdm->nxpad);
	alpha_x_half_x =sf_floatalloc(fdm->nxpad);
	a_x_half_x =sf_floatalloc(fdm->nxpad);
	b_x_half_x =sf_floatalloc(fdm->nxpad);

	d_z =sf_floatalloc(fdm->nzpad);
	K_z =sf_floatalloc(fdm->nzpad);
	alpha_z =sf_floatalloc(fdm->nzpad);
	a_z =sf_floatalloc(fdm->nzpad);
	b_z =sf_floatalloc(fdm->nzpad);
	d_z_half_z =sf_floatalloc(fdm->nzpad);
	K_z_half_z =sf_floatalloc(fdm->nzpad);
	alpha_z_half_z =sf_floatalloc(fdm->nzpad);
	a_z_half_z =sf_floatalloc(fdm->nzpad);
	b_z_half_z =sf_floatalloc(fdm->nzpad);

	/* -----------------PML Parameters---------------------------------------- */
	/* 2D */
	R =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	ga =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	S =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	rho_11 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	rho_12 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	rho_22 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	c1 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	b1 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	a1 =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	delta =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	Vp =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	Vps =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	Vs =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	CFL_LHS =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	CFL_RHS =sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	/*------------------------------------------------------------*/
	/* allocate wavefield arrays */
	/* -----------------------------------------------------------*/
	/* particle displacement */
	umz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	uoz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	upz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	uaz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	umx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	uox=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	upx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	uax=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("particle displacement fields set\n");

	/* particle velocity */
	vmx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	vox=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	vpx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	vax=sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	vmz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	voz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	vpz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	vaz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("particle velocity fields set\n");

	/* filtration displacement */
	wmz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	woz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	wpz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	waz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	wmx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	wox=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	wpx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	wax=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("filtration displacement fields set\n");

	/* filtration velocity */
	qmx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qox=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qpx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qax=sf_floatalloc2(fdm->nzpad,fdm->nxpad);

	qmz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qoz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qpz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	qaz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("filtration displacement fields set\n");

	/* stress tensor */
	tzz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	tzx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	txz=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	txx=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("stress tensor fields set\n");

	/* pore pressure */
	p  =sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	if (verb) sf_warning("pore pressure field set\n");

	/* ------------------------------------------------------------------------ */
	/* Zero out values */
	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			umz[ix][iz] = 0.0f;
			uoz[ix][iz] = 0.0f;
			upz[ix][iz] = 0.0f;
			uaz[ix][iz] = 0.0f;

			umx[ix][iz] = 0.0f;
			uox[ix][iz] = 0.0f;
			upx[ix][iz] = 0.0f;
			uax[ix][iz] = 0.0f;
		}
	}
	if (verb) sf_warning("particle displacement fields zeroed\n");
	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			wmz[ix][iz] = 0.0f;
			woz[ix][iz] = 0.0f;
			wpz[ix][iz] = 0.0f;
			waz[ix][iz] = 0.0f;

			wmx[ix][iz] = 0.0f;
			wox[ix][iz] = 0.0f;
			wpx[ix][iz] = 0.0f;
			wax[ix][iz] = 0.0f;
		}
	}
	if (verb) sf_warning("filtration displacement fields zeroed\n");

	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			vmz[ix][iz] = 0.0f;
			voz[ix][iz] = 0.0f;
			vpz[ix][iz] = 0.0f;
			vaz[ix][iz] = 0.0f;

			vox[ix][iz] = 0.0f;
			vmx[ix][iz] = 0.0f;
			vpx[ix][iz] = 0.0f;
			vax[ix][iz] = 0.0f;
		}
	}
	if (verb) sf_warning("particle velocity fields zeroed\n");

	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			qmz[ix][iz] = 0.0f;
			qoz[ix][iz] = 0.0f;
			qpz[ix][iz] = 0.0f;
			qaz[ix][iz] = 0.0f;

			qmx[ix][iz] = 0.0f;
			qox[ix][iz] = 0.0f;
			qpx[ix][iz] = 0.0f;
			qax[ix][iz] = 0.0f;
		}
	}
	if (verb) sf_warning("flitration velocity fields zeroed\n");

	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			txx[ix][iz] = 0.0f;
			txz[ix][iz] = 0.0f;
			tzx[ix][iz] = 0.0f;
			tzz[ix][iz] = 0.0f;

			p[ix][iz] = 0.0f;
		}
	}
	if (verb) sf_warning("stress fields zeroed\n");
	if (verb) sf_warning("pore pressure field zeroed\n");

	if (opot) {
		qp=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
		qs=sf_floatalloc2(fdm->nzpad,fdm->nxpad);
	}

	if (verb) sf_warning("all wavefield structures allocated and zeroed\n");
  /* ----------------------zero memory variables------------------------------*/
	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			memory_dx_vx1[ix][iz] = 0.0f;
      memory_dx_vx2[ix][iz] = 0.0f;
      memory_dz_vx[ix][iz] = 0.0f;
      memory_dx_vz[ix][iz] = 0.0f;
      memory_dz_vz1[ix][iz] = 0.0f;
      memory_dz_vz2[ix][iz] = 0.0f;
      memory_dx_sigmaxx[ix][iz] = 0.0f;
      memory_dx_sigmazz[ix][iz] = 0.0f;
      memory_dx_sigmaxz[ix][iz] = 0.0f;
      memory_dx_sigma2vx[ix][iz] = 0.0f;
      memory_dx_sigma2vxf[ix][iz] = 0.0f;
      memory_dz_sigmaxx[ix][iz] = 0.0f;
      memory_dz_sigmazz[ix][iz] = 0.0f;
      memory_dz_sigmaxz[ix][iz] = 0.0f;
      memory_dz_sigma2vz[ix][iz] = 0.0f;
      memory_dz_sigma2vzf[ix][iz] = 0.0f;
		}
	}
if (verb) sf_warning("memory variables zeroed\n");

	/* free work vector */
	free(*tt); free(tt);
	if (verb) sf_warning("all parameter variables allocated\n");

	/*------------------------------------------------------------*/
	/* calculate local parameters */
	/* for    (ix = NOP; ix < fdm->nxpad - NOP; ix++) { */
	/*   for    (iz = NOP; iz < fdm->nzpad - NOP; iz++) { */
	for (ix = 0; ix < fdm->nxpad; ix++) {
		for (iz = 0; iz < fdm->nzpad; iz++) {
			/* bulk density */
			bro[ix][iz] = phi[ix][iz]*fro[ix][iz] + (1.0 - phi[ix][iz])*sro[ix][iz];
			/* biot coefficient */
			alpha[ix][iz] = 1.0 - kdr[ix][iz]/ksg[ix][iz];
			/* skempton coefficient */
			skem[ix][iz] = (1.0/kdr[ix][iz] - 1.0/ksg[ix][iz])/(1.0/kdr[ix][iz] - 1.0/ksg[ix][iz] + phi[ix][iz]*(1.0/kfl[ix][iz] - 1.0/ksg[ix][iz]));
			/* undrained bulk modulus */
			kud[ix][iz] = kdr[ix][iz] / (1.0 - skem[ix][iz]*(1.0 - kdr[ix][iz]/ksg[ix][iz]));
			/* biot modulus */
			biotmod[ix][iz] = skem[ix][iz] * kud[ix][iz]/alpha[ix][iz];
			/* undrained lame # 1 */
			lambdau[ix][iz] = kud[ix][iz] - 2.0*shm[ix][iz]/3.0;
			/* solid matrix lame # 1 */
			lambda[ix][iz] = kdr[ix][iz] - 2.0*shm[ix][iz]/3.0;
			/* Poroelastodynamic Values */
			mro[ix][iz] = tor[ix][iz]*fro[ix][iz] / phi[ix][iz];
			r_bar[ix][iz] = mro[ix][iz]*bro[ix][iz] - fro[ix][iz]*fro[ix][iz];
			/* fluid mobility / coefficient of friction */
			fmo[ix][iz] = fvs[ix][iz]/prm[ix][iz];
		}
	}
	if (verb) sf_warning("local parameters generated\n");

	/* ------------------------------------------------------------------------ */
	/* Velocities */
	/* ------------------------------------------------------------------------ */
	for (ix = 0; ix < fdm->nxpad; ix++) {
		for (iz = 0; iz < fdm->nzpad; iz++) {
			R[ix][iz] = biotmod[ix][iz]*powf(phi[ix][iz],2.0);
			rho_11[ix][iz] = bro[ix][iz]*phi[ix][iz]*fro[ix][iz]*(tor[ix][iz]);
			rho_12[ix][iz] = phi[ix][iz]*fro[ix][iz]*(1.0-tor[ix][iz]);
			rho_22[ix][iz] = tor[ix][iz]*phi[ix][iz]*fro[ix][iz];
			S[ix][iz] = lambdau[ix][iz] + 2.0*shm[ix][iz];
			ga[ix][iz] = biotmod[ix][iz]*phi[ix][iz]*(alpha[ix][iz] - phi[ix][iz]);
			c1[ix][iz] = S[ix][iz]*R[ix][iz] - ga[ix][iz];
			b1[ix][iz] = -1.0*S[ix][iz]*rho_22[ix][iz] - R[ix][iz]*rho_11[ix][iz] + 2.0*ga[ix][iz]*rho_12[ix][iz];
			a1[ix][iz] = rho_11[ix][iz]*rho_22[ix][iz] - powf(rho_12[ix][iz],2.0);
			delta[ix][iz] = powf(b1[ix][iz],2.0) - 4.0*a1[ix][iz]*c1[ix][iz];
			Vp[ix][iz] = sqrtf( (-1.0*b1[ix][iz] + sqrtf(delta[ix][iz])) / (2.0*a1[ix][iz] ) );
			Vps[ix][iz] = sqrtf( (-1.0*b1[ix][iz] - sqrtf(delta[ix][iz])) / (2.0*a1[ix][iz] ) );
			Vs[ix][iz] = sqrtf( shm[ix][iz] / ( rho_11[ix][iz] - powf(rho_12[ix][iz],2.0)/rho_22[ix][iz] ) );
			CFL_LHS[ix][iz] = (Vp[ix][iz] * dt) * fmin(dx,dz);
			CFL_RHS[ix][iz] = 1.0 / ( ( 9.0 / 8.0 + 1.0 / 24.0 ) * sqrtf(2.0));
		}
	}
		if (verb) sf_warning("Velocity information generated\n");
	/* ------------------------------------------------------------------------ */
	/* Boundary Conditions */
	/* ------------------------------------------------------------------------ */

	/****************************************************************************/
	/*PML structures initialization */
	/****************************************************************************/
	/* ========================================================================= */
	/* define profile of absorption in PML region */
	/* PML thickness, metres */
	thickness_PML_x = NPOINTS_PML * dx;
	thickness_PML_z = NPOINTS_PML * dz;


	if (NPOWER < 1) {
		sf_warning("NPOWER must be greater than 1");
		exit(0);
	}

	/* from Festa and Vilotte */
	ALPHA_MAX_PML = 2.0f*PI*(fmax/2.0f);

	/* Determine maximum Vp */
	Vp_max = 0.0f;
	for (ix=0; ix<fdm->nxpad; ix++) {
		for (iz=0; iz<fdm->nzpad; iz++) {
			if (Vp[ix][iz] > Vp_max) {
				Vp_max = Vp[ix][iz];
			}
		}
	}
		if (verb) sf_warning("Maximum Vp determined\n");
	/* compute d0 */
	d0_x = -1.0f * (NPOWER + 1) * Vp_max * logf(Rcoef) / (2.0f * thickness_PML_x);
	d0_z = -1.0f * (NPOWER + 1) * Vp_max * logf(Rcoef) / (2.0f * thickness_PML_z);

	/* set up buffer arrays */
	for (ix=0; ix<fdm->nxpad; ix++){
		d_x[ix] = 0.0f;
		d_x_half_x[ix] = 0.0f;
		K_x[ix] = 1.0f;
		K_x_half_x[ix] = 1.0f;
		alpha_x[ix] = 0.0f;
		alpha_x_half_x[ix] = 0.0f;
		a_x[ix] = 0.0f;
		a_x_half_x[ix] = 0.0f;
	}

	for (iz=0; iz<fdm->nxpad; iz++){
		d_z[iz] = 0.0f;
		d_z_half_z[iz] = 0.0f;
		K_z[iz] = 1.0f;
		K_z_half_z[iz] = 1.0f;
		alpha_z[iz] = 0.0f;
		alpha_z_half_z[iz] = 0.0f;
		a_z[iz] = 0.0f;
		a_z_half_z[iz] = 0.0f;
	}

	/* origin of the PML layer (position of right edge minus thickness, in meters) */
	xoriginleft = thickness_PML_x;
	xoriginright = (fdm->nxpad - 1)*dx - thickness_PML_x;

	/* -----------------------X Damping Profile-----------------------------------*/
	for (ix=0; ix<fdm->nxpad; ix++) {
		/* abscissa of current grid point along the damping profile */
		xval = dx * (float)ix;

		/* Left Edge */
		if (USE_PML_LEFT) {
			/* define damping profile at the grid points */
			abscissa_in_PML = xoriginleft - xval;
			if (abscissa_in_PML >= 0.0f) {
				abscissa_normalized = abscissa_in_PML / thickness_PML_x;
				d_x[ix] = d0_x * powf(abscissa_normalized, NPOWER);
				/* from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-2 */
				K_x[ix] = 1.0f + (K_MAX_PML - 1.0f) * powf(abscissa_normalized, NPOWER);
				alpha_x[ix] = ALPHA_MAX_PML * (1.0f - abscissa_normalized);
			}

			/* define damping profile at half the grid points */
			abscissa_in_PML = xoriginleft - (xval + dx/2.0f);
			if (abscissa_in_PML >= 0.0f) {
				abscissa_normalized = abscissa_in_PML / thickness_PML_x;
				d_x_half_x[ix] = d0_x * powf(abscissa_normalized, NPOWER);
				/* from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-2 */
				K_x_half_x[ix] = 1.0f + (K_MAX_PML - 1.0f) * powf(abscissa_normalized, NPOWER);
				alpha_x_half_x[ix] = ALPHA_MAX_PML * (1.0f - abscissa_normalized);
			}
		}

		/* Right Edge */
		if (USE_PML_RIGHT) {
			/* define damping profile at the grid points */
			abscissa_in_PML = xval - xoriginright;
			if (abscissa_in_PML >= 0.0f) {
				abscissa_normalized = abscissa_in_PML / thickness_PML_x;
				d_x[ix] = d0_x * powf(abscissa_normalized, NPOWER);
				/* from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-2 */
				K_x[ix] = 1.0f + (K_MAX_PML - 1.0f) * powf(abscissa_normalized, NPOWER);
				alpha_x[ix] = ALPHA_MAX_PML * (1.0f - abscissa_normalized);
			}

			/* define damping profile at half the grid points */
			abscissa_in_PML = xval + dx/2.0f - xoriginright;
			if (abscissa_in_PML >= 0.0f) {
				abscissa_normalized = powf(abscissa_normalized, NPOWER);
				/* from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-2 */
				K_x_half_x[ix] = 1.0f + (K_MAX_PML - 1.0f) * powf(abscissa_normalized,NPOWER);
				alpha_x_half_x[ix] = ALPHA_MAX_PML * (1.0f - abscissa_normalized);
			}
		}

		/* just in case, for -5 at the end */
		if (alpha_x[ix] < 0.0f){
			alpha_x[ix] = 0.0f;
		}
		if (alpha_x_half_x[ix] < 0.0f) {
			alpha_x_half_x[ix] = 0.0f;
		}

		b_x[ix] = expf( -1.0f * ( d_x[ix] / K_x[ix] + alpha_x[ix]) * dt);
		b_x_half_x[ix] = expf(-1.0f * (d_x_half_x[ix] / K_x_half_x[ix] + alpha_x_half_x[ix]) * dt);
		/* ! this to avoid division by zero outside the PML */
		if (fabsf(d_x[ix]) > 1e-6f) {
			a_x[ix] = d_x[ix] * (b_x[ix] - 1.0f) / (K_x[ix] * (d_x[ix] + K_x[ix] * alpha_x[ix]));
		}
		if (fabsf(d_x_half_x[ix]) > 1e-6f) {
			a_x_half_x[ix] = d_x_half_x[ix] * (b_x_half_x[ix] - 1.0f) / (K_x_half_x[ix] * (d_x_half_x[ix] + K_x_half_x[ix] * alpha_x_half_x[ix]));
		}
	}
			if (verb) sf_warning("X Damping Profile Generated\n");
	/* -----------------------Z Damping Profile-----------------------------------*/

	/* Bottom Edge */

	/* Top Edge */



	if (verb) sf_warning("Z Damping Profile Generated\n");

	/* ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
	/*------------------------------------------------------------*/
	/*
	*  MAIN LOOP - actually run stuff
	*/
	/*------------------------------------------------------------*/
	if (verb) fprintf(stderr,"\n");
	/* Begin Time Loop */
	if (verb) sf_warning("Beginning time iteration\n");
	for (it = 0; it < nt; it++) {
		if (verb) fprintf(stderr,"%d/%d \r",it,nt);

		/* Time for Time Step */
		t = (double) it*dt;
		if (verb) sf_warning("Iteration #%i\n",it);


		/* Calculate constituitive relations */
		for (ix = NOP; ix < fdm->nxpad-NOP - 1; ix++) {
			for (iz = NOP + 1; iz < fdm->nzpad-NOP; iz++) {
				/* p(i+1/2,j+1/2), m */
				value_dx_sigmaxx =(27.0f*vx[ix+1][iz]-27.0f*vx[ix][iz]-vx[ix+2][iz]+vx[ix-1][iz])/dx/24.0f;
				value_dz_sigmaxx =(27.0f*vz[ix][iz]-27.0f*vz[ix][iz-1]-vz[ix][iz+1]+vz[ix][iz-2])/dz/24.0f;

				memory_dx_sigmaxx[ix][iz] = b_x_half_x[ix] * memory_dx_sigmaxx[ix][iz] + a_x_half_x[ix] *  Dx(vox,ix,iz,idx);
				memory_dz_sigmaxx[ix][iz] = b_z[iz] * memory_dz_sigmaxx[ix][iz] + a_z[iz] * Dz(voz,ix,iz,idz);

				gamma11[ix][iz] = gamma11[ix][iz] + dt * ( Dx(vox,ix,iz,idx) / K_x_half_x[ix] + memory_dz_sigmaxx[ix][iz]);
				gamma22[ix][iz] = gamma22[ix][iz] + dt * ( Dz(voz,ix,iz,idz) / K_z[iz] + memory_dz_sigmaxx[ix][iz]);

				// p = sigma2

				value_dx_sigma2vxf=(27.0f*vxf[ix+1][iz]-27.0f* vxf(i,j)-vxf(i+2,j)+vxf(i-1,j)) / DELTAX/24.D0
				value_dz_sigma2vzf=(27.0f*vzf[ix,iz]-27.0f*vzf(i,j-1)-vyf(i,j+1)+vyf(i,j-2)) / DELTAY/24.D0

				memory_dx_sigma2vxf[ix][iz] = b_x_half_x[ix] * memory_dx_sigma2vxf[ix][iz] + a_x_half_x[ix] * Dx(qox,ix,iz,idx);
				memory_dz_sigma2vzf[ix][iz] = b_z[iz] * memory_dz_sigma2vzf[ix][iz] + a_z[iz] * Dz(qoz,ix,iz,idz);

				xi_1[ix][iz] = xi_1[ix][iz] - ( Dx(qox,ix,iz,idx) / K_x_half_x[ix] + memory_dx_sigma2vxf[ix][iz]) * dt;
				xi_2[ix][iz] = xi_2[ix][iz] - ( Dz(qoz,ix,iz,idz) / K_z[iz] + memory_dz_sigma2vzf[ix][iz]) * dt;

				p[ix][iz] = -1.0*alpha[ix][iz]*biotmod[ix][iz]*(gamma11[ix][iz] + gamma22[ix][iz]) + biotmod[ix][iz]*(xi_1[ix][iz] + xi_2[ix][iz]);
			}
		}
		if (verb) sf_warning("Pressure information generated\n");


		/*------------------------------------------------------------*/
		/* inject stress source                                       */
		/*------------------------------------------------------------*/
		// if (srctype == STRESS || srctype == TENSOR) {
		//   if (verb) sf_warning("Injecting stress source");
		//   lint2d_bell(tzz,ww[it][0],cs);
		//   lint2d_bell(txx,ww[it][0],cs);
		//   lint2d_bell(  p,ww[it][1],cs);
		// }
		/* Debug pressure source */
		//p[nx/2][nz/2] = p[nx/2][nz/2] + ((exp( -1.0 * (80.0f*80.0f*PI*PI) * pow((t - 0.0f),2.0f) ) / (-2.0f * (80.0f*80.0f*PI*PI) ) )*1e2 ) * biotmod[nx/2][nz/2];


		/* Add pressures sources here */
		lint2d_bell(p,ww[it][0],cs);

		for (ix = NOP + 1; ix < fdm->nxpad-NOP; ix++) {
			for (iz = NOP; iz < fdm->nzpad-NOP - 1; iz++) {
				/* p(i+1/2,j+1/2), m */

				/* interpolate material parameters at the right location in the staggered grid cell */
				c33_half_z = 2.0 / (1.0 / shm[ix][iz] + 1.0 / shm[ix][iz+1]);

				memory_dx_sigmaxz[ix][iz] = b_x[ix] * memory_dx_sigmaxz[ix][iz] + a_x[ix] * Dx(voz,ix,iz,idx);
				memory_dz_sigmaxz[ix][iz] = b_z_half_z[iz] * memory_dz_sigmaxz[ix][iz] + a_z_half_z[iz] * Dz(vox,ix,iz,idz);

				/* txz(i,j+1), m */
				txz[ix][iz] =    txz[ix][iz] + c33_half_z / 1.0f * ( Dx(voz,ix,iz,idx) / K_x[ix] + memory_dx_sigmaxz[ix][iz] + Dz(vox,ix,iz,idz) ) * dt;

				/* txz(i,j+1), m */
			}
		}
		if (verb) sf_warning("Shear stress generated\n");


		/* ========================================================================== */
		for (ix = NOP; ix < fdm->nxpad-NOP - 1; ix++) {
			for (iz = NOP + 1; iz < fdm->nzpad-NOP; iz++) {

				/* txx(i+1/2,j+1/2), m */

				txx[ix][iz] =          shm[ix][iz]   * ( gamma11[ix][iz] ) +
				lambda[ix][iz]   * ( gamma11[ix][iz] + gamma22[ix][iz] ) -
				( alpha[ix][iz]  * p[ix][iz] );

				/* tzz(i+1/2,j+1/2), m */

				tzz[ix][iz] =          shm[ix][iz]   * ( gamma11[ix][iz] + gamma22[ix][iz] ) +
				lambda[ix][iz]   * ( gamma11[ix][iz] ) -
				( alpha[ix][iz]  * p[ix][iz] );
			}
		}

		if (verb) sf_warning("Principal stresses generated\n");
		/* ========================================================================== */
		/* Compute velocity and update memory variables for C-PML */
		/* X - Component */
		for (ix = NOP + 1; ix < fdm->nxpad-NOP; ix++) {
			for (iz = NOP + 1; iz < fdm->nzpad-NOP; iz++) {

				co  = (bro[ix][iz] * shm[ix][iz] - fro[ix][iz]*fro[ix][iz])/dt;
				c1a = co + bro[ix][iz] * fvs[ix][iz]/prm[ix][iz]*0.5f;
				c2  = co - bro[ix][iz] * fvs[ix][iz]/prm[ix][iz]*0.5f;

				memory_dx_vx1[ix][iz] = b_x[ix] * memory_dx_vx1[ix][iz] + a_x[ix] * Dx(txx,ix,iz,idx);
				memory_dx_vx2[ix][iz] = b_x[ix] * memory_dx_vx2[ix][iz] + a_x[ix] * Dx(p,ix,iz,idx);
				memory_dz_vx[ix][iz]  = b_z[iz] * memory_dz_vx[ix][iz]  + a_z[iz] * Dz(txz,ix,iz,idz);

				qpx[ix][iz] = (c2*qox[ix][iz] + ( -1.0f*fro[ix][iz] * ( Dx(txx,ix,iz,idz) / K_x[ix] +
				memory_dx_vx1[ix][iz] + Dz(txz,ix,iz,idz) / K_z[iz] + memory_dz_vx[ix][iz]))) / c1a;

				vpx[ix][iz] = vox[ix][iz] + ( shm[ix][iz]*(Dx(txx,ix,iz,idx) / K_x[ix] + memory_dx_vx1[ix][iz] + Dz(txz,ix,iz,idz) / K_z[iz] +
				memory_dz_vx[ix][iz]) + fro[ix][iz]*(Dx(p,ix,iz,idx) / K_x[ix] + memory_dx_vx2[ix][iz]) +
				fro[ix][iz]*fvs[ix][iz]/prm[ix][iz]*(qox[ix][iz] + qpx[ix][iz])/2.0f) / co;
			}
		}
		if (verb) sf_warning("X Component Velocities Generated\n");
		/* ======================================================================= */
		/* Z - Component */
		for (ix = NOP; ix < fdm->nxpad-NOP-1; ix++) {
			for (iz = NOP; iz < fdm->nzpad-NOP-1; iz++) {

				co = (bro[ix][iz+1] * shm[ix][iz+1] - fro[ix][iz+1]*fro[ix][iz+1])/dt;
				c1a = co + bro[ix][iz+1] * fvs[ix][iz+1]/prm[ix][iz+1]*0.5f;
				c2 = co - bro[ix][iz+1] * fvs[ix][iz+1]/prm[ix][iz+1]*0.5f;

				memory_dx_vz[ix][iz]  = b_x_half_x[ix] * memory_dx_vz[ix][iz]  + a_x_half_x[ix] * Dx(txz,ix,iz,idx);
				memory_dz_vz1[ix][iz] = b_z_half_z[iz] * memory_dz_vz1[ix][iz] + a_z_half_z[iz] * Dz(tzz,ix,iz,idz);
				memory_dz_vz2[ix][iz] = b_z_half_z[iz] * memory_dz_vz2[ix][iz] + a_z_half_z[iz] * Dz(p,ix,iz,idz);

				qpz[ix][iz] = (c2*qoz[ix][iz] + ( -1.0f*fro[ix][iz+1] * ( Dx(txz,ix,iz,idx) / K_x_half_x[ix] + memory_dx_vz[ix][iz] +
				Dz(tzz,ix,iz,idz) / K_z_half_z[iz] + memory_dz_vz1[ix][iz]))) / c1a;

				vpz[ix][iz] = voz[ix][iz] + ( shm[ix][iz+1]*(Dx(txz,ix,iz,idx) / K_x_half_x[ix] + memory_dx_vz[ix][iz] + Dz(tzz,ix,iz,idz) / K_z_half_z[iz] +
				memory_dz_vz1[ix][iz]) + fro[ix][iz+1]*(Dz(p,ix,iz,idz) / K_z_half_z[ix] + memory_dz_vz2[ix][iz]) +
				fro[ix][iz+1]*fvs[ix][iz+1]/prm[ix][iz+1]*(qoz[ix][iz] + qpz[ix][iz])/2.0f) / co;
			}
		}
		if (verb) sf_warning("Z Component Velocities Generated\n");
		/* ======================================================================= */
		/* apply the dirichlet boundary condition                               */
		/* undrained, fixed all around                                */
		/*------------------------------------------------------------*/
		for (ix = 0; ix < fdm->nxpad; ix++){
			for (iz = 0; iz < NOP; iz++){
				vpz[ix][iz] = 0.0f;
				vpx[ix][iz] = 0.0f;
				qpz[ix][iz] = 0.0f;
				qpx[ix][iz] = 0.0f;
			}
		}
		for (ix = 0; ix < fdm->nxpad; ix++){
			for (iz = fdm->nzpad-NOP; iz < fdm->nzpad; iz++){
				vpz[ix][iz] = 0.0f;
				vpx[ix][iz] = 0.0f;
				qpz[ix][iz] = 0.0f;
				qpx[ix][iz] = 0.0f;
			}
		}
		for (ix = 0; ix < NOP; ix++){
			for (iz = 0; iz < fdm->nzpad; iz++){
				vpz[ix][iz] = 0.0f;
				vpx[ix][iz] = 0.0f;
				qpz[ix][iz] = 0.0f;
				qpx[ix][iz] = 0.0f;
			}
		}
		for (ix = fdm->nxpad-NOP; ix < fdm->nxpad; ix++){
			for (iz = 0; iz < fdm->nzpad; iz++){
				vpz[ix][iz] = 0.0f;
				vpx[ix][iz] = 0.0f;
				qpz[ix][iz] = 0.0f;
				qpx[ix][iz] = 0.0f;
			}
		}
		if (verb) sf_warning("dirichlet condition applied\n");
		/*------------------------------------------------------------*/
		/* free surface */
		/*------------------------------------------------------------*/
		/* Francesco: the z component of the traction must be zero at the free surface */
		if (fsrf) {
			for (ix=0; ix < fdm->nxpad; ix++) {
				for (iz=0; iz < fdm->nb; iz++) {
					txx[ix][iz] = 0.0f;
					txz[ix][iz] = 0.0f;
					tzx[ix][iz] = 0.0f;
					tzz[ix][iz] = 0.0f;
					p[ix][iz] = 0.0f;
				}
			}
		}

		/* ========================================================================== */
		/* Check Stability */

		/* ========================================================================== */
		/* circulate wavefield arrays */
		/* Change pointers around */

		/* particle displacement */
		utz=umz; utx=umx;
		umz=uoz; umx=uox;
		uoz=upz; uox=upx;
		upz=utz; upx=utx;

		/* relative displacement */
		wtz=wmz; wtx=wmx;
		wmz=woz; wmx=wox;
		woz=wpz; wox=wpx;
		wpz=wtz; wpx=wtx;

		/* partcle velocity */
		vtz=vmz; vtx=vmx;
		vmz=voz; vmx=vox;
		voz=vpz; vox=vpx;
		vpz=vtz; vpx=vtx;

		/* relative velocity */
		qtz=qmz; qtx=qmx;
		qmz=qoz; qmx=qox;
		qoz=qpz; qox=qpx;
		qpz=qtz; qpx=qtx;

		/*------------------------------------------------------------*/
		/* cut wavefield and save */
		/*------------------------------------------------------------*/
		/*    if (verb) sf_warning("Saving wavefield");*/
		lint2d_extract(p,dd[0],cr);
		lint2d_extract(txz,dd[1],cr);
		/*    if (verb) sf_warning("Wavefield Saved");*/


		/* Output Potentials */
		if (opot){
			if (snap && it%jsnap==0) {
				for  (ix = NOP; ix < fdm->nxpad - NOP; ix++) {
					for (iz = NOP; iz < fdm->nzpad - NOP; iz++) {
						qp[ix][iz] = Dz( voz,ix,iz,idz ) + Dx( vox,ix,iz,idx );
						qs[ix][iz] = Dz( vox,ix,iz,idz ) - Dx( voz,ix,iz,idx );
					}
				}
				cut2d(qp,uc,fdm,acz,acx);
				sf_floatwrite(uc[0],sf_n(acz)*sf_n(acx),Fwfl);

				cut2d(qs,uc,fdm,acz,acx);
				sf_floatwrite(uc[0],sf_n(acz)*sf_n(acx),Fwfl);
			}
			if (it%jdata==0) sf_floatwrite(dd[0],nr*nc,Fdat);
		}
		else {
			/* Save snapshots of wavefield if selected */
			if (snap && it%jsnap==0) {
				/* Export Vz */
				cut2d(voz,uc,fdm,acz,acx);
				sf_floatwrite(uc[0],sf_n(acz)*sf_n(acx),Fwfl);

				/* Export Vx */
				cut2d(vox,uc,fdm,acz,acx);
				sf_floatwrite(uc[0],sf_n(acz)*sf_n(acx),Fwfl);
			}
			if (it%jdata==0) sf_floatwrite(dd[0],nr*nc,Fdat);
		}
		/* Save data snapshots*/
	}
	/* ========================================================================== */
	if (verb) sf_warning("End iterations");
	if (verb) fprintf(stderr,"\n");

	/* ------------------------------------------------------------ */
	/* deallocate arrays */
	/* ------------------------------------------------------------ */
	if (debug) fprintf(stderr,"Finished loop, trying to deallocate...\n");
	free(**ww); free(*ww); free(ww);
	free(ss);
	free(rr);
	free(*dd);  free(dd);
	if (debug) fprintf(stderr,"Deallocating coefficient matrices...\n");

	/*free(**ww); free(*ww); free(ww);*/
	/* free(ss); */
	/* /\* free(rr); *\/ */
	/* free(*dd);  free(dd); */
	/* /\* Only free double pointers that are not null... *\/ */

	/* /\* Free all outstanding parameters *\/ */

	free(*umz); free(umz);
	free(*uoz); free(uoz);
	free(*upz); free(upz);
	free(*uaz); free(uaz);

	free(*umx); free(umx);
	free(*uox); free(uox);
	free(*upx); free(upx);
	free(*uax); free(uax);

	free(*vmz); free(vmz);
	free(*voz); free(voz);
	free(*vpz); free(vpz);
	free(*vaz); free(vaz);

	free(*vmx); free(vmx);
	free(*vox); free(vox);
	free(*vpx); free(vpx);
	free(*vax); free(vax);

	free(*wmz); free(wmz);
	free(*woz); free(woz);
	free(*wpz); free(wpz);
	free(*waz); free(waz);

	free(*wmx); free(wmx);
	free(*wox); free(wox);
	free(*wpx); free(wpx);
	free(*wax); free(wax);

	free(*qmz); free(qmz);
	free(*qoz); free(qoz);
	free(*qpz); free(qpz);
	free(*qaz); free(qaz);

	free(*qmx); free(qmx);
	free(*qox); free(qox);
	free(*qpx); free(qpx);
	free(*qax); free(qax);

	free(*tzz); free(tzz);
	free(*txx); free(txx);
	free(*tzx); free(tzx);
	free(*txz); free(txz);
	if (snap) {free(*uc);  free(uc);}
	if (opot) {free(*qp);  free(qp);}


	exit (0);
	/* ------------end 2d ------------------ */
}
