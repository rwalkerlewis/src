import rsf.doc

sfwexwfl = rsf.doc.rsfprog('sfwexwfl','user/cwp/Mwexwfl.c','''3-D wavefield extrapolation with extended SSF ''')
sfwexwfl.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexwfl.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwexwfl.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexwfl.par('datum',rsf.doc.rsfpar('int','0','','''datuming flag '''))
sfwexwfl.par('inv',rsf.doc.rsfpar('int','1','','''down/upward flag '''))
sfwexwfl.par('causal',rsf.doc.rsfpar('bool','n','','''causality flag '''))
sfwexwfl.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfwexwfl.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexwfl.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexwfl.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfwexwfl.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfwexwfl.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfwexwfl.version('2.1-git')
sfwexwfl.synopsis('''sfwexwfl slo=Fs.rsf < Fd.rsf > Fw.rsf verb=n eps=0.01 datum=0 inv=1 causal=n nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0''','''''')
rsf.doc.progs['sfwexwfl']=sfwexwfl

sfweximg = rsf.doc.rsfprog('sfweximg','user/cwp/Mweximg.c','''3-D modeling/migration with extended SSF ''')
sfweximg.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfweximg.par('swfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfweximg.par('cc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfweximg.par('rwfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfweximg.par('adj',rsf.doc.rsfpar('int','','','''y=ADJ migration; n=FWD modeling '''))
sfweximg.par('save',rsf.doc.rsfpar('int','0','','''save wfld flag '''))
sfweximg.par('feic',rsf.doc.rsfpar('int','0','','''extended I.C. flag '''))
sfweximg.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfweximg.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfweximg.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfweximg.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfweximg.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfweximg.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfweximg.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfweximg.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfweximg.par('nhx',rsf.doc.rsfpar('int','0','','''number of lags on the x axis '''))
sfweximg.par('nhy',rsf.doc.rsfpar('int','0','','''number of lags on the y axis '''))
sfweximg.par('nhz',rsf.doc.rsfpar('int','0','','''number of lags on the z axis '''))
sfweximg.par('nht',rsf.doc.rsfpar('int','0','','''number of lags on the t axis '''))
sfweximg.par('dht',rsf.doc.rsfpar('float','','',''''''))
sfweximg.par('rwfl',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfweximg.version('2.1-git')
sfweximg.synopsis('''sfweximg slo=Fs.rsf swfl=Fws.rsf < Fm.rsf cc=Fc.rsf > Fd.rsf rwfl=Fwr.rsf adj= save=0 feic=0 verb=n eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nhx=0 nhy=0 nhz=0 nht=0 dht=''','''''')
rsf.doc.progs['sfweximg']=sfweximg

sfwexmig = rsf.doc.rsfprog('sfwexmig','user/cwp/Mwexmig.c','''3-D modeling/migration with extended SSF ''')
sfwexmig.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmig.par('swfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmig.par('cc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmig.par('cip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwexmig.par('feic',rsf.doc.rsfpar('bool','n','','''extended I.C. flag '''))
sfwexmig.par('fdrv',rsf.doc.rsfpar('bool','n','','''image derivative flag '''))
sfwexmig.par('fnew',rsf.doc.rsfpar('bool','n','','''phase-shift flag '''))
sfwexmig.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwexmig.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexmig.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfwexmig.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexmig.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexmig.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y '''))
sfwexmig.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x '''))
sfwexmig.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfwexmig.par('nhx',rsf.doc.rsfpar('int','0','','''number of lags on the x axis '''))
sfwexmig.par('nhy',rsf.doc.rsfpar('int','0','','''number of lags on the y axis '''))
sfwexmig.par('nhz',rsf.doc.rsfpar('int','0','','''number of lags on the z axis '''))
sfwexmig.par('nht',rsf.doc.rsfpar('int','0','','''number of lags on the t axis '''))
sfwexmig.par('dht',rsf.doc.rsfpar('float','','',''''''))
sfwexmig.version('2.1-git')
sfwexmig.synopsis('''sfwexmig slo=Fs.rsf swfl=Fws.rsf < Fd.rsf > Fm.rsf cc=Fc.rsf cip=Fe.rsf feic=n fdrv=n fnew=n verb=n eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nhx=0 nhy=0 nhz=0 nht=0 dht=''','''''')
rsf.doc.progs['sfwexmig']=sfwexmig

sfwexmva = rsf.doc.rsfprog('sfwexmva','user/cwp/Mwexmva.c','''3-D S/R WEMVA with extended split-step ''')
sfwexmva.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmva.par('swfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmva.par('rwfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmva.par('cc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexmva.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfwexmva.par('adj',rsf.doc.rsfpar('int','','','''y=ADJ Back-projection; n=FWD Forward Scattering '''))
sfwexmva.par('feic',rsf.doc.rsfpar('int','','','''extended I.C. flag '''))
sfwexmva.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexmva.par('nrmax',rsf.doc.rsfpar('int','1','','''max number of refs '''))
sfwexmva.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexmva.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexmva.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y '''))
sfwexmva.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x   '''))
sfwexmva.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y   '''))
sfwexmva.par('nhx',rsf.doc.rsfpar('int','0','','''number of lags on the x axis '''))
sfwexmva.par('nhy',rsf.doc.rsfpar('int','0','','''number of lags on the y axis '''))
sfwexmva.par('nhz',rsf.doc.rsfpar('int','0','','''number of lags on the z axis '''))
sfwexmva.par('nht',rsf.doc.rsfpar('int','0','','''number of lags on the t axis '''))
sfwexmva.par('dht',rsf.doc.rsfpar('float','','',''''''))
sfwexmva.version('2.1-git')
sfwexmva.synopsis('''sfwexmva slo=Bs.rsf < Pi.rsf < Ps.rsf swfl=Bws.rsf rwfl=Bwr.rsf cc=Fc.rsf verb=y adj= feic= eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nhx=0 nhy=0 nhz=0 nht=0 dht=''','''''')
rsf.doc.progs['sfwexmva']=sfwexmva

