import rsf.doc

sfbeamsteer = rsf.doc.rsfprog('sfbeamsteer','user/browaeys/Mbeamsteer.c','''Beam steering for 2D surface array. ''')
sfbeamsteer.par('mode',rsf.doc.rsfpar('bool','y','','''if n, beams computed as a function of apparent slowness and azimuth angle. '''))
sfbeamsteer.par('xref',rsf.doc.rsfpar('float','','','''x coordinate where beams are computed '''))
sfbeamsteer.par('yref',rsf.doc.rsfpar('float','','','''y coordinate where beams are computed '''))
sfbeamsteer.par('npx',rsf.doc.rsfpar('int','','','''number of px values (if mode=y). '''))
sfbeamsteer.par('dpx',rsf.doc.rsfpar('float','','','''px sampling (if mode=y). '''))
sfbeamsteer.par('opx',rsf.doc.rsfpar('float','','','''px origin (if mode=y) '''))
sfbeamsteer.par('npy',rsf.doc.rsfpar('int','','','''number of py values (if mode=y). '''))
sfbeamsteer.par('dpy',rsf.doc.rsfpar('float','','','''py sampling (if mode=y). '''))
sfbeamsteer.par('opy',rsf.doc.rsfpar('float','','','''py origin (if mode=y) '''))
sfbeamsteer.version('2.1-git')
sfbeamsteer.synopsis('''sfbeamsteer < in.rsf > out.rsf mode=y xref= yref= npx= dpx= opx= npy= dpy= opy=''','''''')
rsf.doc.progs['sfbeamsteer']=sfbeamsteer

sfbmcgauss = rsf.doc.rsfprog('sfbmcgauss','user/browaeys/Mbmcgauss.c','''Correlated Gaussian joint probability distribution histogram generated with modified Box Mulller algorithm ''')
sfbmcgauss.par('n',rsf.doc.rsfpar('int','100','','''number of random deviates pairs '''))
sfbmcgauss.par('m1',rsf.doc.rsfpar('float','0.0','','''mean for deviate 1 '''))
sfbmcgauss.par('m2',rsf.doc.rsfpar('float','0.0','','''mean for deviate 2 '''))
sfbmcgauss.par('s1',rsf.doc.rsfpar('float','1.0','','''standard deviation for deviate 1 '''))
sfbmcgauss.par('s2',rsf.doc.rsfpar('float','1.0','','''standard deviation for deviate 2 '''))
sfbmcgauss.par('r',rsf.doc.rsfpar('float','0.0','','''correlation coefficient '''))
sfbmcgauss.par('nbin',rsf.doc.rsfpar('int','51','','''number of bins for histogram '''))
sfbmcgauss.par('dbin',rsf.doc.rsfpar('float','0.1','','''histogram bin size '''))
sfbmcgauss.par('obin',rsf.doc.rsfpar('float','0.0','','''histogram origin '''))
sfbmcgauss.par('iseed',rsf.doc.rsfpar('int','-33','','''random generator seed '''))
sfbmcgauss.version('2.1-git')
sfbmcgauss.synopsis('''sfbmcgauss > out.rsf n=100 m1=0.0 m2=0.0 s1=1.0 s2=1.0 r=0.0 nbin=51 dbin=0.1 obin=0.0 iseed=-33''','''''')
rsf.doc.progs['sfbmcgauss']=sfbmcgauss