sfwexnmig = rsf.doc.rsfprog('sfwexnmig','user/cwp/Mwexnmig.c','''3-D modeling/migration with extended SSF ''')
sfwexnmig.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexnmig.par('swfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexnmig.par('dipx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexnmig.par('dipy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexnmig.par('cc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexnmig.par('cip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwexnmig.par('feic',rsf.doc.rsfpar('bool','n','','''extended I.C. flag '''))
sfwexnmig.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwexnmig.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexnmig.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfwexnmig.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexnmig.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexnmig.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfwexnmig.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfwexnmig.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfwexnmig.par('nhx',rsf.doc.rsfpar('int','0','','''number of lags on the x axis '''))
sfwexnmig.par('nhy',rsf.doc.rsfpar('int','0','','''number of lags on the y axis '''))
sfwexnmig.par('nhz',rsf.doc.rsfpar('int','0','','''number of lags on the z axis '''))
sfwexnmig.par('nht',rsf.doc.rsfpar('int','0','','''number of lags on the t axis '''))
sfwexnmig.par('dht',rsf.doc.rsfpar('float','','',''''''))
sfwexnmig.par('dhx',rsf.doc.rsfpar('float','cub->amx.d*2','',''''''))
sfwexnmig.par('dhy',rsf.doc.rsfpar('float','cub->amy.d*2','',''''''))
sfwexnmig.par('dhz',rsf.doc.rsfpar('float','cub->az.d*2','',''''''))
sfwexnmig.version('2.1-git')
sfwexnmig.synopsis('''sfwexnmig slo=Fs.rsf swfl=Fws.rsf dipx=Fdx.rsf dipy=Fdy.rsf < Fd.rsf > Fm.rsf cc=Fc.rsf cip=Fe.rsf feic=n verb=n eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nhx=0 nhy=0 nhz=0 nht=0 dht= dhx=cub->amx.d*2 dhy=cub->amy.d*2 dhz=cub->az.d*2''','''''')
rsf.doc.progs['sfwexnmig']=sfwexnmig

sfwexzomva = rsf.doc.rsfprog('sfwexzomva','user/cwp/Mwexzomva.c','''3-D S/R WEMVA with extended split-step ''')
sfwexzomva.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexzomva.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexzomva.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfwexzomva.par('adj',rsf.doc.rsfpar('int','','','''y=ADJ Back-projection; n=FWD Forward Scattering '''))
sfwexzomva.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexzomva.par('nrmax',rsf.doc.rsfpar('int','1','','''max number of refs '''))
sfwexzomva.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexzomva.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexzomva.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y '''))
sfwexzomva.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x   '''))
sfwexzomva.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y   '''))
sfwexzomva.version('2.1-git')
sfwexzomva.synopsis('''sfwexzomva slo=Bs.rsf < Pi.rsf < Ps.rsf wfl=Bwr.rsf verb=y adj= eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0''','''''')
rsf.doc.progs['sfwexzomva']=sfwexzomva

sfwexzoimg = rsf.doc.rsfprog('sfwexzoimg','user/cwp/Mwexzoimg.c','''3-D zero-offset modeling/migration with extended SSF ''')
sfwexzoimg.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwexzoimg.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwexzoimg.par('adj',rsf.doc.rsfpar('int','','','''y=ADJ migration; n=FWD modeling '''))
sfwexzoimg.par('save',rsf.doc.rsfpar('int','0','','''save wfld flag '''))
sfwexzoimg.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwexzoimg.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfwexzoimg.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfwexzoimg.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfwexzoimg.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfwexzoimg.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfwexzoimg.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfwexzoimg.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfwexzoimg.par('nw',rsf.doc.rsfpar('int','','',''''''))
sfwexzoimg.par('dw',rsf.doc.rsfpar('float','','',''''''))
sfwexzoimg.par('ow',rsf.doc.rsfpar('float','0.','',''''''))
sfwexzoimg.version('2.1-git')
sfwexzoimg.synopsis('''sfwexzoimg < Fm.rsf < Fd.rsf slo=Fs.rsf wfl=Fwr.rsf adj= save=0 verb=n eps=0.01 nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nw= dw= ow=0.''','''''')
rsf.doc.progs['sfwexzoimg']=sfwexzoimg

sfawesg = rsf.doc.rsfprog('sfawesg','user/cwp/Mawesg.c','''Acoustic staggered-gridded time-domain FD modeling,''')
sfawesg.par('bulk',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawesg.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawesg.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawesg.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawesg.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawesg.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfawesg.par('ompnth',rsf.doc.rsfpar('int','0','','''OpenMP available threads '''))
sfawesg.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfawesg.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfawesg.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfawesg.par('abc',rsf.doc.rsfpar('bool','n','','''ABC if the abcpml=n: spongeABC '''))
sfawesg.par('pml',rsf.doc.rsfpar('bool','n','','''"PML ABC" '''))
sfawesg.par('debug',rsf.doc.rsfpar('bool','n','','''debug '''))
sfawesg.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfawesg.par('jsnap',rsf.doc.rsfpar('int','nt','','''save wavefield every *jsnap* time steps '''))
sfawesg.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','',''''''))
sfawesg.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','',''''''))
sfawesg.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','',''''''))
sfawesg.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','',''''''))
sfawesg.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','',''''''))
sfawesg.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','',''''''))
sfawesg.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','',''''''))
sfawesg.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','',''''''))
sfawesg.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','',''''''))
sfawesg.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','',''''''))
sfawesg.version('2.1-git')
sfawesg.synopsis('''sfawesg < Fwav.rsf bulk=Fbulk.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf ompchunk=1 ompnth=0 verb=n snap=n free=n abc=n pml=n debug=n jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax) nqz=sf_n(az) nqx=sf_n(ax) nqy=sf_n(ay) oqz=sf_o(az) oqx=sf_o(ax) oqy=sf_o(ay)''','''automatically determines whether or not to use 3D or 2D.

Acoustic wave equation finite difference modeling in both 2D and 3D, using an explicit time-domain solver.

*** Please see the SConstruct in book/tutorial/ewe for a SConstruct that demonstrates how to use 
predefined functions for using this program. ***

This program solves a system of first-order PDE's for pressure and particle velocity using a staggered-grid approach.
The model parameters are incompressibility (K: bulk modulus) and density.

The program is parallelized using OpenMP, so be sure to use a compatible compiler to take
advantage of the performance boost

============= STAGGERED-GRID   ========================

		o -- x -- o -- x -- o -- x -- o
		|    |    |    |    |    |    |
		x -- x -- x -- x -- x -- x -- x
		|    |    |    |    |    |    |
		o -- x -- o -- x -- o -- x -- o

The "o"'s are the points where the pressures at computed (integer grid). The "x"'s 
are the points where the particle velocities are computed (half grid).

============= FILE DESCRIPTIONS   ========================      

Fdat.rsf - An RSF file containing your data in the following format:
axis 1 - source location
axis 2 - wavefield component (z,x,y) order
axis 3 - Time
			
Fwav.rsf - An RSF file containing your VOLUME DENSITY INJECTION RATE AND DENSITY OF FORCE 
wavelet information.  The sampling interval, origin time, 
and number of time samples will be used as the defaults for the modeling code.
	       i.e. your wavelet needs to have the same length and parameters that you want to model with!
	       The first axis is the number of source locations.
	       The second axis contains [fz, fx, (fy,) q],respectively. If the file is 1D then the source is assumed
	       to be a isotropic pressure source.
	       The third axis is time.
	       The code check the dimensions of the model and the dimensions of the wavelt file; for 2D modeling, the wavelet
	       file may have n2=1 or n2=3, for 3D modeling, n2=1 or n2=4.  An error is returned if the dimensions don't match.
		   
Fbulk.rsf - An N dimensional RSF file that contains the values for the incompressibility (bulk modulus K) at every point in the computational domain.
		
Fden.rsf - An N dimensional RSF file that contains the values for density at every point in the computational domain.

Fsou.rsf, Frec.rsf - The source and receiver RSF files respectively.  
The 1st axis contains the locations for the points like so:
				   [x,y,z]
The second axis is a concatenated list of all points in the list.
				   So, for an array of receivers, it would look like:
[x1,y1,z1]
[x2,y2,z2]
[x3,y3,z3]
[x4,y4,z4]
				   
Fwfl.rsf     - The name of the file to save the PRESSURE wavefield snapshots to.  This will be an N+2 
dimensional file.  The file will be organized as follows:
1-2(3) axes, spatial coordinates
3(4) axis, wavefield value
4(5) axis, time, sequential snapshots
***The parentheses indicate what the axes will be for 3D models.

Fdat.rsf     - The name of the file to save the receiver data to.  The data has the format of:
	      spatial coordinates, then value of the wavefield.  Lastly, time.
		  
======= PARAMETERS ========

free = y/[n]   - Free surface boundary condition (the free surface is for PRESSURE).

abc  = y/[n]   - Absorbing Boundary Conditions (PML).

nb             - thickness of the absorbing boundary  

verb = y/[n]   - verbosity flag


		  		  
======= TIPS ========

If the simulation seems to slow down as it's running, its a pretty
good indication that the simulation has become unstable and is overflowing
with NaNs.