sfcatan2 = rsf.doc.rsfprog('sfcatan2','user/browaeys/Mcatan2.c','''Argument of complex data calculated by atan2. ''')
sfcatan2.version('2.1-git')
sfcatan2.synopsis('''sfcatan2 < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfcatan2']=sfcatan2

sfcomblist = rsf.doc.rsfprog('sfcomblist','user/browaeys/Mcomblist.c','''Create masks to remove combinations of k elements out of n ''')
sfcomblist.par('k',rsf.doc.rsfpar('int','','','''combination of k elements '''))
sfcomblist.version('2.1-git')
sfcomblist.synopsis('''sfcomblist < in.rsf > out.rsf k=''','''''')
rsf.doc.progs['sfcomblist']=sfcomblist

sfcplxatt = rsf.doc.rsfprog('sfcplxatt','user/browaeys/Mcplxatt.c','''Statistical attributes for circular data. ''')
sfcplxatt.version('2.1-git')
sfcplxatt.synopsis('''sfcplxatt < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfcplxatt']=sfcplxatt

sfcplxcoh = rsf.doc.rsfprog('sfcplxcoh','user/browaeys/Mcplxcoh.c','''Coherency based on complex statistical correlation. ''')
sfcplxcoh.par('nw',rsf.doc.rsfpar('int','','','''half time-window size '''))
sfcplxcoh.version('2.1-git')
sfcplxcoh.synopsis('''sfcplxcoh < in.rsf > out.rsf nw=''','''''')
rsf.doc.progs['sfcplxcoh']=sfcplxcoh

sfcplxcor = rsf.doc.rsfprog('sfcplxcor','user/browaeys/Mcplxcor.c','''Statistical complex correlation for circular data. ''')
sfcplxcor.version('2.1-git')
sfcplxcor.synopsis('''sfcplxcor < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfcplxcor']=sfcplxcor

sfcplxloc = rsf.doc.rsfprog('sfcplxloc','user/browaeys/Mcplxloc.c','''Local coherency and dip based on trace-by-trace complex statistical correlation. ''')
sfcplxloc.par('nw',rsf.doc.rsfpar('int','','','''half time-window size '''))
sfcplxloc.version('2.1-git')
sfcplxloc.synopsis('''sfcplxloc < in.rsf > out.rsf nw=''','''''')
rsf.doc.progs['sfcplxloc']=sfcplxloc

sfdifferr = rsf.doc.rsfprog('sfdifferr','user/browaeys/Mdifferr.c','''Error by substituting numerical solution into equation ''')
sfdifferr.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifferr.par('slowz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifferr.par('slowx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifferr.par('err_cutoff',rsf.doc.rsfpar('float','0.2','',''''''))
sfdifferr.par('iq',rsf.doc.rsfpar('int','2','','''switch for escape variable 0=x, 1=a, 2=t, 3=z '''))
sfdifferr.version('2.1-git')
sfdifferr.synopsis('''sfdifferr < in.rsf > out.rsf slow=slow.rsf slowz=slowz.rsf slowx=slowx.rsf err_cutoff=0.2 iq=2''','''''')
rsf.doc.progs['sfdifferr']=sfdifferr

sfgsray = rsf.doc.rsfprog('sfgsray','user/browaeys/Mgsray.c','''Gauss Seidel iterative solver for phase space escape positions, angle and traveltime ''')
sfgsray.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray.par('slowz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray.par('slowx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray.par('dslow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgsray.par('dtout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgsray.par('iq',rsf.doc.rsfpar('int','','','''switch for escape variable 0=x, 1=a, 2=t, 3=z, 4=l, 5=i '''))
sfgsray.par('niter',rsf.doc.rsfpar('int','50','','''number of Gauss-Seidel iterations '''))
sfgsray.par('liter',rsf.doc.rsfpar('int','0','','''number of first iterations with low-order scheme '''))
sfgsray.par('tol',rsf.doc.rsfpar('float','0.000002*nx*nz','','''accuracy tolerance '''))
sfgsray.par('order',rsf.doc.rsfpar('int','1','','''order of upwind '''))
sfgsray.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfgsray.par('sph',rsf.doc.rsfpar('bool','n','','''true - half-sphere, false - flat B.C. on left/right '''))
sfgsray.par('dslow',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgsray.version('2.1-git')
sfgsray.synopsis('''sfgsray < in.rsf > out.rsf slow=slow.rsf slowz=slowz.rsf slowx=slowx.rsf dslow=dslow.rsf dtout=dtout.rsf iq= niter=50 liter=0 tol=0.000002*nx*nz order=1 verb=n sph=n''','''''')
rsf.doc.progs['sfgsray']=sfgsray

sfkarman = rsf.doc.rsfprog('sfkarman','user/browaeys/Mkarman.c','''Estimation of von Karman autocorrelation 1D spectrum. ''')
sfkarman.par('x0',rsf.doc.rsfpar('float','1.','','''initial squared length scale '''))
sfkarman.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfkarman.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfkarman.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkarman.version('2.1-git')
sfkarman.synopsis('''sfkarman < in.rsf > out.rsf x0=1. niter=100 nliter=1 verb=n''','''''')
rsf.doc.progs['sfkarman']=sfkarman

sfkarmans = rsf.doc.rsfprog('sfkarmans','user/browaeys/Mkarmans.c','''Inversion for von Karman autocorrelation 1D spectrum. ''')
sfkarmans.par('prm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkarmans.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfkarmans.par('x10',rsf.doc.rsfpar('float','6.','','''initial nonlinear parameter x1 value '''))
sfkarmans.par('x20',rsf.doc.rsfpar('float','-0.5','','''initial nonlinear parameter x2 value '''))
sfkarmans.par('x30',rsf.doc.rsfpar('float','200.','','''initial nonlinear parameter x3 value '''))
sfkarmans.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkarmans.version('2.1-git')
sfkarmans.synopsis('''sfkarmans < in.rsf > out.rsf prm=prm.rsf niter=100 x10=6. x20=-0.5 x30=200. verb=n''','''''')
rsf.doc.progs['sfkarmans']=sfkarmans

sfkarman2 = rsf.doc.rsfprog('sfkarman2','user/browaeys/Mkarman2.c','''Estimation of von Karman autocorrelation 2D spectrum by nonlinear separable least squares. ''')
sfkarman2.par('a0',rsf.doc.rsfpar('float','1000.','','''starting correlation length in xx '''))
sfkarman2.par('b0',rsf.doc.rsfpar('float','0.','','''starting correlation length in xy '''))
sfkarman2.par('c0',rsf.doc.rsfpar('float','400.','','''starting correlation length in yy '''))
sfkarman2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfkarman2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkarman2.version('2.1-git')
sfkarman2.synopsis('''sfkarman2 < in.rsf > out.rsf a0=1000. b0=0. c0=400. niter=100 verb=n''','''''')
rsf.doc.progs['sfkarman2']=sfkarman2

sfmcbmcgauss = rsf.doc.rsfprog('sfmcbmcgauss','user/browaeys/Mmcbmcgauss.c','''Monte Carlo integration of cos(2t).P(x1,x2).P(y1,y2) ''')
sfmcbmcgauss.par('n',rsf.doc.rsfpar('int','100','','''number of random deviates pairs '''))
sfmcbmcgauss.par('m1',rsf.doc.rsfpar('float','0.0','','''mean for deviates '''))
sfmcbmcgauss.par('s1',rsf.doc.rsfpar('float','1.0','','''standard deviation for deviates '''))
sfmcbmcgauss.par('iseed',rsf.doc.rsfpar('int','-33','','''random generator seed '''))
sfmcbmcgauss.version('2.1-git')
sfmcbmcgauss.synopsis('''sfmcbmcgauss < in.rsf > out.rsf n=100 m1=0.0 s1=1.0 iseed=-33''','''''')
rsf.doc.progs['sfmcbmcgauss']=sfmcbmcgauss

sfpde2dadp = rsf.doc.rsfprog('sfpde2dadp','user/browaeys/Mpde2dadp.c','''Numerical solution of linear pde 2-d (X-Z-a) for phase space escape positions, angle and traveltime ''')
sfpde2dadp.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpde2dadp.par('slowz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpde2dadp.par('slowx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpde2dadp.par('iq',rsf.doc.rsfpar('int','','','''switch for escape variable 0=x, 1=a, 2=t, 3=z '''))
sfpde2dadp.par('method',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('method_2d',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('niter',rsf.doc.rsfpar('int','100','','''number of Gauss-Seidel iterations '''))
sfpde2dadp.par('ixsmooth',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('izsmooth',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('xsmooth',rsf.doc.rsfpar('float','','',''''''))
sfpde2dadp.par('zsmooth',rsf.doc.rsfpar('float','','',''''''))
sfpde2dadp.par('is_xinf',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('is_zinf',rsf.doc.rsfpar('int','','',''''''))
sfpde2dadp.par('tol',rsf.doc.rsfpar('float','0.000002*nx*nz','','''accuracy tolerance '''))
sfpde2dadp.par('cvgce',rsf.doc.rsfpar('string ',desc='''output file for convergence '''))
sfpde2dadp.version('2.1-git')
sfpde2dadp.synopsis('''sfpde2dadp < in.rsf > out.rsf slow=slow.rsf slowz=slowz.rsf slowx=slowx.rsf iq= method= method_2d= niter=100 ixsmooth= izsmooth= xsmooth= zsmooth= is_xinf= is_zinf= tol=0.000002*nx*nz cvgce=''','''''')
rsf.doc.progs['sfpde2dadp']=sfpde2dadp

sfradonslope2 = rsf.doc.rsfprog('sfradonslope2','user/browaeys/Mradonslope2.c','''Directional angle transform for 3-D time image cube I(x,z,t) into G(x,z,d) ''')
sfradonslope2.par('slowness',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfradonslope2.par('nd',rsf.doc.rsfpar('int','nt','',''''''))
sfradonslope2.par('dd',rsf.doc.rsfpar('float','160.0/(nt-1)','',''''''))
sfradonslope2.par('d0',rsf.doc.rsfpar('float','-80.0','',''''''))
sfradonslope2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfradonslope2.version('2.1-git')
sfradonslope2.synopsis('''sfradonslope2 < Fimgt.rsf > Fimgd.rsf slowness=slowness.rsf nd=nt dd=160.0/(nt-1) d0=-80.0 verb=n''','''''')
rsf.doc.progs['sfradonslope2']=sfradonslope2

sftan2dang = rsf.doc.rsfprog('sftan2dang','user/browaeys/Mtan2dang.c','''2-D slowness vector to angle transformation. ''')
sftan2dang.par('na',rsf.doc.rsfpar('int','360','',''''''))
sftan2dang.par('da',rsf.doc.rsfpar('float','0.5','',''''''))
sftan2dang.par('oa',rsf.doc.rsfpar('float','0.0','',''''''))
sftan2dang.par('nr',rsf.doc.rsfpar('int','2*nsx','','''line summation samples '''))
sftan2dang.par('dr',rsf.doc.rsfpar('float','0.5*dsx','','''line summation sampling '''))
sftan2dang.par('or',rsf.doc.rsfpar('float','osx','','''line summation origin '''))
sftan2dang.version('2.1-git')
sftan2dang.synopsis('''sftan2dang < in.rsf > out.rsf na=360 da=0.5 oa=0.0 nr=2*nsx dr=0.5*dsx or=osx''','''''')
rsf.doc.progs['sftan2dang']=sftan2dang

sfvelmap = rsf.doc.rsfprog('sfvelmap','user/browaeys/Mvelmap.c','''2-D mapping from moving-object velocity to plane-wave slowness ''')
sfvelmap.par('osx',rsf.doc.rsfpar('float','-0.5/dvx','',''''''))
sfvelmap.par('osy',rsf.doc.rsfpar('float','-0.5/dvy','',''''''))
sfvelmap.par('nt',rsf.doc.rsfpar('int','360','','''number of line parameter for integration in [0,180]. '''))
sfvelmap.par('dt',rsf.doc.rsfpar('float','0.5','','''line parameter increment '''))
sfvelmap.par('ot',rsf.doc.rsfpar('float','0.','','''line parameter origin '''))
sfvelmap.version('2.1-git')
sfvelmap.synopsis('''sfvelmap < in.rsf > out.rsf osx=-0.5/dvx osy=-0.5/dvy nt=360 dt=0.5 ot=0.''','''''')
rsf.doc.progs['sfvelmap']=sfvelmap

sfvelsteer = rsf.doc.rsfprog('sfvelsteer','user/browaeys/Mvelsteer.c','''Velocity steering for 2D receivers array. ''')
sfvelsteer.par('nvx',rsf.doc.rsfpar('int','','','''number of vx values '''))
sfvelsteer.par('dvx',rsf.doc.rsfpar('float','','','''vx sampling '''))
sfvelsteer.par('ovx',rsf.doc.rsfpar('float','','','''vx origin '''))
sfvelsteer.par('nvy',rsf.doc.rsfpar('int','','','''number of vy values '''))
sfvelsteer.par('dvy',rsf.doc.rsfpar('float','','','''vy sampling '''))
sfvelsteer.par('ovy',rsf.doc.rsfpar('float','','','''vy origin '''))
sfvelsteer.par('iypi',rsf.doc.rsfpar('int','0','','''first depth position where velocity steering is computed '''))
sfvelsteer.par('iyps',rsf.doc.rsfpar('int','ny-1','','''last depth position where velocity steering is computed '''))
sfvelsteer.par('xp',rsf.doc.rsfpar('float','','','''lateral position where velocity steering is computed '''))
sfvelsteer.version('2.1-git')
sfvelsteer.synopsis('''sfvelsteer < in.rsf > out.rsf nvx= dvx= ovx= nvy= dvy= ovy= iypi=0 iyps=ny-1 xp=''','''''')
rsf.doc.progs['sfvelsteer']=sfvelsteer

sfsqsanaly = rsf.doc.rsfprog('sfsqsanaly','user/browaeys/Msqsanaly.c','''Analytic escape solutions in phase space for constant gradient of slowness squared ''')
sfsqsanaly.par('iq',rsf.doc.rsfpar('int','','','''switch for escape variable 0=x, 1=a, 2=t, 3=z '''))
sfsqsanaly.par('gx',rsf.doc.rsfpar('float','','','''x-gradient of slowness^2 '''))
sfsqsanaly.par('gz',rsf.doc.rsfpar('float','','','''z-gradient of slowness^2 '''))
sfsqsanaly.par('sc',rsf.doc.rsfpar('float','','','''slowness constant '''))
sfsqsanaly.par('xc',rsf.doc.rsfpar('float','','','''x reference '''))
sfsqsanaly.par('zc',rsf.doc.rsfpar('float','','','''z reference '''))
sfsqsanaly.version('2.1-git')
sfsqsanaly.synopsis('''sfsqsanaly < in.rsf > out.rsf iq= gx= gz= sc= xc= zc=''','''''')
rsf.doc.progs['sfsqsanaly']=sfsqsanaly