''')
rsf.doc.progs['sfawesg']=sfawesg

sfcipcut = rsf.doc.rsfprog('sfcipcut','user/cwp/Mcipcut.c','''cut at CIPs ''')
sfcipcut.par('cip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcipcut.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfcipcut.version('2.1-git')
sfcipcut.synopsis('''sfcipcut < Fcub.rsf cip=Fcip.rsf > Fcut.rsf verb=n''','''''')
rsf.doc.progs['sfcipcut']=sfcipcut

sfewefdm = rsf.doc.rsfprog('sfewefdm','user/cwp/Mewefdm.c','''Elastic time-domain FD modeling, automatically determines whether or not to use 3D or 2D, supports different types of elastic.''')
sfewefdm.par('ccc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefdm.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefdm.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefdm.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfewefdm.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfewefdm.par('srctype',rsf.doc.rsfpar('int','0','','''source type, see comments '''))
sfewefdm.par('ani',rsf.doc.rsfpar('int','-1','','''Anisotropy type, see comments '''))
sfewefdm.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfewefdm.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfewefdm.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfewefdm.par('dabc',rsf.doc.rsfpar('bool','y','','''use sponge absorbing BC '''))
sfewefdm.par('abcone',rsf.doc.rsfpar('bool','n','','''use sharp brake at end of boundary layer '''))
sfewefdm.par('debug',rsf.doc.rsfpar('bool','y','','''print debugging info '''))
sfewefdm.par('cfl',rsf.doc.rsfpar('bool','y','','''use CFL check, will cause program to fail if not satisfied '''))
sfewefdm.par('opot',rsf.doc.rsfpar('bool','n','','''output potentials '''))
sfewefdm.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','',''''''))
sfewefdm.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','',''''''))
sfewefdm.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','',''''''))
sfewefdm.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','',''''''))
sfewefdm.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','',''''''))
sfewefdm.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','',''''''))
sfewefdm.par('nbell',rsf.doc.rsfpar('int','1','','''bell size '''))
sfewefdm.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfewefdm.par('nb',rsf.doc.rsfpar('int','100','','''padding size for absorbing boundary '''))
sfewefdm.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfewefdm.par('fmax',rsf.doc.rsfpar('float','','',''''''))
sfewefdm.version('2.1-git')
sfewefdm.synopsis('''sfewefdm < Fwav.rsf ccc=Fccc.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf srctype=0 ani=-1 verb=y snap=n free=n dabc=y abcone=n debug=y cfl=y opot=n nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax) nqy=sf_n(ay) oqy=sf_o(ay) nbell=1 jdata=1 nb=100 jsnap=nt fmax=''','''
Elastic wave equation finite difference modeling in both 2D and 3D, using an explicit time-domain solver.

*** Please see the SConstruct in book/tutorial/ewe for a SConstruct that demonstrates how to use 
predefined functions for using this program. ***

This program is designed to be as generic as possible, and allows you to use files
with arbitrary models, and arbitrary source and receiver geometries.  Source types are
as generic as possible.  Supports arbitrary types of anisotropy as well.  

The downside to the generality, is that the program is not as performant as dedicated solvers
that are less flexible.  The program is parallelized using OpenMP, so be sure to use a compatible compiler to take
advantage of the performance boost.
=========== Rotated Staggered grid ==========================
Ux,Uz=====================Ux,Uz
||            |             || 
||                          ||
||            |             ||
||             tij          ||
||- - - - - - |- - - - - - -|| 
||             Cij          ||
||            |             ||
||                          ||
||            |             ||
Ux,Uz=====================Ux,Uz
===========  OPTIONS  ======================================= 
ani - The type of anisotropy for this simulation.  Valid options:
For 2D:
ISO/HTI/VTI = 0
TTI = 1

For 3D:
ISO/HTI/VTI = 0
TTI    = 1

VTI, HTI, and Isotropic media are special cases of ISO/HTI/VTI media. 
TTI media can be represented using TTI media.

cfl   - Execute the CFL check.  If the CFL check fails, then it will cause the program to fail. 
The CFL check will check both the stability and accuracy conditions for both p-waves and
s-waves. Depending on the type of anisotropy that you specify, the CFL condition will
use a safety factor (that you can override if necessary).  

NOTE: the CFL condition will return both minimum and maximum
constraints on the grid given your velocity model, desired frequency content, and other
parameters.  IT IS POSSIBLE TO HAVE NO STABLE, AND ACCURATE SOLUTIONS FOR A GIVEN 
MODEL WITH GIVEN PARAMETERS. THE CFL CONDITION WILL WARN YOU IF THIS IS THE CASE.

YOU MUST SPECIFY fmax Parameter as well!

----- STABILITY ------
The stability condition is related to the maximum wave speed and minimum grid sampling
as follows:

dt < min(dx,dy,dz) / (sqrt(2)*vmax)

Given a time sampling dt, it is possible to determine the minimum dx,dy,dz for stability.
vmax is the MAXIMUM velocity for all waves in the model (usually P-wave velocity).

For elastic FD, the P-wave most greatly influences the stability, as it moves fastest
on the grid.  

The stability condition gives us a LOWER bound on the grid sampling for a given dt.

------ ACCURACY -------
The accuracy condition is related to the number of gridpoints per wavelength.  Thus,

safety*vmin / fmax > N * sqrt(dx^2+dy^2+dz^2) 

where vmin is the minimum wave velocity in the model (usually S-wave), fmax is some
relative measure of the maximum frequency of your wavelet (usually 1.5*peak for Ricker), 
N is the number of points desired per wavelength (5), and safety is a safety factor that 
is dependent on the type of anisotropy.  

For elastic FD, the S-wave most greatly impacts the accuracy of the solution, as the S-wave
is typically much higher frequency and travels at slower wave speeds, meaning shorter 
wavelengths.  

The accuracy condition places an UPPER bound on the grid sampling.

---- SAFETY FACTOR -----
The safety factor depends on the type of anisotropy specified, and attempts to place a lower
bound on the slowest S-wave velocity (guess):

ISO/HTI/VTI - (3/4)
TTI    - (1/2)

You can also override the safety factor using the safety parameter.
safety- Override the safety factor for the CFL condition.  This should be a floating point (0-1.0).
fmax  - An estimate of the highest frequency content in your wavelet (for Ricker use 1.5*peak)

fsrf  - Use a free surface at the top boundary (z=0).  
WARNING: The free surface condition appears to introduce numerical artifacts into the simulation.  
USE AT YOUR OWN RISK.

snap  - Save snapshots of the wavefield every n iterations of the modeling program. 

jsnap - Number of iterations between snapshots of the wavefield.  
	    i.e. jsnap=10, means save a snapshot every 10 iterations. 
	    If you had 1000 total iterations, then you would have 100 snapshots total.
	    The default, will output no snapshots.

jdata - Number of time imterations between exporting the data at the receivers.
	    i.e. jdata=1, means save a snapshot every iteration, which should be the default.
	    This can be used to change the sampling of the data to something different from 
the wavelet/wavefield.

verb  - Print useful information
debug - Print debugging information.  This is more detailed than verbose.

srctype - An integer which determines where the source wavelet is injected
in the simulation.  Valid options are:  
0 - Acceleration source
1 - Displacement source
2 - Stress source
3 - Tensor source
The default option is 2: Acceleration source.
For Stress, Displacement and Acceleration sources, your wavelet
needs to have only 3 components (z,x,y).
For a Tensor source, you must specify wavelet components for 
all 3 (2D) or 6 (3D) tensor components in the following order:
2D: tzz, txx, tzx
3D: tzz, txx, tyy, tyz, tzx, txy

Hint:  To inject an acoustic source, use a stress source,
with equal components on all three components.

dabc  - Use a sponge layer to attenuate waves off the edge of the grid.  Use this in 
combination with the nb parameter.
abcone- In addition to the sponge layer, using a severe ramp at the very edge of the expanded 
sponge layer to severely attenuate zero-incidence waves at the boundaries. 
It's not clear if this condition actually affects most computations.
opot  - True: output is second spatial derivative of potentials; False: output wavefield.
nbell - Size of gaussian used to linearly interpolate curves.  A value of 5 seems to work well.  
nb    - Not listed, but is an important parameter.  Allows you to control the size of the sponge 
layer for the absorbing boundary condition.  If you are getting reflections off the sides, 
with dabc=y, then make this number larger (int).  This pads the grid by this amount on all sides.  
For example:
|--------------------------|
|            ramp layer    |
|r |--------------------|  |
|a |        nb          |r |
|m |      |~~~~~~~~|    |a |
|p |      |  MODEL |    |m |
|  |  nb  |  SPACE | nb |p |
|  |      |~~~~~~~~|    |  |
|  |         nb         |  |
|  |--------------------|  |
|         ramp layer       |
|--------------------------| 
nqz, nqx, oqz, oqx, nqy, oqy, - Allows you to set the parameters for the axes.  Leave as defaults.

=============BOUNDARY CONDITIONS ========================

This code enforces a fixed reflecting boundary condition at the 
edge of the computational domain.  The absorbing sponge is used
IN ADDITION to this condition.

=============FILE DESCRIPTIONS   ========================      

Fdat.rsf - An RSF file containing your data in the following format:
axis 1 - source location
axis 2 - wavefield component (z,x,y) order
axis 3 - Time

Fwav.rsf - An RSF file containing your wavelet information.  For elastic modeling, the wavelet needs 
to have 3 samples on N1 one for each component Z-X-Y (or just Z-X for 2D).  The second 
axis describes the component as a function of time.  The sampling interval, origin time, 
and number of time samples will be used as the defaults for the modeling code.
	       i.e. your wavelet needs to have the same length and parameters that you want to model with!
	   Ex:
	   1st axis    index
	   Z component  0     0 0 0 0 0 0 0 0 1 2 3 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	   X component  1     0 0 0 0 0 0 0 0 1 2 3 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	   Y component  2     0 0 0 0 0 0 0 0 1 2 3 2 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
				    2nd axis
NOTE: For tensor sources, you must have an appropriate number of components.  See srctype for more information.

cccc  - An N+1 dimensional RSF file that contains the values for the stiffness coefficients to be used 
as the model for the modeling code.  So, for 2D, this would be a 3D array of values concatenated 
together in the order as described in the anisotropy section.  Each coefficient file contains 
the value of that coefficient for every point in space. 
The axes for this file are: Axis 1: Z; Axis 2: X; Axis 3: Y;

The stiffness tensor coefficients are defined uniformly as follows, where 
--x---y---z--(y)-----(y) describes how the coefficients depend on space.
|C11 C12 C13 C14 C15 C16|
|    C22 C23 C24 C25 C26|
|        C33 C34 C35 C36|
|            C44 C45 C46|
|                C55 C56|
|                    C66|

The tensor is assumed to be symmetric.  

Order of the coefficients in the N+1 dimensional file...
(First coefficient is the first 2D array in the 3D array).
2D Anisotropy Modes:

ISO/HTI/VTI: C11, C33, C55, C13
"TTI:" C11, C13, C15, C33, C35, C55 
***TTI basically allows access to all coefs in 2D, but is not really triclinic media
------------------------------------------------------------
(First coefficient is the first 3D array in the 4D array).
3D Anisotropy Modes:

ISO/HTI/VTI: C11, C22, C33, C44, C55, C66, C12, C13, C23
TTI: C11, C12, C13, C14, C15, C16, C22, C23, C24, C25, C26, C33, C34, 
C35, C36, C44, C45, C46, C55, C56, C66


den      - An N dimensional RSF file that contains the valuese for the density to be used for the model.  
For 2D, this would be a 2D array.  

sou, rec -The source and receiver RSF files respectively.  
The 1st axis contains the locations for the points like so:
[x,y,z]
The second axis is a concatenated list of all points in the list.
So, for an array of receivers, it would look like:
[x1,y1,z1]
[x2,y2,z2]
[x3,y3,z3]
[x4,y4,z4]

wfl     - The name of the file to save the wavefield snapshots to.  This will be an N+2 
dimensional file.  The file will be organized as follows:
1-2(3) axes, spatial coordinates
3(4) axis, wavefield components, in the Z,X,(Y) order
4(5) axis, time, sequential snapshots
***The parentheses indicate what the axes will be for 3D models.

dat     - The name of the file to save the receiver data to.  The data has the format of:
	      spatial coordinates, then the data components of the elastic wavefield in the 
	      same order as the wavefield.  Lastly, time.

========== USEFUL COMMANDS  ============================= 	  

To view the wavefield snapshots (2D case):
sfwindow < Fwfl.rsf n3=1 f3=0 | sfgrey gainpanel=a pclip=100 | sfpen

To view the data (2D case):
sfwindow < Fdat.rsf n3=1 f3=0 | sfgrey gainpanel=a pclip=100 | sfpen

========== TROUBLESHOOTING ===============================

If you aren't getting output, or your output is full of Nans, make sure
that you have the proper dimensions for your wavelet files, and that
your input files make sense.

Make sure your source and receiver points are located inside the 
model space, otherwise you will get all NaNs and the simulation will
run forever.

======= TIPS ========

If the simulation seems to slow down as it's running, its a pretty
good indication that the simulation has become unstable and is overflowing
with NaNs.


Modified by Yuting Duan, Colorado School of Mines,2013-10-22. 

''')
rsf.doc.progs['sfewefdm']=sfewefdm

sfawefd2d = rsf.doc.rsfprog('sfawefd2d','user/cwp/Mawefd2d.c','''2D acoustic time-domain FD modeling ''')
sfawefd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd2d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfawefd2d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfawefd2d.par('expl',rsf.doc.rsfpar('bool','n','','''Multiple sources, one wvlt'''))
sfawefd2d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfawefd2d.par('cden',rsf.doc.rsfpar('bool','n','','''Constant density '''))
sfawefd2d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfawefd2d.par('fsrf',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfawefd2d.par('optfd',rsf.doc.rsfpar('bool','n','','''optimized FD coefficients flag '''))
sfawefd2d.par('fdorder',rsf.doc.rsfpar('int','4','','''spatial FD order '''))
sfawefd2d.par('hybridbc',rsf.doc.rsfpar('bool','n','','''hybrid Absorbing BC '''))
sfawefd2d.par('sinc',rsf.doc.rsfpar('bool','n','','''sinc source injection '''))
sfawefd2d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfawefd2d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfawefd2d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfawefd2d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfawefd2d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfawefd2d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfawefd2d.par('dqz',rsf.doc.rsfpar('float','sf_d(az)','','''Saved wfld window dz '''))
sfawefd2d.par('dqx',rsf.doc.rsfpar('float','sf_d(ax)','','''Saved wfld window dx '''))
sfawefd2d.par('den',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfawefd2d.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfawefd2d')
sfawefd2d.version('2.1-git')
sfawefd2d.synopsis('''sfawefd2d < file_wav.rsf vel=file_vel.rsf sou=file_src.rsf rec=file_rec.rsf > file_dat.rsf wfl=file_wfl.rsf den=file_den.rsf verb=n snap=n expl=n dabc=n cden=n adj=n fsrf=n optfd=n fdorder=4 hybridbc=n sinc=n jsnap=nt jdata=1 nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax) dqz=sf_d(az) dqx=sf_d(ax)''','''2Nth order in space, 2nd order in time
with optimized FD scheme option and hybrid one-way ABC option 
adj flag indicates backwards source injection, not exact adjoint propagator
''')
rsf.doc.progs['sfawefd2d']=sfawefd2d

sfawefd3d = rsf.doc.rsfprog('sfawefd3d','user/cwp/Mawefd3d.c','''3D acoustic time-domain FD modeling ''')
sfawefd3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd3d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfawefd3d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfawefd3d.par('expl',rsf.doc.rsfpar('bool','n','','''Multiple sources, one wvlt'''))
sfawefd3d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfawefd3d.par('cden',rsf.doc.rsfpar('bool','n','','''Constant density '''))
sfawefd3d.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfawefd3d.par('fsrf',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfawefd3d.par('optfd',rsf.doc.rsfpar('bool','n','','''optimized FD coefficients flag '''))
sfawefd3d.par('fdorder',rsf.doc.rsfpar('int','4','','''spatial FD order '''))
sfawefd3d.par('hybridbc',rsf.doc.rsfpar('bool','n','','''hybrid Absorbing BC '''))
sfawefd3d.par('sinc',rsf.doc.rsfpar('bool','n','','''sinc source injection '''))
sfawefd3d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfawefd3d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfawefd3d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfawefd3d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfawefd3d.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','','''Saved wfld window ny '''))
sfawefd3d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfawefd3d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfawefd3d.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','','''Saved wfld window oy '''))
sfawefd3d.par('dqz',rsf.doc.rsfpar('float','sf_d(az)','','''Saved wfld window dz '''))
sfawefd3d.par('dqx',rsf.doc.rsfpar('float','sf_d(ax)','','''Saved wfld window dx '''))
sfawefd3d.par('dqy',rsf.doc.rsfpar('float','sf_d(ay)','','''Saved wfld window dy '''))
sfawefd3d.par('den',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfawefd3d.version('2.1-git')
sfawefd3d.synopsis('''sfawefd3d < file_wav.rsf vel=file_vel.rsf sou=file_src.rsf rec=file_rec.rsf > file_dat.rsf wfl=file_wfl.rsf den=file_den.rsf verb=n snap=n expl=n dabc=n cden=n adj=n fsrf=n optfd=n fdorder=4 hybridbc=n sinc=n jsnap=nt jdata=1 nqz=sf_n(az) nqx=sf_n(ax) nqy=sf_n(ay) oqz=sf_o(az) oqx=sf_o(ax) oqy=sf_o(ay) dqz=sf_d(az) dqx=sf_d(ax) dqy=sf_d(ay)''','''2Nth order in space, 2nd order in time
with optimized FD scheme option and hybrid one-way ABC option 
adj flag indicates backwards source injection, not exact adjoint propagator
''')
rsf.doc.progs['sfawefd3d']=sfawefd3d

sfdbmerge = rsf.doc.rsfprog('sfdbmerge','user/cwp/Mdbmerge.py','''''')
sfdbmerge.version('2.1-git')
sfdbmerge.synopsis('''sfdbmerge''','''A program that can be used to merge separate SCons databases together.  Typically used when an SConstruct is split
into multiple pieces (e.g. on a cluster).

args:
outdb - path of the output database

strings - names of the databases to merge together
''')
rsf.doc.progs['sfdbmerge']=sfdbmerge

sfmpiencode = rsf.doc.rsfprog('sfmpiencode','user/cwp/Mmpiencode.c','''shot encoding with arbitrary phase and amplitude weights using MPI on a distributed cluster ''')
sfmpiencode.par('encode',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpiencode.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfmpiencode.par('dprefix',rsf.doc.rsfpar('string ',desc='''printf like statement that can be evaluated to find the data files corresponding to shot records '''))
sfmpiencode.par('eprefix',rsf.doc.rsfpar('string ',desc='''printf like statement that can be evaluated for the output encodings '''))
sfmpiencode.version('2.1-git')
sfmpiencode.synopsis('''sfmpiencode encode=Fencode.rsf verb=n dprefix= eprefix=''','''* axes are x-y-w

''')
rsf.doc.progs['sfmpiencode']=sfmpiencode

sfbigmpiencode = rsf.doc.rsfprog('sfbigmpiencode','user/cwp/Mbigmpiencode.c','''shot encoding with arbitrary phase and amplitude weights using MPI on a distributed cluster ''')
sfbigmpiencode.par('encode',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbigmpiencode.par('nx',rsf.doc.rsfpar('int','','','''# of output grid x points '''))
sfbigmpiencode.par('ny',rsf.doc.rsfpar('int','','','''# of output grid y points '''))
sfbigmpiencode.par('dy',rsf.doc.rsfpar('float','','','''dy of output grid points '''))
sfbigmpiencode.par('dx',rsf.doc.rsfpar('float','','','''dx of output grid points '''))
sfbigmpiencode.par('ox',rsf.doc.rsfpar('float','','','''ox of output grid points '''))
sfbigmpiencode.par('oy',rsf.doc.rsfpar('float','','','''ox of output grid points '''))
sfbigmpiencode.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfbigmpiencode.par('dprefix',rsf.doc.rsfpar('string ',desc='''printf like statement that can be evaluated to find the data files corresponding to shot records '''))
sfbigmpiencode.par('eprefix',rsf.doc.rsfpar('string ',desc='''printf like statement that can be evaluated for the output encodings '''))
sfbigmpiencode.par('shots',rsf.doc.rsfpar('string ',desc='''shot-file name, dimensions are 1xNS '''))
sfbigmpiencode.version('2.1-git')
sfbigmpiencode.synopsis('''sfbigmpiencode encode=Fencode.rsf nx= ny= dy= dx= ox= oy= verb=n dprefix= eprefix= shots=''','''

Use mpiencode if your shots are on the same grid prior to encoding.

Use bigmpiencode if your shots are not on a single grid prior to encoding.
YOUR SHOTS MUST ALL FALL ONTO THE SAME REGULAR GRID.  BigMPIENCODE does not do any
shot interpolation.

Data axes - X, Y, W

''')
rsf.doc.progs['sfbigmpiencode']=sfbigmpiencode

sfmpistack = rsf.doc.rsfprog('sfmpistack','user/cwp/Mmpistack.c','''stacks rsf files of the same dimensionality using mpi ''')
sfmpistack.par('mode',rsf.doc.rsfpar('int','0','','''operation for stack'''))
sfmpistack.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfmpistack.par('seq',rsf.doc.rsfpar('bool','n','','''not sequentially ordered files'''))
sfmpistack.par('nf',rsf.doc.rsfpar('int','','','''number of files to stack '''))
sfmpistack.par('jf',rsf.doc.rsfpar('int','1','','''delta between files '''))
sfmpistack.par('of',rsf.doc.rsfpar('int','0','','''origin of files'''))
sfmpistack.par('shots',rsf.doc.rsfpar('string ',desc=''''''))
sfmpistack.par('prefix',rsf.doc.rsfpar('string ',desc='''printf like prefix '''))
sfmpistack.par('prefix',rsf.doc.rsfpar('string ',desc='''printf like prefix (printf like prefix)'''))
sfmpistack.par('oname',rsf.doc.rsfpar('string ',desc='''name of output file '''))
sfmpistack.version('2.1-git')
sfmpistack.synopsis('''sfmpistack mode=0 verb=n seq=n nf= jf=1 of=0 shots= prefix= oname=''','''
Mode specifies whether to add, multiply, divide or subtract.

mode=0 - add
mode=1 - multiply

If useprefix is set, then:

assume that files are commonly named sequentially, e.g.:

File001.rsf
File002.rsf
File003.rsf ...
FileN.rsf

Such that all files can be represented as a prefix, which 
is a printf like statement that will be evaluated for all
files to be included in a range.

For the above example the prefix would be:

prefix="File%03d.rsf" 

The nf, jf, and of parameters specify a range of numbers to evaluate the 
prefix for, giving the program filenames to be used for summing
together.  For example:  

nf=10,of=0,jf=1 --> (0,1,2,3,4,5,6,7,8,9,10)
nf=10,of=5,jf=2 --> (5,7,9,11,13,15,17,19,21,23)

If there are more files than processes, then this program will subdivide
the files onto various processes, and run multiple rounds until
everything is done.

This program does not care about dimensionality!  It treats every file
as a 1D array and writes out a 1D array, and then modifies the header
to match the input file size.  

''')
rsf.doc.progs['sfmpistack']=sfmpistack

sfbigmpistack = rsf.doc.rsfprog('sfbigmpistack','user/cwp/Mbigmpistack.c','''remap and stacks rsf files using mpi ''')
sfbigmpistack.par('nx',rsf.doc.rsfpar('int','','','''origin of files'''))
sfbigmpistack.par('ny',rsf.doc.rsfpar('int','','','''origin of files'''))
sfbigmpistack.par('nz',rsf.doc.rsfpar('int','','','''origin of files'''))
sfbigmpistack.par('debug',rsf.doc.rsfpar('bool','n','',''''''))
sfbigmpistack.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfbigmpistack.par('dx',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('dy',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('dz',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('oz',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('oy',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('ox',rsf.doc.rsfpar('float','','',''''''))
sfbigmpistack.par('nf',rsf.doc.rsfpar('int','','','''number of files to stack '''))
sfbigmpistack.par('jf',rsf.doc.rsfpar('int','','','''delta between files '''))
sfbigmpistack.par('of',rsf.doc.rsfpar('int','','','''origin of files'''))
sfbigmpistack.par('prefix',rsf.doc.rsfpar('string ',desc='''printf like prefix '''))
sfbigmpistack.par('shots',rsf.doc.rsfpar('string ',desc='''name of shot file '''))
sfbigmpistack.par('oname',rsf.doc.rsfpar('string ',desc='''name of output file '''))
sfbigmpistack.version('2.1-git')
sfbigmpistack.synopsis('''sfbigmpistack nx= ny= nz= debug=n verb=n dx= dy= dz= oz= oy= ox= nf= jf= of= prefix= shots= oname=''','''
Assumes that files are commonly named sequentially, e.g.:

File001.rsf
File002.rsf
File003.rsf ...
FileN.rsf

Such that all files can be represented as a prefix, which 
is a printf like statement that will be evaluated for all
files to be included in a range.

For the above example the prefix would be:

prefix="File%03d.rsf" 

The nf, jf, and of parameters specify a range of numbers to evaluate the 
prefix for, giving the program filenames to be used for summing
together.  For example:  

nf=10,of=0,jf=1 --> (0,1,2,3,4,5,6,7,8,9,10)
nf=10,of=5,jf=2 --> (5,7,9,11,13,15,17,19,21,23)

If there are more files than processes, then this program will subdivide
the files onto various processes, and run multiple rounds until
everything is done.

These must be 3D arrays (or 2D ,but with three dimensions), arrays must be
X-Y-Z
a1-a2-a3
''')
rsf.doc.progs['sfbigmpistack']=sfbigmpistack

