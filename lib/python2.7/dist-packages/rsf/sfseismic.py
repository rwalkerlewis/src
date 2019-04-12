import rsf.doc

sfaastack = rsf.doc.rsfprog('sfaastack','system/seismic/Maastack.c','''Stack with antialiasing ''')
sfaastack.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfaastack.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag '''))
sfaastack.par('n2',rsf.doc.rsfpar('int','15','',''''''))
sfaastack.par('n2',rsf.doc.rsfpar('int','1','',''''''))
sfaastack.par('vel',rsf.doc.rsfpar('float','1.5','','''velocity '''))
sfaastack.par('antialias',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfaastack.par('box',rsf.doc.rsfpar('bool','n','','''box antialiasing '''))
sfaastack.version('2.1-git')
sfaastack.synopsis('''sfaastack < inp.rsf > out.rsf adj=n inv=n n2=15 n2=1 vel=1.5 antialias=1. box=n''','''''')
rsf.doc.progs['sfaastack']=sfaastack

sfagmig = rsf.doc.rsfprog('sfagmig','system/seismic/Magmig.c','''Angle-gather constant-velocity time migration. ''')
sfagmig.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfagmig.par('ng',rsf.doc.rsfpar('int','','','''number of reflection angles '''))
sfagmig.par('dg',rsf.doc.rsfpar('float','','','''reflection angle sampling '''))
sfagmig.par('g0',rsf.doc.rsfpar('float','','','''reflection angle origin '''))
sfagmig.par('na',rsf.doc.rsfpar('int','nx','','''number of dip angles '''))
sfagmig.par('a',rsf.doc.rsfpar('float','80.','','''maximum dip angle '''))
sfagmig.version('2.1-git')
sfagmig.synopsis('''sfagmig < in.rsf > out.rsf vel= ng= dg= g0= na=nx a=80.''','''''')
rsf.doc.progs['sfagmig']=sfagmig

sfai2refl = rsf.doc.rsfprog('sfai2refl','system/seismic/Mai2refl.c','''Convert acoustic impedance to reflectivity. ''')
sfai2refl.version('2.1-git')
sfai2refl.synopsis('''sfai2refl < ai.rsf > mod.rsf''','''
August 2013 program of the month:
http://www.ahay.org/blog/2013/08/02/program-of-the-month-sfai2refl/
''')
rsf.doc.progs['sfai2refl']=sfai2refl

sfavo = rsf.doc.rsfprog('sfavo','system/seismic/Mavo.c','''Compute intercept and gradient by least squares. ''')
sfavo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfavo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfavo.version('2.1-git')
sfavo.synopsis('''sfavo < cmp.rsf > avo.rsf offset=offset.rsf half=y''','''''')
rsf.doc.progs['sfavo']=sfavo

sfbeamspray = rsf.doc.rsfprog('sfbeamspray','system/seismic/Mbeamspray.c','''2-D beam spraying. ''')
sfbeamspray.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbeamspray.par('cur',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbeamspray.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfbeamspray.par('eps',rsf.doc.rsfpar('float','1.0','','''experimental '''))
sfbeamspray.version('2.1-git')
sfbeamspray.synopsis('''sfbeamspray < in.rsf dip=dip.rsf cur=cur.rsf > out.rsf rect=3 eps=1.0''','''''')
rsf.doc.progs['sfbeamspray']=sfbeamspray

sfcascade = rsf.doc.rsfprog('sfcascade','system/seismic/Mcascade.c','''Velocity partitioning for cascaded migrations. ''')
sfcascade.par('ntcut',rsf.doc.rsfpar('ints','','',''' [ncut]'''))
sfcascade.par('tcut',rsf.doc.rsfpar('floats','','','''time cuts  [ncut]'''))
sfcascade.par('ncut',rsf.doc.rsfpar('int','1','','''number of cuts '''))
sfcascade.version('2.1-git')
sfcascade.synopsis('''sfcascade < in.rsf > out.rsf ntcut= tcut= ncut=1''','''''')
rsf.doc.progs['sfcascade']=sfcascade

sfc2r = rsf.doc.rsfprog('sfc2r','system/seismic/Mc2r.c','''Cartesian-Coordinates to Riemannian-Coordinates interpolation ''')
sfc2r.par('rays',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfc2r.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfc2r.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfc2r.par('linear',rsf.doc.rsfpar('bool','y','',''''''))
sfc2r.par('a2n',rsf.doc.rsfpar('int','1','',''''''))
sfc2r.par('a2o',rsf.doc.rsfpar('float','0.','',''''''))
sfc2r.par('a2d',rsf.doc.rsfpar('float','1.','',''''''))
sfc2r.par('a1n',rsf.doc.rsfpar('int','1','',''''''))
sfc2r.par('a1o',rsf.doc.rsfpar('float','0.','',''''''))
sfc2r.par('a1d',rsf.doc.rsfpar('float','1.','',''''''))
sfc2r.version('2.1-git')
sfc2r.synopsis('''sfc2r < Fi.rsf rays=Fr.rsf > Fo.rsf verb=n adj=n linear=y a2n=1 a2o=0. a2d=1. a1n=1 a1o=0. a1d=1.''','''''')
rsf.doc.progs['sfc2r']=sfc2r

sfcell2 = rsf.doc.rsfprog('sfcell2','system/seismic/Mcell2.c','''Second-order cell ray tracing with locally parabolic rays.''')
sfcell2.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcell2.par('anglefile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcell2.par('vel',rsf.doc.rsfpar('bool','y','','''If y, the input is velocity; if n, slowness '''))
sfcell2.par('order',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sfcell2.par('lsint',rsf.doc.rsfpar('bool','n','','''if use least-squares interpolation '''))
sfcell2.par('nt',rsf.doc.rsfpar('int','nx*nz','','''number of time steps '''))
sfcell2.par('nr',rsf.doc.rsfpar('int','','','''Number of angles (if anglefile is not specified) '''))
sfcell2.par('a0',rsf.doc.rsfpar('float','0.','','''First angle in degrees (if anglefile is not specified) '''))
sfcell2.par('amax',rsf.doc.rsfpar('float','360.','','''Maximum angle in degrees (if anglefile is not specified) '''))
sfcell2.par('traj',rsf.doc.rsfpar('string ',desc=''''''))
sfcell2.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfcell2.par('anglefile',rsf.doc.rsfpar('string ',desc='''file with initial angles (auxiliary input file name)'''))
sfcell2.version('2.1-git')
sfcell2.synopsis('''sfcell2 < vel.rsf > time.rsf shotfile=shots.rsf anglefile=angles.rsf vel=y order=4 lsint=n nt=nx*nz nr= a0=0. amax=360. traj= > rays.rsf''','''Rays and wavefronts can be displayed with sfplotrays.
''')
rsf.doc.progs['sfcell2']=sfcell2

sfcell3 = rsf.doc.rsfprog('sfcell3','system/seismic/Mcell3.c','''Second-order cell ray tracing with locally parabolic rays in 3-D.''')
sfcell3.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcell3.par('anglefile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcell3.par('vel',rsf.doc.rsfpar('bool','y','','''If y, the input is velocity; if n, slowness '''))
sfcell3.par('order',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sfcell3.par('nt',rsf.doc.rsfpar('int','nx*nz','','''number of time steps '''))
sfcell3.par('na',rsf.doc.rsfpar('int','','','''Number of azimuths (if anglefile is not specified) '''))
sfcell3.par('nb',rsf.doc.rsfpar('int','','','''Number of inclinations (if anglefile is not specified) '''))
sfcell3.par('a0',rsf.doc.rsfpar('float','0.','','''First azimuth angle in degrees (if anglefile is not specified) '''))
sfcell3.par('amax',rsf.doc.rsfpar('float','360.','','''Maximum azimuth angle in degrees (if anglefile is not specified) '''))
sfcell3.par('b0',rsf.doc.rsfpar('float','0.','','''First inclination angle in degrees (if anglefile is not specified) '''))
sfcell3.par('bmax',rsf.doc.rsfpar('float','180.','','''Maximum inclination angle in degrees (if anglefile is not specified) '''))
sfcell3.par('traj',rsf.doc.rsfpar('string ',desc=''''''))
sfcell3.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfcell3.par('anglefile',rsf.doc.rsfpar('string ',desc='''file with initial angles (auxiliary input file name)'''))
sfcell3.version('2.1-git')
sfcell3.synopsis('''sfcell3 < vel.rsf > time.rsf shotfile=shots.rsf anglefile=angles.rsf vel=y order=4 nt=nx*nz na= nb= a0=0. amax=360. b0=0. bmax=180. traj= > rays.rsf''','''Rays and wavefronts can be displayed with sfplotrays.
''')
rsf.doc.progs['sfcell3']=sfcell3

sfcgscan = rsf.doc.rsfprog('sfcgscan','system/seismic/Mcgscan.c','''Hyperbolic Radon transform with conjugate-directions inversion ''')
sfcgscan.par('error',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcgscan.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcgscan.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfcgscan.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfcgscan.par('miter',rsf.doc.rsfpar('int','2','','''conjugate-direction memory '''))
sfcgscan.par('psun1',rsf.doc.rsfpar('int','1','','''amplitude type for adjoint '''))
sfcgscan.par('psun2',rsf.doc.rsfpar('int','1','','''amplitude type for forward '''))
sfcgscan.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfcgscan.par('s02',rsf.doc.rsfpar('float','0.','','''reference slowness squared (for antialiasing) '''))
sfcgscan.par('ncycle',rsf.doc.rsfpar('int','0','','''number of sharpening cycles '''))
sfcgscan.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfcgscan.par('error',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfcgscan.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfcgscan.version('2.1-git')
sfcgscan.synopsis('''sfcgscan < in.rsf > out.rsf error=err.rsf mask=msk.rsf adj=n niter=0 miter=2 psun1=1 psun2=1 anti=1. s02=0. ncycle=0 perc=50.0''','''''')
rsf.doc.progs['sfcgscan']=sfcgscan

sfcmp2shot = rsf.doc.rsfprog('sfcmp2shot','system/seismic/Mcmp2shot.c','''Convert CMPs to shots for regular 2-D geometry. ''')
sfcmp2shot.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfcmp2shot.version('2.1-git')
sfcmp2shot.synopsis('''sfcmp2shot < in.rsf > out.rsf positive=y''','''''')
rsf.doc.progs['sfcmp2shot']=sfcmp2shot

sfconstfdmig2 = rsf.doc.rsfprog('sfconstfdmig2','system/seismic/Mconstfdmig2.c','''2-D implicit finite-difference migration in constant velocity. ''')
sfconstfdmig2.par('movie',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconstfdmig2.par('nz',rsf.doc.rsfpar('int','2*(nw-1)','','''vertical time samples '''))
sfconstfdmig2.par('dz',rsf.doc.rsfpar('float','1./(nz*dw)','','''vertical time sampling '''))
sfconstfdmig2.par('vel',rsf.doc.rsfpar('float','','','''constant velocity '''))
sfconstfdmig2.par('hi',rsf.doc.rsfpar('bool','y','','''if y, use 45-degree; n, 15-degree '''))
sfconstfdmig2.par('sixth',rsf.doc.rsfpar('float','1./12','','''one-sixth trick '''))
sfconstfdmig2.par('movie',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfconstfdmig2.version('2.1-git')
sfconstfdmig2.synopsis('''sfconstfdmig2 < data.rsf > imag.rsf movie=movie.rsf nz=2*(nw-1) dz=1./(nz*dw) vel= hi=y sixth=1./12''','''''')
rsf.doc.progs['sfconstfdmig2']=sfconstfdmig2

sfcos2ang = rsf.doc.rsfprog('sfcos2ang','system/seismic/Mcos2ang.c','''Inverse cos to angle transformation ''')
sfcos2ang.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcos2ang.par('na',rsf.doc.rsfpar('int','nt','','''number of angles'''))
sfcos2ang.par('da',rsf.doc.rsfpar('float','90/(nt-1)','','''angle sampling '''))
sfcos2ang.par('a0',rsf.doc.rsfpar('float','0.','','''angle origin '''))
sfcos2ang.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sfcos2ang.par('top',rsf.doc.rsfpar('bool','n','','''velocity scaling option '''))
sfcos2ang.version('2.1-git')
sfcos2ang.synopsis('''sfcos2ang < Fstk.rsf > Fang.rsf velocity=velocity.rsf na=nt da=90/(nt-1) a0=0. extend=4 top=n''','''''')
rsf.doc.progs['sfcos2ang']=sfcos2ang

sfdepth2time = rsf.doc.rsfprog('sfdepth2time','system/seismic/Mdepth2time.c','''Conversion from depth to time in a V(z) medium.''')
sfdepth2time.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdepth2time.par('nt',rsf.doc.rsfpar('int','','','''Number of points in time (default is n1) '''))
sfdepth2time.par('dt',rsf.doc.rsfpar('float','','','''Time sampling (default is d1) '''))
sfdepth2time.par('t0',rsf.doc.rsfpar('float','','','''Time origin (default is 0) '''))
sfdepth2time.par('slow',rsf.doc.rsfpar('bool','n','','''y: slowness, n: velocity '''))
sfdepth2time.par('eps',rsf.doc.rsfpar('float','0.01','','''smoothness parameter '''))
sfdepth2time.version('2.1-git')
sfdepth2time.synopsis('''sfdepth2time < in.rsf velocity=velocity.rsf > out.rsf nt= dt= t0= slow=n eps=0.01''','''
Transforms function of z to function of

tau = Integral[2/v[x,n],{n,0,z}]
''')
rsf.doc.progs['sfdepth2time']=sfdepth2time

sfdiffoc = rsf.doc.rsfprog('sfdiffoc','system/seismic/Mdiffoc.c','''Diffraction focusing test. ''')
sfdiffoc.par('v0',rsf.doc.rsfpar('float','SF_EPS','','''initial velocity '''))
sfdiffoc.par('v',rsf.doc.rsfpar('float','','','''final velocity '''))
sfdiffoc.par('pad',rsf.doc.rsfpar('int','nt','','''padding for stretch '''))
sfdiffoc.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfdiffoc.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfdiffoc.version('2.1-git')
sfdiffoc.synopsis('''sfdiffoc < inp.rsf > out.rsf v0=SF_EPS v= pad=nt pad2=2*kiss_fft_next_fast_size((n2+1)/2) extend=4''','''''')
rsf.doc.progs['sfdiffoc']=sfdiffoc

sfdiffraction = rsf.doc.rsfprog('sfdiffraction','system/seismic/Mdiffraction.c','''Generate diffractions in zero-offset data. ''')
sfdiffraction.par('w2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('w12',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('spikes',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffraction.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfdiffraction.version('2.1-git')
sfdiffraction.synopsis('''sfdiffraction < w1.rsf w2=w2.rsf w12=w12.rsf spikes=spikes.rsf > data.rsf freq=0.2/dt''','''''')
rsf.doc.progs['sfdiffraction']=sfdiffraction

sfdimag = rsf.doc.rsfprog('sfdimag','system/seismic/Mdimag.c','''Diffraction imaging in the plane-wave domain. ''')
sfdimag.par('semblance',rsf.doc.rsfpar('bool','n','','''if y, compute semblance; if n, stack '''))
sfdimag.par('nb',rsf.doc.rsfpar('int','2','','''semblance averaging '''))
sfdimag.par('v0',rsf.doc.rsfpar('float','','',''''''))
sfdimag.par('dv',rsf.doc.rsfpar('float','','',''''''))
sfdimag.par('nv',rsf.doc.rsfpar('int','','',''''''))
sfdimag.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfdimag.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfdimag.par('str',rsf.doc.rsfpar('float','0.','','''maximum stretch allowed '''))
sfdimag.par('x0',rsf.doc.rsfpar('float','','',''''''))
sfdimag.version('2.1-git')
sfdimag.synopsis('''sfdimag < cmp.rsf > scan.rsf semblance=n nb=2 v0= dv= nv= extend=4 mute=12 str=0. x0=''','''''')
rsf.doc.progs['sfdimag']=sfdimag

sfdmo = rsf.doc.rsfprog('sfdmo','system/seismic/Mdmo.c','''Kirchhoff DMO with antialiasing by reparameterization. ''')
sfdmo.par('mint',rsf.doc.rsfpar('int','2','','''starting time sample '''))
sfdmo.par('n',rsf.doc.rsfpar('int','32','','''number of offset samples '''))
sfdmo.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag '''))
sfdmo.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfdmo.par('type',rsf.doc.rsfpar('int','1','','''type of amplitude (0,1,2,3) '''))
sfdmo.par('h',rsf.doc.rsfpar('float','','',''''''))
sfdmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the third axis is half-offset instead of full offset '''))
sfdmo.par('velhalf',rsf.doc.rsfpar('float','0.75','','''half-velocity '''))
sfdmo.version('2.1-git')
sfdmo.synopsis('''sfdmo < in.rsf > out.rsf mint=2 n=32 adj=y inv=n type=1 h= half=y velhalf=0.75''','''''')
rsf.doc.progs['sfdmo']=sfdmo

sfdsr = rsf.doc.rsfprog('sfdsr','system/seismic/Mdsr.c','''Prestack 2-D VTI v(z) modeling/migration by DSR with angle gathers. ''')
sfdsr.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsr.par('velz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsr.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsr.par('inv',rsf.doc.rsfpar('bool','n','','''If y, modeling; If n, migration '''))
sfdsr.par('eps',rsf.doc.rsfpar('float','0.01','','''Stabilization parameter '''))
sfdsr.par('depth',rsf.doc.rsfpar('bool','n','','''if true, depth migration '''))
sfdsr.par('na',rsf.doc.rsfpar('int','1','','''number of angles '''))
sfdsr.par('da',rsf.doc.rsfpar('float','90.','','''angle sampling (in degrees) '''))
sfdsr.par('nt',rsf.doc.rsfpar('int','','','''Length of time axis (for modeling) '''))
sfdsr.par('dt',rsf.doc.rsfpar('float','','','''Sampling of time axis (for modeling) '''))
sfdsr.par('t0',rsf.doc.rsfpar('float','0.','',''''''))
sfdsr.par('nh',rsf.doc.rsfpar('int','','','''Number of offsets (for modeling) '''))
sfdsr.par('dh',rsf.doc.rsfpar('float','','','''Offset sampling (for modeling) '''))
sfdsr.par('nz',rsf.doc.rsfpar('int','nt','','''Length of depth axis (for migration, if no velocity file) '''))
sfdsr.par('dz',rsf.doc.rsfpar('float','dt','','''Sampling of depth axis (for migration, if no velocity file) '''))
sfdsr.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (if no velocity file) '''))
sfdsr.par('vz',rsf.doc.rsfpar('float','v0','','''Constant vertical velocity (if no velocity file) '''))
sfdsr.par('n',rsf.doc.rsfpar('float','0.0','','''Constant eta (if no velocity file) '''))
sfdsr.par('nw',rsf.doc.rsfpar('int','nt2/2+1','','''Maximum number of frequencies '''))
sfdsr.par('velocity',rsf.doc.rsfpar('string ',desc='''file with velocity (auxiliary input file name)'''))
sfdsr.par('velocity',rsf.doc.rsfpar('string ',desc='''file with velocity (file with velocity (auxiliary input file name))'''))
sfdsr.par('velz',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsr.par('eta',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdsr.par('rule',rsf.doc.rsfpar('string ',desc='''phase-shift interpolation rule (simple, midpoint, linear, anisotropic, dti) '''))
sfdsr.par('arule',rsf.doc.rsfpar('string ',desc='''angle gather rule '''))
sfdsr.version('2.1-git')
sfdsr.synopsis('''sfdsr < in.rsf > out.rsf velocity=vel.rsf velz=velz.rsf eta=eta.rsf inv=n eps=0.01 depth=n na=1 da=90. nt= dt= t0=0. nh= dh= nz=nt dz=dt vel= vz=v0 n=0.0 nw=nt2/2+1 rule= arule=''','''''')
rsf.doc.progs['sfdsr']=sfdsr

sfdsr2 = rsf.doc.rsfprog('sfdsr2','system/seismic/Mdsr2.c','''2-D prestack modeling/migration with split-step DSR. ''')
sfdsr2.par('slowness',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdsr2.par('inv',rsf.doc.rsfpar('bool','n','','''If y, modeling; if n, migration '''))
sfdsr2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdsr2.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfdsr2.par('nt',rsf.doc.rsfpar('int','1','','''taper size '''))
sfdsr2.par('nr',rsf.doc.rsfpar('int','1','','''maximum number of references '''))
sfdsr2.par('dt',rsf.doc.rsfpar('float','0.004','','''time error '''))
sfdsr2.par('npad',rsf.doc.rsfpar('int','0','','''padding on offset wavenumber '''))
sfdsr2.par('nw',rsf.doc.rsfpar('int','','','''Length of frequency axis (for modeling) '''))
sfdsr2.par('dw',rsf.doc.rsfpar('float','','','''Frequency sampling (for modeling) '''))
sfdsr2.par('w0',rsf.doc.rsfpar('float','0.','','''Frequency origin (for modeling) '''))
sfdsr2.version('2.1-git')
sfdsr2.synopsis('''sfdsr2 < in.rsf > out.rsf slowness=vel.rsf inv=n verb=n eps=0.01 nt=1 nr=1 dt=0.004 npad=0 nw= dw= w0=0.''','''''')
rsf.doc.progs['sfdsr2']=sfdsr2

sfenvelope = rsf.doc.rsfprog('sfenvelope','system/seismic/Menvelope.c','''None''')
sfenvelope.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfenvelope.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfenvelope.par('hilb',rsf.doc.rsfpar('bool','n','','''if y, compute Hilbert transform '''))
sfenvelope.par('phase',rsf.doc.rsfpar('float','90.','','''phase shift (in degrees) to use with hilb=y '''))
sfenvelope.version('2.1-git')
sfenvelope.synopsis('''sfenvelope < in.rsf > out.rsf order=100 ref=1. hilb=n phase=90.''','''''')
rsf.doc.progs['sfenvelope']=sfenvelope

sffincon = rsf.doc.rsfprog('sffincon','system/seismic/Mfincon.c','''Offset continuation by finite differences ''')
sffincon.par('nh',rsf.doc.rsfpar('int','','','''Number of steps in offset '''))
sffincon.par('dh',rsf.doc.rsfpar('float','','','''Offset step size '''))
sffincon.par('h0',rsf.doc.rsfpar('float','','','''Initial offset '''))
sffincon.par('all',rsf.doc.rsfpar('bool','n','','''if y, output all offsets '''))
sffincon.version('2.1-git')
sffincon.synopsis('''sffincon < input.rsf > output.rsf nh= dh= h0= all=n''','''''')
rsf.doc.progs['sffincon']=sffincon

sffindmo = rsf.doc.rsfprog('sffindmo','system/seismic/Mfindmo.c','''DMO without stacking by finite-difference offset continuation. ''')
sffindmo.version('2.1-git')
sffindmo.synopsis('''sffindmo < cmp.rsf > stk.rsf''','''''')
rsf.doc.progs['sffindmo']=sffindmo

sffinstack = rsf.doc.rsfprog('sffinstack','system/seismic/Mfinstack.c','''DMO and stack by finite-difference offset continuation. ''')
sffinstack.version('2.1-git')
sffinstack.synopsis('''sffinstack < cmp.rsf > stk.rsf''','''''')
rsf.doc.progs['sffinstack']=sffinstack

sffkamo = rsf.doc.rsfprog('sffkamo','system/seismic/Mfkamo.c','''Computes Azimuth Move-Out (AMO) operator in the f-k log-stretch domain ''')
sffkamo.par('h1',rsf.doc.rsfpar('float','','','''input offset '''))
sffkamo.par('h2',rsf.doc.rsfpar('float','','','''output offset '''))
sffkamo.par('f1',rsf.doc.rsfpar('float','','','''input azimuth in degrees '''))
sffkamo.par('f2',rsf.doc.rsfpar('float','','','''output azimuth in degrees '''))
sffkamo.par('maxe',rsf.doc.rsfpar('float','10.','','''stability constraint '''))
sffkamo.version('2.1-git')
sffkamo.synopsis('''sffkamo < in.rsf > out.rsf h1= h2= f1= f2= maxe=10.''','''''')
rsf.doc.progs['sffkamo']=sffkamo

sffkdmo = rsf.doc.rsfprog('sffkdmo','system/seismic/Mfkdmo.c','''Offset continuation by log-stretch F-K operator. ''')
sffkdmo.par('h',rsf.doc.rsfpar('float','','','''final offset '''))
sffkdmo.par('nh',rsf.doc.rsfpar('int','1','','''number of offset steps '''))
sffkdmo.par('h0',rsf.doc.rsfpar('float','0.','','''initial offset '''))
sffkdmo.version('2.1-git')
sffkdmo.synopsis('''sffkdmo < in.rsf > out.rsf h= nh=1 h0=0.''','''''')
rsf.doc.progs['sffkdmo']=sffkdmo

sffkgdmo = rsf.doc.rsfprog('sffkgdmo','system/seismic/Mfkgdmo.c','''FK-domain Gardner's DMO for regularly sampled 2-D data ''')
sffkgdmo.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sffkgdmo.par('shot',rsf.doc.rsfpar('bool','n','','''if shot gathers instead of midpoint gathers '''))
sffkgdmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sffkgdmo.par('nb',rsf.doc.rsfpar('int','85','','''number of angles '''))
sffkgdmo.par('db',rsf.doc.rsfpar('float','1','','''angle increment '''))
sffkgdmo.par('xi',rsf.doc.rsfpar('float','1','','''continuation paremeter '''))
sffkgdmo.version('2.1-git')
sffkgdmo.synopsis('''sffkgdmo < in.rsf > out.rsf inv=y shot=n eps=0.01 nb=85 db=1 xi=1''','''
The input/ouput is (offset,logstretch frequency, midpoint/shot wavenumber).
''')
rsf.doc.progs['sffkgdmo']=sffkgdmo

sffold = rsf.doc.rsfprog('sffold','system/seismic/Mfold.c','''Make a seismic foldplot/stacking chart. ''')
sffold.par('verbose',rsf.doc.rsfpar('int','1','','''0 terse, 1 informative, 2 chatty, 3 debug '''))
sffold.par('o1',rsf.doc.rsfpar('float','','','''Minimum label1 - usually min offset '''))
sffold.par('o2',rsf.doc.rsfpar('float','','','''Minimum label2 - usually min xline  '''))
sffold.par('o3',rsf.doc.rsfpar('float','','','''Minimum label3 - usually min iline '''))
sffold.par('n1',rsf.doc.rsfpar('int','','','''Number label1 - usually number offset '''))
sffold.par('n2',rsf.doc.rsfpar('int','','','''Number label2 - usually number xline '''))
sffold.par('n3',rsf.doc.rsfpar('int','','','''Number label3 - usually number iline '''))
sffold.par('d1',rsf.doc.rsfpar('float','','','''Delta label1 - usually delta offset  '''))
sffold.par('d2',rsf.doc.rsfpar('float','','','''Delta label2 - usually delta xline  '''))
sffold.par('d3',rsf.doc.rsfpar('float','','','''Delta label3 - usually delta iline  '''))
sffold.par('label1',rsf.doc.rsfpar('string ',desc='''header for axis1 - usually offset '''))
sffold.par('label2',rsf.doc.rsfpar('string ',desc='''header for axis2 - usually xline or cdp  '''))
sffold.par('label3',rsf.doc.rsfpar('string ',desc='''header for axis3 - usually iline  '''))
sffold.version('2.1-git')
sffold.synopsis('''sffold < in.rsf > out.rsf verbose=1 o1= o2= o3= n1= n2= n3= d1= d2= d3= label1= label2= label3=''','''
This is a general 3D histogram program implemented to create foldplot or
stacking charts on a 3d project from trace headers.  Axis1, 2 and 3 
define the bins for the output fold map.  These are usually 
(offset,xline,iline), but you might want to compute some other
histogram.  This can be done by selecting other segy headers using 
label1, 2 and 3.

See also fold= option in sfbin for creating 2D histograms.

EXAMPLES:

To make a stacking chart movie showing fold(xline,offset) for each 
iline from a 3D segyfile:

sfsegyread tfile=tteapot.rsf hfile=teapot.asc bfile=teapot.bin \\
tape=npr3_field.sgy > teapot.rsf

# read the tfile, which contains the segy trace headers
< teapot_hdr.rsf sffold verbose=1        \\
o1=0 n1=96  d1=200 label1=offset \\
o2=1 n2=188 d2=1   label2=xline  \\
o3=1 n3=345 d3=1   label3=iline  \\
>foldplot.rsf
<foldplot.rsf sfgrey title=foldplot pclip=100 \\
| sfpen 

# transpose this data to plot foldmaps for each offset window:

< foldplot.rsf sftransp plane=13          \\
| sftransp plane=12                       \\
| sfgrey title=foldplot_off gainpanel=all \\
| sfpen

''')
rsf.doc.progs['sffold']=sffold

sffourvc = rsf.doc.rsfprog('sffourvc','system/seismic/Mfourvc.c','''Prestack velocity continuation. ''')
sffourvc.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffourvc.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sffourvc.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sffourvc.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourvc.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sffourvc.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sffourvc.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sffourvc.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sffourvc.version('2.1-git')
sffourvc.synopsis('''sffourvc < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=n nv= dv= extend=4 v0=''','''''')
rsf.doc.progs['sffourvc']=sffourvc

sffourvc0 = rsf.doc.rsfprog('sffourvc0','system/seismic/Mfourvc0.c','''Velocity continuation after NMO. ''')
sffourvc0.par('eps',rsf.doc.rsfpar('float','0.01','',''''''))
sffourvc0.par('pad',rsf.doc.rsfpar('int','n1','',''''''))
sffourvc0.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','',''''''))
sffourvc0.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourvc0.par('nv',rsf.doc.rsfpar('int','','',''''''))
sffourvc0.par('dv',rsf.doc.rsfpar('float','','',''''''))
sffourvc0.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sffourvc0.version('2.1-git')
sffourvc0.synopsis('''sffourvc0 < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=n nv= dv= extend=4''','''''')
rsf.doc.progs['sffourvc0']=sffourvc0

sffourvc2 = rsf.doc.rsfprog('sffourvc2','system/seismic/Mfourvc2.c','''Velocity continuation with semblance computation. ''')
sffourvc2.par('nb',rsf.doc.rsfpar('int','2','',''''''))
sffourvc2.par('eps',rsf.doc.rsfpar('float','0.01','',''''''))
sffourvc2.par('pad',rsf.doc.rsfpar('int','n1','',''''''))
sffourvc2.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','',''''''))
sffourvc2.par('nv',rsf.doc.rsfpar('int','','',''''''))
sffourvc2.par('dv',rsf.doc.rsfpar('float','','',''''''))
sffourvc2.par('semblance',rsf.doc.rsfpar('bool','y','','''if y, compute semblance; if n, stack '''))
sffourvc2.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sffourvc2.version('2.1-git')
sffourvc2.synopsis('''sffourvc2 < in.rsf > out.rsf nb=2 eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) nv= dv= semblance=y extend=4''','''''')
rsf.doc.progs['sffourvc2']=sffourvc2

sffowler = rsf.doc.rsfprog('sffowler','system/seismic/Mfowler.c','''2-D velocity-domain imaging (Fowler DMO + Stolt migration).''')
sffowler.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sffowler.version('2.1-git')
sffowler.synopsis('''sffowler < inp.rsf > out.rsf eps=0.01''','''
Input: 2-D cosft of constant-velocity stacks (v,w,k).
''')
rsf.doc.progs['sffowler']=sffowler

sffowler1 = rsf.doc.rsfprog('sffowler1','system/seismic/Mfowler1.c','''2-D velocity-domain DMO (Fowler DMO).''')
sffowler1.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sffowler1.version('2.1-git')
sffowler1.synopsis('''sffowler1 < inp.rsf > out.rsf eps=0.01''','''
Input: 2-D cosft of constant-velocity stacks (v,w,k).
''')
rsf.doc.progs['sffowler1']=sffowler1

sffowler2 = rsf.doc.rsfprog('sffowler2','system/seismic/Mfowler2.c','''2-D ensemble of Stolt migrations.''')
sffowler2.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sffowler2.version('2.1-git')
sffowler2.synopsis('''sffowler2 < inp.rsf > out.rsf eps=0.01''','''
Input: 2-D cosft of constant-velocity stacks (w,v,k).
''')
rsf.doc.progs['sffowler2']=sffowler2

sffreqint = rsf.doc.rsfprog('sffreqint','system/seismic/Mfreqint.c','''1-D data regularization using freqlet transform ''')
sffreqint.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreqint.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreqint.par('n1',rsf.doc.rsfpar('int','','','''output samples '''))
sffreqint.par('d1',rsf.doc.rsfpar('float','','','''output sampling '''))
sffreqint.par('o1',rsf.doc.rsfpar('float','','','''output origin '''))
sffreqint.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations for inversion '''))
sffreqint.par('ncycle',rsf.doc.rsfpar('int','1','','''number of IRLS iterations '''))
sffreqint.par('eps',rsf.doc.rsfpar('float','1.0','','''regularization parameter '''))
sffreqint.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sffreqint.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sffreqint.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sffreqint.version('2.1-git')
sffreqint.synopsis('''sffreqint < in.rsf > out.rsf freq=w.rsf coord=coord.rsf n1= d1= o1= niter=10 ncycle=1 eps=1.0 inv=n perc=50.0 type=''','''''')
rsf.doc.progs['sffreqint']=sffreqint

sffreqlet = rsf.doc.rsfprog('sffreqlet','system/seismic/Mfreqlet.c','''1-D seislet frame ''')
sffreqlet.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreqlet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffreqlet.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffreqlet.par('decomp',rsf.doc.rsfpar('bool','n','','''do decomposition '''))
sffreqlet.par('ncycle',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sffreqlet.par('niter',rsf.doc.rsfpar('int','1','','''number of Bregman iterations '''))
sffreqlet.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sffreqlet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sffreqlet.version('2.1-git')
sffreqlet.synopsis('''sffreqlet < in.rsf > out.rsf freq=w.rsf inv=n verb=y decomp=n ncycle=0 niter=1 perc=50.0 type=''','''''')
rsf.doc.progs['sffreqlet']=sffreqlet

sfgazdag = rsf.doc.rsfprog('sfgazdag','system/seismic/Mgazdag.c','''Post-stack 2-D/3-D v(z) time modeling/migration with Gazdag phase-shift. ''')
sfgazdag.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgazdag.par('velz',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgazdag.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgazdag.par('inv',rsf.doc.rsfpar('bool','n','','''if y, modeling; if n, migration '''))
sfgazdag.par('eps',rsf.doc.rsfpar('float','0.01','','''stabilization parameter '''))
sfgazdag.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfgazdag.par('depth',rsf.doc.rsfpar('bool','n','','''if true, depth migration '''))
sfgazdag.par('nt',rsf.doc.rsfpar('int','','','''Length of time axis (for modeling) '''))
sfgazdag.par('dt',rsf.doc.rsfpar('float','','','''Sampling of time axis (for modeling) '''))
sfgazdag.par('nz',rsf.doc.rsfpar('int','','','''Length of depth axis (for migration, if no velocity file) '''))
sfgazdag.par('dz',rsf.doc.rsfpar('float','','','''Sampling of depth axis (for migration, if no velocity file) '''))
sfgazdag.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (if no velocity file) '''))
sfgazdag.par('vz',rsf.doc.rsfpar('float','v0','','''Constant vertical velocity (if no velocity file) '''))
sfgazdag.par('n',rsf.doc.rsfpar('float','0.0','','''Constant eta (if no velocity file) '''))
sfgazdag.par('pad',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((nt+1)/2)','',''''''))
sfgazdag.par('velocity',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgazdag.par('velz',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgazdag.par('eta',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfgazdag.par('rule',rsf.doc.rsfpar('string ',desc='''phase-shift interpolation rule (simple, midpoint, linear) '''))
sfgazdag.version('2.1-git')
sfgazdag.synopsis('''sfgazdag < in.rsf > out.rsf velocity=vel.rsf velz=velz.rsf eta=eta.rsf inv=n eps=0.01 verb=n depth=n nt= dt= nz= dz= vel= vz=v0 n=0.0 pad=2*kiss_fft_next_fast_size((nt+1)/2) rule=''','''''')
rsf.doc.progs['sfgazdag']=sfgazdag

sfgdmo = rsf.doc.rsfprog('sfgdmo','system/seismic/Mgdmo.c','''Gardner's DMO for regularly sampled 2-D data (slow method) ''')
sfgdmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfgdmo.par('nb',rsf.doc.rsfpar('int','171','','''number of angles '''))
sfgdmo.par('b0',rsf.doc.rsfpar('float','-85','','''first angle '''))
sfgdmo.par('db',rsf.doc.rsfpar('float','1','','''angle increment '''))
sfgdmo.version('2.1-git')
sfgdmo.synopsis('''sfgdmo < in.rsf > out.rsf eps=0.01 nb=171 b0=-85 db=1''','''
The input/ouput is (time,offset,midpoint).
''')
rsf.doc.progs['sfgdmo']=sfgdmo

sfhalfint = rsf.doc.rsfprog('sfhalfint','system/seismic/Mhalfint.c','''Half-order integration or differentiation. ''')
sfhalfint.par('adj',rsf.doc.rsfpar('bool','n','','''If y, apply adjoint '''))
sfhalfint.par('inv',rsf.doc.rsfpar('bool','n','','''If y, do differentiation instead of integration '''))
sfhalfint.par('rho',rsf.doc.rsfpar('float','1.-1./n1','','''Leaky integration constant '''))
sfhalfint.version('2.1-git')
sfhalfint.synopsis('''sfhalfint < in.rsf > out.rsf adj=n inv=n rho=1.-1./n1''','''
December 2012 program of the month:
http://ahay.org/blog/2012/12/23/program-of-the-month-sfhalfint/
''')
rsf.doc.progs['sfhalfint']=sfhalfint

sfheaderattr = rsf.doc.rsfprog('sfheaderattr','system/seismic/Mheaderattr.c','''Display header attributes. ''')
sfheaderattr.par('segy',rsf.doc.rsfpar('bool','y','','''if SEGY headers '''))
sfheaderattr.par('desc',rsf.doc.rsfpar('bool','n','','''if describe keys '''))
sfheaderattr.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheaderattr')
sfheaderattr.version('2.1-git')
sfheaderattr.synopsis('''sfheaderattr < head.rsf segy=y desc=n''','''
Only nonzero values are reported.
''')
rsf.doc.progs['sfheaderattr']=sfheaderattr

sfheadermath = rsf.doc.rsfprog('sfheadermath','system/seismic/Mheadermath.c','''Mathematical operations, possibly on header keys. ''')
sfheadermath.par('segy',rsf.doc.rsfpar('bool','y','','''if SEGY headers '''))
sfheadermath.par('nkey',rsf.doc.rsfpar('int','-1','','''number of key to replace '''))
sfheadermath.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfheadermath.par('key',rsf.doc.rsfpar('string ',desc='''key to replace '''))
sfheadermath.par('output',rsf.doc.rsfpar('string ',desc='''Describes the output in a mathematical notation. '''))
sfheadermath.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfheadermath')
sfheadermath.version('2.1-git')
sfheadermath.synopsis('''sfheadermath < in.rsf > out.rsf segy=y nkey=-1 memsize=sf_memsize() key= output=''','''
Known functions for float data: 
cos,  sin,  tan,  acos,  asin,  atan, 
cosh, sinh, tanh, acosh, asinh, atanh,
exp,  log,  sqrt, abs, erf, erfc, sign

Known functions for int data: sign, abs

See also sfmath.

An addition operation can be performed by sfadd.
''')
rsf.doc.progs['sfheadermath']=sfheadermath

sfhwt2d = rsf.doc.rsfprog('sfhwt2d','system/seismic/Mhwt2d.c','''2-D Huygens wavefront tracing traveltimes ''')
sfhwt2d.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfhwt2d.par('rays',rsf.doc.rsfpar('bool','n','','''velocity file '''))
sfhwt2d.par('xsou',rsf.doc.rsfpar('float','sf_o(ax) + nx*sf_d(ax)/2','',''''''))
sfhwt2d.par('zsou',rsf.doc.rsfpar('float','sf_o(az) + nz*sf_d(az)/2','',''''''))
sfhwt2d.par('nt',rsf.doc.rsfpar('int','100','',''''''))
sfhwt2d.par('ot',rsf.doc.rsfpar('float','0','',''''''))
sfhwt2d.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfhwt2d.par('ng',rsf.doc.rsfpar('int','360','',''''''))
sfhwt2d.par('og',rsf.doc.rsfpar('float','-180','',''''''))
sfhwt2d.par('dg',rsf.doc.rsfpar('float','1','',''''''))
sfhwt2d.version('2.1-git')
sfhwt2d.synopsis('''sfhwt2d < Fv.rsf > Fw.rsf verb=n rays=n xsou=sf_o(ax) + nx*sf_d(ax)/2 zsou=sf_o(az) + nz*sf_d(az)/2 nt=100 ot=0 dt=0.001 ng=360 og=-180 dg=1''','''''')
rsf.doc.progs['sfhwt2d']=sfhwt2d

sfhwtex = rsf.doc.rsfprog('sfhwtex','system/seismic/Mhwtex.c','''Huygens wavefront tracing traveltimes ''')
sfhwtex.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhwtex.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfhwtex.par('wini',rsf.doc.rsfpar('bool','n','','''initialize two wavefronts '''))
sfhwtex.par('nt',rsf.doc.rsfpar('int','100','',''''''))
sfhwtex.par('ot',rsf.doc.rsfpar('float','0','',''''''))
sfhwtex.par('dt',rsf.doc.rsfpar('float','0.001','',''''''))
sfhwtex.version('2.1-git')
sfhwtex.synopsis('''sfhwtex < Fv.rsf sou=Fs.rsf > Fw.rsf verb=n wini=n nt=100 ot=0 dt=0.001''','''''')
rsf.doc.progs['sfhwtex']=sfhwtex

sfinfill = rsf.doc.rsfprog('sfinfill','system/seismic/Minfill.c','''Shot interpolation. ''')
sfinfill.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sfinfill.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfinfill.version('2.1-git')
sfinfill.synopsis('''sfinfill < in.rsf > out.rsf eps=0.1 positive=y''','''''')
rsf.doc.progs['sfinfill']=sfinfill

sfinmo = rsf.doc.rsfprog('sfinmo','system/seismic/Minmo.c','''Inverse normal moveout. ''')
sfinmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfinmo.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfinmo.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfinmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfinmo.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfinmo.version('2.1-git')
sfinmo.synopsis('''sfinmo < cmp.rsf velocity=velocity.rsf > nmod.rsf offset=offset.rsf mask=msk.rsf half=y slowness=n h0=0. eps=0.01''','''''')
rsf.doc.progs['sfinmo']=sfinmo

sfinmo3 = rsf.doc.rsfprog('sfinmo3','system/seismic/Minmo3.c','''3-D Inverse normal moveout.''')
sfinmo3.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfinmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3.version('2.1-git')
sfinmo3.synopsis('''sfinmo3 < cmp.rsf > nmod.rsf velocity=vel.rsf half=y eps=0.01 extend=8''','''
velocity file contains slowness squared with n2=3 (wx,wy,wxy)
''')
rsf.doc.progs['sfinmo3']=sfinmo3

sfinmo3gma = rsf.doc.rsfprog('sfinmo3gma','system/seismic/Minmo3gma.c','''3-D Inverse generalized normal moveout.''')
sfinmo3gma.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3gma.par('half',rsf.doc.rsfpar('bool','n','','''if x,y , the second and third axes are half-offset instead of full offset '''))
sfinmo3gma.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3gma.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3gma.version('2.1-git')
sfinmo3gma.synopsis('''sfinmo3gma < cmp.rsf > nmod.rsf velocity=vel.rsf half=n eps=0.01 extend=8''','''Velocity file contains slowness squared with n2=16 (wx,wxy,wy,A1,A2,A3,A4,A5,B1,B2,B3,C1,C2,C3,C4,C5)
following Sripanich and Fomel (2015).
''')
rsf.doc.progs['sfinmo3gma']=sfinmo3gma

sfintbin = rsf.doc.rsfprog('sfintbin','system/seismic/Mintbin.c','''Data binning by trace sorting. ''')
sfintbin.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfintbin.par('xkey',rsf.doc.rsfpar('int','','','''x key number (if no xk), default is fldr '''))
sfintbin.par('ykey',rsf.doc.rsfpar('int','','','''y key number (if no yk), default is tracf '''))
sfintbin.par('xmin',rsf.doc.rsfpar('int','','','''x minimum '''))
sfintbin.par('xmax',rsf.doc.rsfpar('int','','','''x maximum '''))
sfintbin.par('ymin',rsf.doc.rsfpar('int','','','''y minimum '''))
sfintbin.par('ymax',rsf.doc.rsfpar('int','','','''y maximum '''))
sfintbin.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfintbin.par('xk',rsf.doc.rsfpar('string ',desc='''x key name '''))
sfintbin.par('yk',rsf.doc.rsfpar('string ',desc='''y key name '''))
sfintbin.par('map',rsf.doc.rsfpar('string ',desc='''output map file '''))
sfintbin.par('mask',rsf.doc.rsfpar('string ',desc='''output mask file '''))
sfintbin.version('2.1-git')
sfintbin.synopsis('''sfintbin < in.rsf > out.rsf inv=n xkey= ykey= xmin= xmax= ymin= ymax= head= xk= yk= map= mask=''','''
If inv=n, the input is 2-D (n1 x ntr). The output is 3-D (n1 x n2 x n3), n2 and
n3 correspond to two selected keys from the header file. 

If inv=y, the input is 3-D, and the output is 2-D.

if xkey < 0, the first axis indexes traces in a gather like cdpt.

June 2015 program of the month:
http://ahay.org/blog/2015/06/10/program-of-the-month-sfintbin/
''')
rsf.doc.progs['sfintbin']=sfintbin

sfintbin3 = rsf.doc.rsfprog('sfintbin3','system/seismic/Mintbin3.c','''4-D data binning. ''')
sfintbin3.par('xkey',rsf.doc.rsfpar('int','','','''x key number (if no xk), default is fldr '''))
sfintbin3.par('ykey',rsf.doc.rsfpar('int','','','''y key number (if no yk), default is iline '''))
sfintbin3.par('zkey',rsf.doc.rsfpar('int','','','''z key number (if no zk), default is xline '''))
sfintbin3.par('xmin',rsf.doc.rsfpar('int','','','''x minimum '''))
sfintbin3.par('xmax',rsf.doc.rsfpar('int','','','''x maximum '''))
sfintbin3.par('ymin',rsf.doc.rsfpar('int','','','''y minimum '''))
sfintbin3.par('ymax',rsf.doc.rsfpar('int','','','''y maximum '''))
sfintbin3.par('zmin',rsf.doc.rsfpar('int','','','''z minimum '''))
sfintbin3.par('zmax',rsf.doc.rsfpar('int','','','''z maximum '''))
sfintbin3.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfintbin3.par('xk',rsf.doc.rsfpar('string ',desc='''x key name '''))
sfintbin3.par('yk',rsf.doc.rsfpar('string ',desc='''y key name '''))
sfintbin3.par('zk',rsf.doc.rsfpar('string ',desc='''z key name '''))
sfintbin3.par('mask',rsf.doc.rsfpar('string ',desc='''output mask file '''))
sfintbin3.version('2.1-git')
sfintbin3.synopsis('''sfintbin3 < in.rsf > out.rsf xkey= ykey= zkey= xmin= xmax= ymin= ymax= zmin= zmax= head= xk= yk= zk= mask=''','''
if xkey < 0, the first axis indexes traces in a gather like cdpt.
''')
rsf.doc.progs['sfintbin3']=sfintbin3

sfisin2ang = rsf.doc.rsfprog('sfisin2ang','system/seismic/Misin2ang.c','''inverse sin to angle transformation ''')
sfisin2ang.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisin2ang.par('na',rsf.doc.rsfpar('int','nt','','''number of angles'''))
sfisin2ang.par('da',rsf.doc.rsfpar('float','90/(nt-1)','','''angle sampling '''))
sfisin2ang.par('a0',rsf.doc.rsfpar('float','0.','','''angle origin '''))
sfisin2ang.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sfisin2ang.par('top',rsf.doc.rsfpar('bool','n','','''velocity scaling option '''))
sfisin2ang.version('2.1-git')
sfisin2ang.synopsis('''sfisin2ang < Fstk.rsf > Fang.rsf velocity=velocity.rsf na=nt da=90/(nt-1) a0=0. extend=4 top=n''','''''')
rsf.doc.progs['sfisin2ang']=sfisin2ang

sfitaupmo = rsf.doc.rsfprog('sfitaupmo','system/seismic/Mitaupmo.c','''Inverse normal moveout in tau-p domain. ''')
sfitaupmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo.par('interval',rsf.doc.rsfpar('bool','y','','''use interval velocity '''))
sfitaupmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfitaupmo.par('eta',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfitaupmo.version('2.1-git')
sfitaupmo.synopsis('''sfitaupmo < cmp.rsf velocity=velocity.rsf > nmod.rsf eta=eta.rsf interval=y eps=0.01''','''''')
rsf.doc.progs['sfitaupmo']=sfitaupmo

sfitaupmo2 = rsf.doc.rsfprog('sfitaupmo2','system/seismic/Mitaupmo2.c','''Inverse normal moveout in tau-p-x domain. ''')
sfitaupmo2.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo2.par('nx',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfitaupmo2.par('dx',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfitaupmo2.par('x0',rsf.doc.rsfpar('float','0.0','','''first offset '''))
sfitaupmo2.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfitaupmo2.version('2.1-git')
sfitaupmo2.synopsis('''sfitaupmo2 < cmp.rsf velocity=velocity.rsf > nmod.rsf nx= dx= x0=0.0 nw=4''','''''')
rsf.doc.progs['sfitaupmo2']=sfitaupmo2

sfitaupmo3 = rsf.doc.rsfprog('sfitaupmo3','system/seismic/Mitaupmo3.c','''3-D Inverse taup normal moveout.''')
sfitaupmo3.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfitaupmo3.par('slow',rsf.doc.rsfpar('bool','n','','''slowness [y] or velocity [n] squared'''))
sfitaupmo3.par('interval',rsf.doc.rsfpar('bool','y','','''use interval velocity '''))
sfitaupmo3.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfitaupmo3.version('2.1-git')
sfitaupmo3.synopsis('''sfitaupmo3 < cmp.rsf > nmod.rsf velocity=vel.rsf eps=0.01 slow=n interval=y extend=8''','''
velocity file contains velocity squared with n2=3 (vx,vy,vxy)
''')
rsf.doc.progs['sfitaupmo3']=sfitaupmo3

sfitxmo = rsf.doc.rsfprog('sfitxmo','system/seismic/Mitxmo.c','''Forward and inverse normal moveout with interval velocity. ''')
sfitxmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfitxmo.par('nx',rsf.doc.rsfpar('int','','','''offset samples '''))
sfitxmo.par('dx',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfitxmo.par('x0',rsf.doc.rsfpar('float','0.','','''first offset '''))
sfitxmo.par('np',rsf.doc.rsfpar('int','','','''slope samples '''))
sfitxmo.par('dp',rsf.doc.rsfpar('float','','','''slope sampling '''))
sfitxmo.par('p0',rsf.doc.rsfpar('float','0.','','''first slope '''))
sfitxmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfitxmo.version('2.1-git')
sfitxmo.synopsis('''sfitxmo < inp.rsf > out.rsf velocity=velocity.rsf inv=n nx= dx= x0=0. np= dp= p0=0. eps=0.01''','''''')
rsf.doc.progs['sfitxmo']=sfitxmo

sfitxmo3 = rsf.doc.rsfprog('sfitxmo3','system/seismic/Mitxmo3.c','''Forward and inverse normal moveout with interval velocity. ''')
sfitxmo3.par('c11',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c22',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c33',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c44',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c55',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c66',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c12',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c13',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('c23',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitxmo3.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfitxmo3.par('x',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfitxmo3.par('y',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfitxmo3.par('cij',rsf.doc.rsfpar('bool','n','',''''''))
sfitxmo3.par('inv',rsf.doc.rsfpar('bool','n','',''''''))
sfitxmo3.par('nx',rsf.doc.rsfpar('int','','','''x offset samples '''))
sfitxmo3.par('dx',rsf.doc.rsfpar('float','','','''x offset sampling '''))
sfitxmo3.par('x0',rsf.doc.rsfpar('float','0.','','''x first offset '''))
sfitxmo3.par('ny',rsf.doc.rsfpar('int','','','''y offset samples '''))
sfitxmo3.par('dy',rsf.doc.rsfpar('float','','','''y offset sampling '''))
sfitxmo3.par('y0',rsf.doc.rsfpar('float','0.','','''y first offset '''))
sfitxmo3.par('npx',rsf.doc.rsfpar('int','','','''x slope samples '''))
sfitxmo3.par('dpx',rsf.doc.rsfpar('float','','','''x slope sampling '''))
sfitxmo3.par('px0',rsf.doc.rsfpar('float','0.','','''x first slope '''))
sfitxmo3.par('npy',rsf.doc.rsfpar('int','','','''y slope samples '''))
sfitxmo3.par('dpy',rsf.doc.rsfpar('float','','','''y slope sampling '''))
sfitxmo3.par('py0',rsf.doc.rsfpar('float','0.','','''y first slope '''))
sfitxmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfitxmo3.version('2.1-git')
sfitxmo3.synopsis('''sfitxmo3 < inp.rsf > out.rsf c11=C11.rsf c22=C22.rsf c33=C33.rsf c44=C44.rsf c55=C55.rsf c66=C66.rsf c12=C12.rsf c13=C13.rsf c23=C23.rsf velocity=velocity.rsf time=testtime.rsf x=testx.rsf y=testy.rsf cij=n inv=n nx= dx= x0=0. ny= dy= y0=0. npx= dpx= px0=0. npy= dpy= py0=0. eps=0.01''','''''')
rsf.doc.progs['sfitxmo3']=sfitxmo3

sfiwarp2 = rsf.doc.rsfprog('sfiwarp2','system/seismic/Miwarp2.c','''Inverse 2-D warping ''')
sfiwarp2.par('warp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfiwarp2.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sfiwarp2.par('n1',rsf.doc.rsfpar('int','nt','',''''''))
sfiwarp2.par('n2',rsf.doc.rsfpar('int','nx','','''output samples - for inv=y '''))
sfiwarp2.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfiwarp2.par('d1',rsf.doc.rsfpar('int','1','','''output sampling - for inv=y '''))
sfiwarp2.par('o1',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp2.par('d2',rsf.doc.rsfpar('float','1','','''output sampling - for inv=y '''))
sfiwarp2.par('o2',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp2.version('2.1-git')
sfiwarp2.synopsis('''sfiwarp2 < in.rsf > out.rsf warp=warp.rsf inv=y n1=nt n2=nx eps=0.01 d1=1 o1=0 d2=1 o2=0''','''''')
rsf.doc.progs['sfiwarp2']=sfiwarp2

sfiwarp3 = rsf.doc.rsfprog('sfiwarp3','system/seismic/Miwarp3.c','''Inverse 3-D warping ''')
sfiwarp3.par('warp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfiwarp3.par('inv',rsf.doc.rsfpar('bool','y','','''inversion flag '''))
sfiwarp3.par('n1',rsf.doc.rsfpar('int','nt','',''''''))
sfiwarp3.par('n2',rsf.doc.rsfpar('int','ny','',''''''))
sfiwarp3.par('n3',rsf.doc.rsfpar('int','nx','','''output samples - for inv=y '''))
sfiwarp3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfiwarp3.par('d1',rsf.doc.rsfpar('float','1','','''output sampling - for inv=y '''))
sfiwarp3.par('o1',rsf.doc.rsfpar('float','0','','''output origin - for inv=y '''))
sfiwarp3.version('2.1-git')
sfiwarp3.synopsis('''sfiwarp3 < in.rsf > out.rsf warp=warp.rsf inv=y n1=nt n2=ny n3=nx eps=0.01 d1=1 o1=0''','''''')
rsf.doc.progs['sfiwarp3']=sfiwarp3

sfkirchinv = rsf.doc.rsfprog('sfkirchinv','system/seismic/Mkirchinv.c','''Kirchhoff 2-D post-stack least-squares time migration with antialiasing. ''')
sfkirchinv.par('fweight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinv.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinv.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinv.par('model0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchinv.par('hd',rsf.doc.rsfpar('bool','y','','''if y, apply half-derivative filter '''))
sfkirchinv.par('ps',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfkirchinv.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfkirchinv.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfkirchinv.par('fweight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirchinv.par('model0',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirchinv.par('err',rsf.doc.rsfpar('string ',desc='''output file for error '''))
sfkirchinv.version('2.1-git')
sfkirchinv.synopsis('''sfkirchinv < in.rsf > out.rsf fweight=fwght.rsf weight=wght.rsf velocity=vel.rsf model0=in0.rsf hd=y ps=y sw=0 niter=10 err=''','''
Antialiasing by reparameterization. ''')
rsf.doc.progs['sfkirchinv']=sfkirchinv

sfkirchnew = rsf.doc.rsfprog('sfkirchnew','system/seismic/Mkirchnew.c','''Kirchhoff 2-D post-stack time migration and modeling with antialiasing. ''')
sfkirchnew.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirchnew.par('adj',rsf.doc.rsfpar('bool','y','','''yes: migration, no: modeling '''))
sfkirchnew.par('hd',rsf.doc.rsfpar('bool','y','','''if y, apply half-derivative filter '''))
sfkirchnew.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfkirchnew.par('v0',rsf.doc.rsfpar('float','','','''constant velocity (if no velocity=) '''))
sfkirchnew.par('velocity',rsf.doc.rsfpar('string ',desc='''velocity file (auxiliary input file name)'''))
sfkirchnew.version('2.1-git')
sfkirchnew.synopsis('''sfkirchnew < in.rsf > out.rsf velocity=vel.rsf adj=y hd=y sw=0 v0=''','''
Antialiasing by reparameterization. ''')
rsf.doc.progs['sfkirchnew']=sfkirchnew

sfkirmod = rsf.doc.rsfprog('sfkirmod','system/seismic/Mkirmod.c','''Kirchhoff 2-D/2.5-D modeling with analytical Green's functions. ''')
sfkirmod.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod.par('picks',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkirmod.par('slopes',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkirmod.par('lin',rsf.doc.rsfpar('bool','n','','''if linear operator '''))
sfkirmod.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfkirmod.par('absoff',rsf.doc.rsfpar('bool','n','','''y - h0 is not in shot coordinate system '''))
sfkirmod.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfkirmod.par('dt',rsf.doc.rsfpar('float','0.004','','''time sampling '''))
sfkirmod.par('t0',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfkirmod.par('ns',rsf.doc.rsfpar('int','nx','','''number of shots (midpoints if cmp=y) '''))
sfkirmod.par('s0',rsf.doc.rsfpar('float','x0','','''first shot (midpoint if cmp=y) '''))
sfkirmod.par('ds',rsf.doc.rsfpar('float','dx','','''shot/midpoint increment '''))
sfkirmod.par('nh',rsf.doc.rsfpar('int','nx','','''number of offsets '''))
sfkirmod.par('h0',rsf.doc.rsfpar('float','0.','','''first offset '''))
sfkirmod.par('dh',rsf.doc.rsfpar('float','dx','','''offset increment '''))
sfkirmod.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkirmod.par('r0',rsf.doc.rsfpar('float','1.','','''normal reflectivity (if constant) '''))
sfkirmod.par('r0',rsf.doc.rsfpar('float','1.','','''normal reflectivity (if constant) '''))
sfkirmod.par('twod',rsf.doc.rsfpar('bool','n','','''2-D or 2.5-D '''))
sfkirmod.par('cmp',rsf.doc.rsfpar('bool','n','','''compute CMP instead of shot gathers '''))
sfkirmod.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfkirmod.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfkirmod.par('gradx',rsf.doc.rsfpar('float','','','''horizontal velocity gradient '''))
sfkirmod.par('gradz',rsf.doc.rsfpar('float','','','''vertical velocity gradient '''))
sfkirmod.par('velz',rsf.doc.rsfpar('float','','','''vertical velocity for VTI anisotropy '''))
sfkirmod.par('eta',rsf.doc.rsfpar('float','','','''parameter for VTI anisotropy '''))
sfkirmod.par('refx',rsf.doc.rsfpar('float','','','''reference x-coordinate for velocity '''))
sfkirmod.par('refz',rsf.doc.rsfpar('float','','','''reference z-coordinate for velocity '''))
sfkirmod.par('vel2',rsf.doc.rsfpar('float','','','''converted velocity '''))
sfkirmod.par('gradx2',rsf.doc.rsfpar('float','','','''converted velocity, horizontal gradient '''))
sfkirmod.par('gradz2',rsf.doc.rsfpar('float','','','''converted velocity, vertical gradient '''))
sfkirmod.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirmod.par('rgrad',rsf.doc.rsfpar('string ',desc='''AVO gradient file (B/A) '''))
sfkirmod.par('dip',rsf.doc.rsfpar('string ',desc='''reflector dip file '''))
sfkirmod.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirmod.par('picks',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfkirmod.par('slopes',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfkirmod.par('type',rsf.doc.rsfpar('string ',desc='''type of velocity, 'c': constant, 's': linear sloth, 'v': linear velocity, 'a': VTI anisotropy '''))
sfkirmod.par('type2',rsf.doc.rsfpar('string ',desc='''type of velocity for the converted (receiver side) branch '''))
sfkirmod.version('2.1-git')
sfkirmod.synopsis('''sfkirmod < modl.rsf > data.rsf curv=curv.rsf refl=refl.rsf picks=picks.rsf slopes=slopes.rsf lin=n adj=n absoff=n nt= dt=0.004 t0=0. ns=nx s0=x0 ds=dx nh=nx h0=0. dh=dx verb=n r0=1. r0=1. twod=n cmp=n freq=0.2/dt vel= gradx= gradz= velz= eta= refx= refz= vel2= gradx2= gradz2= rgrad= dip= type= type2=''','''
October 2012 program of the month:
http://ahay.org/blog/2012/10/03/program-of-the-month-sfkirmod/
''')
rsf.doc.progs['sfkirmod']=sfkirmod

sfkirmod3 = rsf.doc.rsfprog('sfkirmod3','system/seismic/Mkirmod3.c','''Kirchhoff 3-D modeling with analytical Green's functions. ''')
sfkirmod3.par('head',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod3.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfkirmod3.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfkirmod3.par('dt',rsf.doc.rsfpar('float','0.004','','''time sampling '''))
sfkirmod3.par('t0',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfkirmod3.par('absoff',rsf.doc.rsfpar('bool','n','','''y - h0x, h0y - are not in shot coordinate system '''))
sfkirmod3.par('nsx',rsf.doc.rsfpar('int','nx','','''number of inline shots '''))
sfkirmod3.par('s0x',rsf.doc.rsfpar('float','x0','','''first inline shot '''))
sfkirmod3.par('dsx',rsf.doc.rsfpar('float','dx','','''inline shot increment '''))
sfkirmod3.par('nsy',rsf.doc.rsfpar('int','ny','','''number of crossline shots '''))
sfkirmod3.par('s0y',rsf.doc.rsfpar('float','y0','','''first crossline shot '''))
sfkirmod3.par('dsy',rsf.doc.rsfpar('float','dy','','''crossline shot increment '''))
sfkirmod3.par('nhx',rsf.doc.rsfpar('int','nx','','''number of inline offsets '''))
sfkirmod3.par('h0x',rsf.doc.rsfpar('float','0.','','''first inline offset '''))
sfkirmod3.par('dhx',rsf.doc.rsfpar('float','dx','','''inline offset increment '''))
sfkirmod3.par('nhy',rsf.doc.rsfpar('int','ny','','''number of crossline offsets '''))
sfkirmod3.par('h0y',rsf.doc.rsfpar('float','0.','','''first crossline offset '''))
sfkirmod3.par('dhy',rsf.doc.rsfpar('float','dy','','''crossline offset increment '''))
sfkirmod3.par('r0',rsf.doc.rsfpar('float','1.','','''constant reflectivity '''))
sfkirmod3.par('aper',rsf.doc.rsfpar('float','hypotf(nx*dx,ny*dy)','','''aperture '''))
sfkirmod3.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfkirmod3.par('head',rsf.doc.rsfpar('string ',desc='''source-receiver geometry (optional) (auxiliary input file name)'''))
sfkirmod3.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirmod3.par('rgrad',rsf.doc.rsfpar('string ',desc=''''''))
sfkirmod3.par('dipx',rsf.doc.rsfpar('string ',desc=''''''))
sfkirmod3.par('dipy',rsf.doc.rsfpar('string ',desc=''''''))
sfkirmod3.par('type',rsf.doc.rsfpar('string ',desc='''type of velocity ('c': constant, 's': linear sloth, 'v': linear velocity) '''))
sfkirmod3.version('2.1-git')
sfkirmod3.synopsis('''sfkirmod3 < curv.rsf > modl.rsf head=head.rsf refl=refl.rsf verb=y nt= dt=0.004 t0=0. absoff=n nsx=nx s0x=x0 dsx=dx nsy=ny s0y=y0 dsy=dy nhx=nx h0x=0. dhx=dx nhy=ny h0y=0. dhy=dy r0=1. aper=hypotf(nx*dx,ny*dy) freq=0.2/dt rgrad= dipx= dipy= type=''','''''')
rsf.doc.progs['sfkirmod3']=sfkirmod3

sflineiko = rsf.doc.rsfprog('sflineiko','system/seismic/Mlineiko.c','''Iterative solution of the linearized eikonal equation. ''')
sflineiko.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflineiko.par('squared',rsf.doc.rsfpar('bool','y','','''if slowness is squared '''))
sflineiko.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag (for what=linear) '''))
sflineiko.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag (for what=linear) '''))
sflineiko.par('niter',rsf.doc.rsfpar('int','1','','''maximum number of iterations '''))
sflineiko.par('tol',rsf.doc.rsfpar('float','0.001','','''tolerance for convergence '''))
sflineiko.par('what',rsf.doc.rsfpar('string ',desc='''what to compute '''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('time',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflineiko.version('2.1-git')
sflineiko.synopsis('''sflineiko < time.rsf > dtime.rsf time=time0.rsf slow=slow.rsf mask=mask.rsf squared=y adj=n inv=n niter=1 tol=0.001 what=''','''''')
rsf.doc.progs['sflineiko']=sflineiko

sflinsincos = rsf.doc.rsfprog('sflinsincos','system/seismic/Mlinsincos.c','''Solve for angle in equation vx*sin(d) + vy*cos(d) = 1/s0. ''')
sflinsincos.par('s0',rsf.doc.rsfpar('float','','','''reference slowness '''))
sflinsincos.par('na',rsf.doc.rsfpar('int','','','''number of angle values. '''))
sflinsincos.par('da',rsf.doc.rsfpar('float','','','''angle sampling. '''))
sflinsincos.par('oa',rsf.doc.rsfpar('float','','','''angle origin '''))
sflinsincos.par('nt',rsf.doc.rsfpar('int','180','','''number of polar angle for integration. '''))
sflinsincos.par('dt',rsf.doc.rsfpar('float','2.','','''polar angle sampling. '''))
sflinsincos.par('ot',rsf.doc.rsfpar('float','0.','','''polar angle origin '''))
sflinsincos.par('nr',rsf.doc.rsfpar('int','nvx/2','','''number of radius on radial lines '''))
sflinsincos.par('dr',rsf.doc.rsfpar('float','dvx','','''radius sampling. '''))
sflinsincos.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sflinsincos.version('2.1-git')
sflinsincos.synopsis('''sflinsincos < in.rsf > out.rsf s0= na= da= oa= nt=180 dt=2. ot=0. nr=nvx/2 dr=dvx extend=4''','''''')
rsf.doc.progs['sflinsincos']=sflinsincos

sfmigsteep3 = rsf.doc.rsfprog('sfmigsteep3','system/seismic/Mmigsteep3.c','''3-D Kirchhoff time migration for antialiased steep dips. ''')
sfmigsteep3.par('hdr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmigsteep3.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('o2',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('d3',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('o3',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('vel',rsf.doc.rsfpar('float','','','''migration velocity '''))
sfmigsteep3.version('2.1-git')
sfmigsteep3.synopsis('''sfmigsteep3 < in.rsf hdr=head.rsf > mig.rsf n2= d2= o2= n3= d3= o3= n1= vel=''','''
Combine with sfmig3 antialias=flat for the complete response.
''')
rsf.doc.progs['sfmigsteep3']=sfmigsteep3

sfmodrefl = rsf.doc.rsfprog('sfmodrefl','system/seismic/Mmodrefl.c','''Normal reflectivity modeling. ''')
sfmodrefl.par('vp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmodrefl.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmodrefl.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfmodrefl.par('nw',rsf.doc.rsfpar('int','4','','''interpolation length '''))
sfmodrefl.version('2.1-git')
sfmodrefl.synopsis('''sfmodrefl < depth.rsf vp=vp.rsf vs=vs.rsf rho=rho.rsf > dat.rsf nt= dt= nw=4''','''''')
rsf.doc.progs['sfmodrefl']=sfmodrefl

sfmodrefl2 = rsf.doc.rsfprog('sfmodrefl2','system/seismic/Mmodrefl2.c','''Normal reflectivity modeling. ''')
sfmodrefl2.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmodrefl2.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfmodrefl2.par('nw',rsf.doc.rsfpar('int','4','','''interpolation length '''))
sfmodrefl2.version('2.1-git')
sfmodrefl2.synopsis('''sfmodrefl2 < in.rsf > out.rsf nt= dt= nw=4''','''
In this version, the input contains Vp, Vs, and density into one file. 
The output contains PP intercept, PP gradient, and PS gradient.

''')
rsf.doc.progs['sfmodrefl2']=sfmodrefl2

sfmodrefl3 = rsf.doc.rsfprog('sfmodrefl3','system/seismic/Mmodrefl3.c','''Normal reflectivity modeling. ''')
sfmodrefl3.par('sparse',rsf.doc.rsfpar('int','10','','''sparseness of reflectivity '''))
sfmodrefl3.par('moveout',rsf.doc.rsfpar('bool','y','','''if apply moveout '''))
sfmodrefl3.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmodrefl3.par('dt',rsf.doc.rsfpar('float','','','''time sampling '''))
sfmodrefl3.par('np',rsf.doc.rsfpar('int','','','''slope samples '''))
sfmodrefl3.par('dp',rsf.doc.rsfpar('float','','','''slope sampling '''))
sfmodrefl3.par('p0',rsf.doc.rsfpar('float','','','''slope origin '''))
sfmodrefl3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfmodrefl3.version('2.1-git')
sfmodrefl3.synopsis('''sfmodrefl3 < in.rsf > out.rsf sparse=10 moveout=y nt= dt= np= dp= p0= eps=0.01''','''
In this version, the input contains Vp, Vs, and density into one file. 
The output contains PP and PS tau-p seismograms.

''')
rsf.doc.progs['sfmodrefl3']=sfmodrefl3

sfmoveout = rsf.doc.rsfprog('sfmoveout','system/seismic/Mmoveout.c','''Put spikes at an arbitrary moveout ''')
sfmoveout.par('n1',rsf.doc.rsfpar('int','','','''time samples '''))
sfmoveout.par('d1',rsf.doc.rsfpar('float','1.','','''time sampling '''))
sfmoveout.par('o1',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfmoveout.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfmoveout.par('nw',rsf.doc.rsfpar('int','10','','''wavelet length '''))
sfmoveout.version('2.1-git')
sfmoveout.synopsis('''sfmoveout < warp.rsf > out.rsf n1= d1=1. o1=0. eps=0.1 nw=10''','''''')
rsf.doc.progs['sfmoveout']=sfmoveout

sfnmo = rsf.doc.rsfprog('sfnmo','system/seismic/Mnmo.c','''Normal moveout.''')
sfnmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('s',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfnmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfnmo.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfnmo.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfnmo.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfnmo.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfnmo.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfnmo.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfnmo.par('s',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.par('a',rsf.doc.rsfpar('string ',desc=''''''))
sfnmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo.version('2.1-git')
sfnmo.synopsis('''sfnmo < cmp.rsf velocity=velocity.rsf > nmod.rsf s=het.rsf offset=offset.rsf mask=msk.rsf half=y str=0.5 mute=12 CDPtype= slowness=n squared=n h0=0. extend=4 a=''','''
Compatible with sfvscan.

April 2013 program of the month:
http://ahay.org/blog/2013/04/08/program-of-the-month-sfnmo/
''')
rsf.doc.progs['sfnmo']=sfnmo

sfnmo3 = rsf.doc.rsfprog('sfnmo3','system/seismic/Mnmo3.c','''3-D Normal moveout.''')
sfnmo3.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfnmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfnmo3.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfnmo3.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfnmo3.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo3.version('2.1-git')
sfnmo3.synopsis('''sfnmo3 < cmp.rsf > nmod.rsf velocity=vel.rsf offset=offset.rsf half=y eps=0.01 mute=12 extend=8''','''
input data has gathers along *4th* axis; 
velocity file contains slowness squared with n2=3 (wx,wy,wxy);
offset file contains x,y offset pairs for input data
''')
rsf.doc.progs['sfnmo3']=sfnmo3

sfnmo3_ort = rsf.doc.rsfprog('sfnmo3_ort','system/seismic/Mnmo3_ort.c','''3-D Normal moveout using orthogonal parametrization''')
sfnmo3_ort.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3_ort.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3_ort.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfnmo3_ort.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfnmo3_ort.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfnmo3_ort.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfnmo3_ort.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo3_ort.version('2.1-git')
sfnmo3_ort.synopsis('''sfnmo3_ort < cmp.rsf > nmod.rsf velocity=vel.rsf offset=offset.rsf half=y eps=0.01 mute=12 extend=8''','''
input data has gathers along *4th* axis; 
velocity file contains slowness squared with n2=3 (Wavg,Wcos,Wsin);
offset file contains x,y offset pairs for input data
''')
rsf.doc.progs['sfnmo3_ort']=sfnmo3_ort

sfnmodips = rsf.doc.rsfprog('sfnmodips','system/seismic/Mnmodips.c','''Slopes for constant-velocity normal moveout. ''')
sfnmodips.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmodips.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfnmodips.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfnmodips.par('v0',rsf.doc.rsfpar('float','','','''first velocity '''))
sfnmodips.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sfnmodips.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfnmodips.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfnmodips.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfnmodips.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfnmodips.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfnmodips.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmodips.version('2.1-git')
sfnmodips.synopsis('''sfnmodips < cmp.rsf > dip.rsf offset=offset.rsf half=y nv= v0= dv= CDPtype= slowness=n squared=n h0=0. extend=4''','''''')
rsf.doc.progs['sfnmodips']=sfnmodips

sfnmov = rsf.doc.rsfprog('sfnmov','system/seismic/Mnmov.c','''Least-squares fitting of t^2-t_0^2 surfaces for isotropic V_{nmo}.''')
sfnmov.version('2.1-git')
sfnmov.synopsis('''sfnmov < inp.rsf > out.rsf''','''''')
rsf.doc.progs['sfnmov']=sfnmov

sfnmow = rsf.doc.rsfprog('sfnmow','system/seismic/Mnmow.c','''Least-squares fitting of t^2-t_0^2 surfaces for elliptical slowness matrix, W.''')
sfnmow.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmow.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfnmow.par('nw',rsf.doc.rsfpar('int','3','',''''''))
sfnmow.par('offset',rsf.doc.rsfpar('string ',desc='''If offset file is provided, it must be of the form:(auxiliary input file name)'''))
sfnmow.version('2.1-git')
sfnmow.synopsis('''sfnmow < inp.rsf > out.rsf offset=offset.rsf half=y nw=3''','''''')
rsf.doc.progs['sfnmow']=sfnmow

sfnmow_adj = rsf.doc.rsfprog('sfnmow_adj','system/seismic/Mnmow_adj.c','''None''')
sfnmow_adj.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmow_adj.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfnmow_adj.par('nw',rsf.doc.rsfpar('int','3','',''''''))
sfnmow_adj.version('2.1-git')
sfnmow_adj.synopsis('''sfnmow_adj < inp.rsf > out.rsf gather=gather.rsf adj=n nw=3''','''''')
rsf.doc.progs['sfnmow_adj']=sfnmow_adj

sfnmo3gma_adj = rsf.doc.rsfprog('sfnmo3gma_adj','system/seismic/Mnmo3gma_adj.c','''Fwd-Adj of 3D NMO GMA for iterative LS coefficient solve ''')
sfnmo3gma_adj.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gma_adj.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gma_adj.par('t0sq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gma_adj.par('adj',rsf.doc.rsfpar('bool','y','',''''''))
sfnmo3gma_adj.par('nw',rsf.doc.rsfpar('int','16','','''16 parameters of 3D GMA'''))
sfnmo3gma_adj.version('2.1-git')
sfnmo3gma_adj.synopsis('''sfnmo3gma_adj < inp.rsf > out.rsf gather=gather.rsf mod=inicoef.rsf t0sq=t0sqf.rsf adj=y nw=16''','''''')
rsf.doc.progs['sfnmo3gma_adj']=sfnmo3gma_adj

sfovc = rsf.doc.rsfprog('sfovc','system/seismic/Movc.c','''Oriented velocity continuation. ''')
sfovc.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfovc.par('nv',rsf.doc.rsfpar('int','1','','''number of velocity steps '''))
sfovc.par('lagrange',rsf.doc.rsfpar('bool','n','','''Use Lagrangian method '''))
sfovc.par('v0',rsf.doc.rsfpar('float','0.','','''starting velocity '''))
sfovc.par('vmax',rsf.doc.rsfpar('float','','','''end velocity '''))
sfovc.version('2.1-git')
sfovc.synopsis('''sfovc < in.rsf > out.rsf eps=0.1 nv=1 lagrange=n v0=0. vmax=''','''
Axis order: t, p, x
''')
rsf.doc.progs['sfovc']=sfovc

sfovcco = rsf.doc.rsfprog('sfovcco','system/seismic/Movcco.c','''Prestack (common-offset) 2-D oriented velocity continuation. ''')
sfovcco.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfovcco.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfovcco.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfovcco.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfovcco.version('2.1-git')
sfovcco.synopsis('''sfovcco < in.rsf > out.rsf verb=y nv= dv= v0=''','''
Axes: (Omega,h,k,p) -> (Omega,v,k,p)
''')
rsf.doc.progs['sfovcco']=sfovcco

sfovczo = rsf.doc.rsfprog('sfovczo','system/seismic/Movczo.c','''Post-stack 2-D oriented velocity continuation. ''')
sfovczo.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfovczo.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfovczo.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfovczo.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfovczo.version('2.1-git')
sfovczo.synopsis('''sfovczo < in.rsf > out.rsf verb=y nv= dv= v0=''','''
Axes: (Omega,k,p) -> (Omega,v,k,p)
''')
rsf.doc.progs['sfovczo']=sfovczo

sfoway1 = rsf.doc.rsfprog('sfoway1','system/seismic/Moway1.c','''Oriented one-way wave equation. ''')
sfoway1.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfoway1.par('vgrad',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfoway1.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfoway1.par('lagrange',rsf.doc.rsfpar('bool','n','','''Use Lagrangian method '''))
sfoway1.version('2.1-git')
sfoway1.synopsis('''sfoway1 < in.rsf > out.rsf velocity=vel.rsf vgrad=vgrad.rsf eps=0.1 lagrange=n''','''
Axis order: x, p, t
''')
rsf.doc.progs['sfoway1']=sfoway1

sfpmig = rsf.doc.rsfprog('sfpmig','system/seismic/Mpmig.c','''Slope-based prestack time migration. ''')
sfpmig.par('xdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig.par('hdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpmig.par('mzo',rsf.doc.rsfpar('bool','n','','''do migration to zero offset '''))
sfpmig.par('eps',rsf.doc.rsfpar('float','1.0','','''stretch regularization '''))
sfpmig.version('2.1-git')
sfpmig.synopsis('''sfpmig < cmp.rsf xdip=xdip.rsf hdip=hdip.rsf > mig.rsf half=y mzo=n eps=1.0''','''''')
rsf.doc.progs['sfpmig']=sfpmig

sfpnmo = rsf.doc.rsfprog('sfpnmo','system/seismic/Mpnmo.c','''Slope-based normal moveout. ''')
sfpnmo.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('crv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpnmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpnmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmo.par('crv',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmo.version('2.1-git')
sfpnmo.synopsis('''sfpnmo < cmp.rsf dip=dip.rsf > nmod.rsf vel=vel.rsf offset=offset.rsf crv=crv.rsf eta=eta.rsf half=y eps=0.01''','''''')
rsf.doc.progs['sfpnmo']=sfpnmo

sfpnmo3d = rsf.doc.rsfprog('sfpnmo3d','system/seismic/Mpnmo3d.c','''Slope-based normal moveout for 3-D CMP geometry. ''')
sfpnmo3d.par('dipx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo3d.par('dipy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo3d.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpnmo3d.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpnmo3d.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfpnmo3d.version('2.1-git')
sfpnmo3d.synopsis('''sfpnmo3d < cmp.rsf dipx=dipx.rsf dipy=dipy.rsf > nmod.rsf vel=vel.rsf half=y eps=0.01 extend=8''','''''')
rsf.doc.progs['sfpnmo3d']=sfpnmo3d

sfpp2psang = rsf.doc.rsfprog('sfpp2psang','system/seismic/Mpp2psang.c','''Transform PP angle gathers to PS angle gathers. ''')
sfpp2psang.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2psang.par('nw',rsf.doc.rsfpar('int','4','','''accuracy level '''))
sfpp2psang.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfpp2psang.version('2.1-git')
sfpp2psang.synopsis('''sfpp2psang < in.rsf > out.rsf vpvs=vpvs.rsf nw=4 inv=n''','''* (designed for absolute offsets)
''')
rsf.doc.progs['sfpp2psang']=sfpp2psang

sfpp2psang2 = rsf.doc.rsfprog('sfpp2psang2','system/seismic/Mpp2psang2.c','''Transform PP angle gathers to PS angle gathers. ''')
sfpp2psang2.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2psang2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2psang2.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfpp2psang2.par('nw',rsf.doc.rsfpar('int','4','','''accuracy level '''))
sfpp2psang2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfpp2psang2.version('2.1-git')
sfpp2psang2.synopsis('''sfpp2psang2 < in.rsf > out.rsf vpvs=vpvs.rsf dip=dip.rsf verb=n nw=4 inv=n''','''* (designed for horizontal offsets)
''')
rsf.doc.progs['sfpp2psang2']=sfpp2psang2

sfpp2pstsic = rsf.doc.rsfprog('sfpp2pstsic','system/seismic/Mpp2pstsic.c','''Compute angle gathers for time-shift imaging condition ''')
sfpp2pstsic.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2pstsic.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2pstsic.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpp2pstsic.par('na',rsf.doc.rsfpar('int','nv','',''''''))
sfpp2pstsic.par('da',rsf.doc.rsfpar('float','1./(nv-1)','',''''''))
sfpp2pstsic.par('a0',rsf.doc.rsfpar('float','0.','',''''''))
sfpp2pstsic.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sfpp2pstsic.version('2.1-git')
sfpp2pstsic.synopsis('''sfpp2pstsic < Fstk.rsf velocity=Fvel.rsf vpvs=Fgam.rsf dip=Fdip.rsf > Fang.rsf na=nv da=1./(nv-1) a0=0. extend=4''','''''')
rsf.doc.progs['sfpp2pstsic']=sfpp2pstsic

sfpreconstkirch = rsf.doc.rsfprog('sfpreconstkirch','system/seismic/Mpreconstkirch.c','''Prestack Kirchhoff modeling/migration in constant velocity. ''')
sfpreconstkirch.par('inv',rsf.doc.rsfpar('bool','n','','''if y, modeling; if n, migration '''))
sfpreconstkirch.par('zero',rsf.doc.rsfpar('bool','n','','''if y, stack in migration '''))
sfpreconstkirch.par('aal',rsf.doc.rsfpar('bool','y','','''if y, apply antialiasing '''))
sfpreconstkirch.par('nh',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfpreconstkirch.par('dh',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfpreconstkirch.par('h0',rsf.doc.rsfpar('float','','','''offset origin '''))
sfpreconstkirch.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfpreconstkirch.version('2.1-git')
sfpreconstkirch.synopsis('''sfpreconstkirch < in.rsf > out.rsf inv=n zero=n aal=y nh= dh= h0= vel=''','''
Requires the input to be in (time,cmp x,cmp y,offset)
''')
rsf.doc.progs['sfpreconstkirch']=sfpreconstkirch

sfprestolt = rsf.doc.rsfprog('sfprestolt','system/seismic/Mprestolt.c','''Prestack Stolt modeling/migration. ''')
sfprestolt.par('inv',rsf.doc.rsfpar('bool','n','','''y: modeling, n: migration '''))
sfprestolt.par('depth',rsf.doc.rsfpar('bool','n','','''y: depth migration, n: time migration '''))
sfprestolt.par('stack',rsf.doc.rsfpar('bool','y','','''if y: stack migrated image '''))
sfprestolt.par('nh',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfprestolt.par('dh',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfprestolt.par('vel',rsf.doc.rsfpar('float','','','''constant velocity '''))
sfprestolt.par('pad',rsf.doc.rsfpar('int','nt','','''padding on the time axis '''))
sfprestolt.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfprestolt.version('2.1-git')
sfprestolt.synopsis('''sfprestolt < in.rsf > out.rsf inv=n depth=n stack=y nh= dh= vel= pad=nt extend=4''','''''')
rsf.doc.progs['sfprestolt']=sfprestolt

sfptaupmo3 = rsf.doc.rsfprog('sfptaupmo3','system/seismic/Mptaupmo3.c','''Slope-based tau-p 3D moveout. ''')
sfptaupmo3.par('dip1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo3.par('dip2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo3.par('tau0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfptaupmo3.par('dip1',rsf.doc.rsfpar('string ',desc='''slope field mesaure along dimension 2(auxiliary input file name)'''))
sfptaupmo3.par('dip2',rsf.doc.rsfpar('string ',desc='''slope field mesaure along dimension 3(auxiliary input file name)'''))
sfptaupmo3.par('tau0',rsf.doc.rsfpar('string ',desc='''tau0(tau,p) (auxiliary output file name)'''))
sfptaupmo3.version('2.1-git')
sfptaupmo3.synopsis('''sfptaupmo3 < inp.rsf dip1=dip1.rsf dip2=dip2.rsf > nmod.rsf tau0=tau0.rsf eps=0.01''','''''')
rsf.doc.progs['sfptaupmo3']=sfptaupmo3

sfptaupmo = rsf.doc.rsfprog('sfptaupmo','system/seismic/Mptaupmo.c','''Slope-based tau-p moveout. ''')
sfptaupmo.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo.par('vel2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfptaupmo.par('v0',rsf.doc.rsfpar('float','0.','','''initial velocity '''))
sfptaupmo.par('type',rsf.doc.rsfpar('string ',desc='''transform type '''))
sfptaupmo.version('2.1-git')
sfptaupmo.synopsis('''sfptaupmo < inp.rsf dip=dip.rsf dipt=dipt.rsf > nmod.rsf vel2=vel2.rsf eps=0.01 v0=0. type=''','''''')
rsf.doc.progs['sfptaupmo']=sfptaupmo

sfptaupmoVTI = rsf.doc.rsfprog('sfptaupmoVTI','system/seismic/MptaupmoVTI.c','''Slope-based tau-p moveout in VTI. ''')
sfptaupmoVTI.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmoVTI.par('ddip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmoVTI.par('tau0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmoVTI.par('cos2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmoVTI.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfptaupmoVTI.par('dip',rsf.doc.rsfpar('string ',desc='''slope field (auxiliary input file name)'''))
sfptaupmoVTI.par('ddip',rsf.doc.rsfpar('string ',desc='''curvature field (auxiliary input file name)'''))
sfptaupmoVTI.par('tau0',rsf.doc.rsfpar('string ',desc='''tau0(tau,p) (auxiliary output file name)'''))
sfptaupmoVTI.version('2.1-git')
sfptaupmoVTI.synopsis('''sfptaupmoVTI < inp.rsf dip=dip.rsf ddip=ddip.rsf > nmod.rsf tau0=tau0.rsf cos2=cos2.rsf eps=0.01''','''''')
rsf.doc.progs['sfptaupmoVTI']=sfptaupmoVTI

sfpveltran = rsf.doc.rsfprog('sfpveltran','system/seismic/Mpveltran.c','''Slope-based velocity transform. ''')
sfpveltran.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpveltran.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfpveltran.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfpveltran.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfpveltran.par('interval',rsf.doc.rsfpar('bool','n','','''if y, compute interval velocity '''))
sfpveltran.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfpveltran.version('2.1-git')
sfpveltran.synopsis('''sfpveltran < cmp.rsf dip=dip.rsf > vel.rsf dipt=dipt.rsf half=y nv= v0= dv= interval=n eps=0.1''','''''')
rsf.doc.progs['sfpveltran']=sfpveltran

sfmap2coh = rsf.doc.rsfprog('sfmap2coh','system/seismic/Mmap2coh.c','''From parameter's attribute map (veltran) to coherency-like plots. ''')
sfmap2coh.par('map',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmap2coh.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfmap2coh.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfmap2coh.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfmap2coh.par('min2',rsf.doc.rsfpar('float','o2','','''min2 '''))
sfmap2coh.par('max2',rsf.doc.rsfpar('float','o2+d2*(n2-1)','','''max2 '''))
sfmap2coh.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfmap2coh.par('map',rsf.doc.rsfpar('string ',desc='''parameters map (auxiliary input file name)'''))
sfmap2coh.version('2.1-git')
sfmap2coh.synopsis('''sfmap2coh < cmp.rsf map=map.rsf > coh.rsf nv= v0= dv= min2=o2 max2=o2+d2*(n2-1) nw=4''','''(eventually masked) ''')
rsf.doc.progs['sfmap2coh']=sfmap2coh

sfpveltranVTI = rsf.doc.rsfprog('sfpveltranVTI','system/seismic/MpveltranVTI.c','''Slope-based tau-p velocity transform for VTI media. ''')
sfpveltranVTI.par('velH',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltranVTI.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltranVTI.par('cmp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('tau0t',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('curvt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltranVTI.par('map',rsf.doc.rsfpar('bool','n','','''output maps instead of coherency panels '''))
sfpveltranVTI.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfpveltranVTI.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfpveltranVTI.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfpveltranVTI.par('nvh',rsf.doc.rsfpar('int','nv','','''number of HOR velocities  '''))
sfpveltranVTI.par('vh0',rsf.doc.rsfpar('float','v0','','''HOR velocity origin '''))
sfpveltranVTI.par('dvh',rsf.doc.rsfpar('float','dv','','''HOR velocity sampling '''))
sfpveltranVTI.par('ne',rsf.doc.rsfpar('int','101','','''number of etas '''))
sfpveltranVTI.par('e0',rsf.doc.rsfpar('float','-0.5','','''eta origin '''))
sfpveltranVTI.par('de',rsf.doc.rsfpar('float','0.01','','''eta sampling '''))
sfpveltranVTI.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfpveltranVTI.par('method',rsf.doc.rsfpar('string ',desc='''method to use (stripping,dix,fowler,effective) '''))
sfpveltranVTI.par('dip',rsf.doc.rsfpar('string ',desc='''slope field (required for method=e and method=d) (auxiliary input file name)'''))
sfpveltranVTI.par('curv',rsf.doc.rsfpar('string ',desc='''curvature field (required for method=e and method=d) (auxiliary input file name)'''))
sfpveltranVTI.par('dipt',rsf.doc.rsfpar('string ',desc='''time derivative of slope field(auxiliary input file name)'''))
sfpveltranVTI.par('tau0t',rsf.doc.rsfpar('string ',desc='''tau0 tau derivative field (required for method=f) (auxiliary input file name)'''))
sfpveltranVTI.par('curvt',rsf.doc.rsfpar('string ',desc='''time derivative of curvature field (required for method=d and method=s) (auxiliary input file name)'''))
sfpveltranVTI.version('2.1-git')
sfpveltranVTI.synopsis('''sfpveltranVTI < tau0.rsf > velN.rsf velH=velH.rsf eta=eta.rsf cmp=cmp.rsf dip=dip.rsf curv=curv.rsf dipt=dipt.rsf tau0t=tau0t.rsf curvt=curvt.rsf map=n nv= v0= dv= nvh=nv vh0=v0 dvh=dv ne=101 e0=-0.5 de=0.01 nw=4 method=''','''''')
rsf.doc.progs['sfpveltranVTI']=sfpveltranVTI

sfpveltran3 = rsf.doc.rsfprog('sfpveltran3','system/seismic/Mpveltran3.c','''Slope-based tau-p 3D velocity transform for elliptical anisotropy.''')
sfpveltran3.par('vely',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltran3.par('velxy',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpveltran3.par('cmp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipxy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran3.par('map',rsf.doc.rsfpar('bool','n','','''output maps instead of coherency panels '''))
sfpveltran3.par('interval',rsf.doc.rsfpar('bool','n','','''interval values by 3D stripping equations '''))
sfpveltran3.par('nvx',rsf.doc.rsfpar('int','','','''number of vx squared velocities '''))
sfpveltran3.par('vx0',rsf.doc.rsfpar('float','','','''vx squared velocity origin '''))
sfpveltran3.par('dvx',rsf.doc.rsfpar('float','','','''vx squared velocity sampling '''))
sfpveltran3.par('nvy',rsf.doc.rsfpar('int','nvx','','''number of vy squared velocities  '''))
sfpveltran3.par('vy0',rsf.doc.rsfpar('float','vx0','','''vy squared  velocity origin '''))
sfpveltran3.par('dvy',rsf.doc.rsfpar('float','dvx','','''vy squared  velocity sampling '''))
sfpveltran3.par('nvxy',rsf.doc.rsfpar('int','101','','''number of vxy velocities '''))
sfpveltran3.par('vxy0',rsf.doc.rsfpar('float','-0.1','','''vxy   velocity origin '''))
sfpveltran3.par('dvxy',rsf.doc.rsfpar('float','0.1','','''vxy   velocity sampling '''))
sfpveltran3.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfpveltran3.par('cmp',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipx',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipy',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpveltran3.par('dipxy',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpveltran3.version('2.1-git')
sfpveltran3.synopsis('''sfpveltran3 < input.rsf > velx.rsf vely=vely.rsf velxy=velxy.rsf cmp=cmp.rsf dipx=dipx.rsf dipy=dipy.rsf dipxy=dipxy.rsf map=n interval=n nvx= vx0= dvx= nvy=nvx vy0=vx0 dvy=dvx nvxy=101 vxy0=-0.1 dvxy=0.1 nw=4''','''* The program returns the squared velocity vx,vy,vxy spectra or maps
''')
rsf.doc.progs['sfpveltran3']=sfpveltran3

sfpyramid = rsf.doc.rsfprog('sfpyramid','system/seismic/Mpyramid.c','''Pyramid transform ''')
sfpyramid.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfpyramid.par('nu',rsf.doc.rsfpar('int','','',''''''))
sfpyramid.par('du',rsf.doc.rsfpar('float','dx','',''''''))
sfpyramid.par('u0',rsf.doc.rsfpar('float','x0','',''''''))
sfpyramid.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpyramid.version('2.1-git')
sfpyramid.synopsis('''sfpyramid < in.rsf > out.rsf inv=n nu= du=dx u0=x0 eps=0.01''','''''')
rsf.doc.progs['sfpyramid']=sfpyramid

sfradial = rsf.doc.rsfprog('sfradial','system/seismic/Mradial.c','''Radial transform. ''')
sfradial.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfradial.par('nw',rsf.doc.rsfpar('int','2','','''accuracy level '''))
sfradial.par('tp',rsf.doc.rsfpar('float','t0','',''''''))
sfradial.par('xp',rsf.doc.rsfpar('float','0.','',''''''))
sfradial.par('nv',rsf.doc.rsfpar('int','','','''number of velocities (if inv=n) '''))
sfradial.par('vmin',rsf.doc.rsfpar('float','','','''minimum velocity (if inv=n) '''))
sfradial.par('vmax',rsf.doc.rsfpar('float','','','''maximum velocity (if inv=n) '''))
sfradial.version('2.1-git')
sfradial.synopsis('''sfradial < in.rsf > out.rsf inv=n nw=2 tp=t0 xp=0. nv= vmin= vmax=''','''''')
rsf.doc.progs['sfradial']=sfradial

sfradial2 = rsf.doc.rsfprog('sfradial2','system/seismic/Mradial2.c','''Another version of radial transform. ''')
sfradial2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfradial2.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfradial2.par('tp',rsf.doc.rsfpar('float','t0','',''''''))
sfradial2.par('nv',rsf.doc.rsfpar('int','','','''number of velocities (if inv=n) '''))
sfradial2.par('vmin',rsf.doc.rsfpar('float','','','''minimum velocity (if inv=n) '''))
sfradial2.par('vmax',rsf.doc.rsfpar('float','','','''maximum velocity (if inv=n) '''))
sfradial2.version('2.1-git')
sfradial2.synopsis('''sfradial2 < in.rsf > out.rsf inv=n eps=0.01 tp=t0 nv= vmin= vmax=''','''''')
rsf.doc.progs['sfradial2']=sfradial2

sfradon = rsf.doc.rsfprog('sfradon','system/seismic/Mradon.c','''High-resolution Radon transform. ''')
sfradon.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfradon.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sfradon.par('inv',rsf.doc.rsfpar('bool','adj','','''if y, perform inverse operation '''))
sfradon.par('spk',rsf.doc.rsfpar('bool','inv','','''if y, use spiking (hi-res) inversion '''))
sfradon.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfradon.par('np',rsf.doc.rsfpar('int','','','''number of p values (if adj=y) '''))
sfradon.par('dp',rsf.doc.rsfpar('float','','','''p sampling (if adj=y) '''))
sfradon.par('p0',rsf.doc.rsfpar('float','','','''p origin (if adj=y) '''))
sfradon.par('nx',rsf.doc.rsfpar('int','','','''number of offsets (if adj=n) '''))
sfradon.par('eps',rsf.doc.rsfpar('float','1.','',''''''))
sfradon.par('ns',rsf.doc.rsfpar('int','1','','''number of sharpening cycles '''))
sfradon.par('tol',rsf.doc.rsfpar('float','1.e-6','','''inversion tolerance '''))
sfradon.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfradon.par('ox',rsf.doc.rsfpar('float','','',''''''))
sfradon.par('dx',rsf.doc.rsfpar('float','','',''''''))
sfradon.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform '''))
sfradon.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfradon.par('niter',rsf.doc.rsfpar('int','100','',''''''))
sfradon.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfradon.version('2.1-git')
sfradon.synopsis('''sfradon < in.rsf > out.rsf offset=offset.rsf adj=y inv=adj spk=inv verb=n np= dp= p0= nx= eps=1. ns=1 tol=1.e-6 perc=50.0 ox= dx= parab=n x0=1. niter=100''','''''')
rsf.doc.progs['sfradon']=sfradon

sfrandrefl = rsf.doc.rsfprog('sfrandrefl','system/seismic/Mrandrefl.c','''Simple synthetics with random reflectivity. ''')
sfrandrefl.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrandrefl.par('fo',rsf.doc.rsfpar('floats','','',''' [3]'''))
sfrandrefl.par('nr',rsf.doc.rsfpar('int','','','''number of reflectors '''))
sfrandrefl.par('n1',rsf.doc.rsfpar('int','3501','','''time length '''))
sfrandrefl.par('d1',rsf.doc.rsfpar('float','0.001','','''time sampling '''))
sfrandrefl.par('o1',rsf.doc.rsfpar('float','0.0','','''time origin '''))
sfrandrefl.par('tscale',rsf.doc.rsfpar('float','1.','','''maximum time '''))
sfrandrefl.par('func',rsf.doc.rsfpar('string ',desc='''type of vpvs function '''))
sfrandrefl.version('2.1-git')
sfrandrefl.synopsis('''sfrandrefl > mod.rsf vpvs=vpvs.rsf fo= nr= n1=3501 d1=0.001 o1=0.0 tscale=1. func=''','''''')
rsf.doc.progs['sfrandrefl']=sfrandrefl

sfrays2 = rsf.doc.rsfprog('sfrays2','system/seismic/Mrays2.c','''Ray tracing by a Runge-Kutta integrator.''')
sfrays2.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays2.par('anglefile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays2.par('vel',rsf.doc.rsfpar('bool','y','','''If y, input is velocity; if n, slowness '''))
sfrays2.par('order',rsf.doc.rsfpar('int','4','','''Interpolation order '''))
sfrays2.par('nt',rsf.doc.rsfpar('int','','','''Number of time steps '''))
sfrays2.par('dt',rsf.doc.rsfpar('float','','','''Sampling in time '''))
sfrays2.par('sym',rsf.doc.rsfpar('bool','y','','''if y, use symplectic integrator '''))
sfrays2.par('verb',rsf.doc.rsfpar('bool','y','','''Verbosity flag '''))
sfrays2.par('escvar',rsf.doc.rsfpar('bool','n','','''If y - output escape values, n - trajectories '''))
sfrays2.par('zshot',rsf.doc.rsfpar('float','0.','','''shot coordinates (if no shotfile) '''))
sfrays2.par('yshot',rsf.doc.rsfpar('float','o[1] + 0.5*(n[1]-1)*d[1]','',''''''))
sfrays2.par('nr',rsf.doc.rsfpar('int','','','''number of angles (if no anglefile) '''))
sfrays2.par('a0',rsf.doc.rsfpar('float','0.','','''minimum angle (if no anglefile) '''))
sfrays2.par('amax',rsf.doc.rsfpar('float','360.','','''maximum angle (if no anglefile) '''))
sfrays2.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfrays2.par('anglefile',rsf.doc.rsfpar('string ',desc='''file with initial angles (auxiliary input file name)'''))
sfrays2.version('2.1-git')
sfrays2.synopsis('''sfrays2 < vel.rsf > rays.rsf shotfile=shots.rsf anglefile=angles.rsf vel=y order=4 nt= dt= sym=y verb=y escvar=n zshot=0. yshot=o[1] + 0.5*(n[1]-1)*d[1] nr= a0=0. amax=360. > rays.rsf''','''Rays can be plotted with sfplotrays.
''')
rsf.doc.progs['sfrays2']=sfrays2

sfrays2a = rsf.doc.rsfprog('sfrays2a','system/seismic/Mrays2a.c','''Ray tracing in VTI media by a Runge-Kutta integrator.''')
sfrays2a.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays2a.par('anglefile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays2a.par('vel',rsf.doc.rsfpar('bool','y','','''If y, input is velocity; if n, slowness '''))
sfrays2a.par('order',rsf.doc.rsfpar('int','4','','''Interpolation order '''))
sfrays2a.par('nt',rsf.doc.rsfpar('int','','','''Number of time steps '''))
sfrays2a.par('dt',rsf.doc.rsfpar('float','','','''Sampling in time '''))
sfrays2a.par('verb',rsf.doc.rsfpar('bool','y','','''Verbosity flag '''))
sfrays2a.par('escvar',rsf.doc.rsfpar('bool','n','','''If y - output escape values, n - trajectories '''))
sfrays2a.par('zshot',rsf.doc.rsfpar('float','0.','','''shot coordinates (if no shotfile) '''))
sfrays2a.par('yshot',rsf.doc.rsfpar('float','o[1] + 0.5*(n[1]-1)*d[1]','',''''''))
sfrays2a.par('nr',rsf.doc.rsfpar('int','','','''number of angles (if no anglefile) '''))
sfrays2a.par('a0',rsf.doc.rsfpar('float','0.','','''minimum angle (if no anglefile) '''))
sfrays2a.par('amax',rsf.doc.rsfpar('float','360.','','''maximum angle (if no anglefile) '''))
sfrays2a.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfrays2a.par('anglefile',rsf.doc.rsfpar('string ',desc='''file with initial angles (auxiliary input file name)'''))
sfrays2a.par('vx',rsf.doc.rsfpar('string ',desc='''horizontal velocity or slowness '''))
sfrays2a.par('eta',rsf.doc.rsfpar('string ',desc='''eta parameter '''))
sfrays2a.version('2.1-git')
sfrays2a.synopsis('''sfrays2a < vz.rsf > rays.rsf shotfile=shots.rsf anglefile=angles.rsf vel=y order=4 nt= dt= verb=y escvar=n zshot=0. yshot=o[1] + 0.5*(n[1]-1)*d[1] nr= a0=0. amax=360. vx= eta= > rays.rsf''','''Rays can be plotted with sfplotrays.
''')
rsf.doc.progs['sfrays2a']=sfrays2a

sfrays3 = rsf.doc.rsfprog('sfrays3','system/seismic/Mrays3.c','''Ray tracing by a Runge-Kutta integrator in 3-D.''')
sfrays3.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays3.par('anglefile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrays3.par('vel',rsf.doc.rsfpar('bool','y','','''If y, input is velocity; if n, slowness '''))
sfrays3.par('order',rsf.doc.rsfpar('int','4','','''Interpolation order '''))
sfrays3.par('nt',rsf.doc.rsfpar('int','','','''Number of time steps '''))
sfrays3.par('dt',rsf.doc.rsfpar('float','','','''Sampling in time '''))
sfrays3.par('sym',rsf.doc.rsfpar('bool','y','','''if y, use symplectic integrator '''))
sfrays3.par('escvar',rsf.doc.rsfpar('bool','n','','''If y - output escape values, n - trajectories '''))
sfrays3.par('zshot',rsf.doc.rsfpar('float','o[0]','','''shot location in depth (if shotfile is not specified) '''))
sfrays3.par('yshot',rsf.doc.rsfpar('float','o[1] + 0.5*(n[1]-1)*d[1]','','''shot location inline (if shotfile is not specified) '''))
sfrays3.par('xshot',rsf.doc.rsfpar('float','o[2] + 0.5*(n[2]-1)*d[2]','','''shot location crossline (if shotfile is not specified) '''))
sfrays3.par('na',rsf.doc.rsfpar('int','','','''Number of azimuths (if anglefile is not specified) '''))
sfrays3.par('nb',rsf.doc.rsfpar('int','','','''Number of inclinations (if anglefile is not specified) '''))
sfrays3.par('a0',rsf.doc.rsfpar('float','0.','','''First azimuth angle in degrees (if anglefile is not specified) '''))
sfrays3.par('amax',rsf.doc.rsfpar('float','360.','','''Maximum azimuth angle in degrees (if anglefile is not specified) '''))
sfrays3.par('b0',rsf.doc.rsfpar('float','0.','','''First inclination angle in degrees (if anglefile is not specified) '''))
sfrays3.par('bmax',rsf.doc.rsfpar('float','180.','','''Maximum inclination angle in degrees (if anglefile is not specified) '''))
sfrays3.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfrays3.par('anglefile',rsf.doc.rsfpar('string ',desc='''file with initial angles (auxiliary input file name)'''))
sfrays3.version('2.1-git')
sfrays3.synopsis('''sfrays3 < vel.rsf > rays.rsf shotfile=shots.rsf anglefile=angles.rsf vel=y order=4 nt= dt= sym=y escvar=n zshot=o[0] yshot=o[1] + 0.5*(n[1]-1)*d[1] xshot=o[2] + 0.5*(n[2]-1)*d[2] na= nb= a0=0. amax=360. b0=0. bmax=180. > rays.rsf''','''Rays can be plotted with sfplotrays.
''')
rsf.doc.progs['sfrays3']=sfrays3

sfrefer = rsf.doc.rsfprog('sfrefer','system/seismic/Mrefer.c','''Subtract a reference from a grid. ''')
sfrefer.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrefer.version('2.1-git')
sfrefer.synopsis('''sfrefer < in.rsf > out.rsf ref=ref.rsf''','''''')
rsf.doc.progs['sfrefer']=sfrefer

sfrefl2ai = rsf.doc.rsfprog('sfrefl2ai','system/seismic/Mrefl2ai.c','''Convert reflectivity to acoustic impedance. ''')
sfrefl2ai.par('a0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrefl2ai.version('2.1-git')
sfrefl2ai.synopsis('''sfrefl2ai < ref.rsf > ai.rsf a0=a0.rsf''','''''')
rsf.doc.progs['sfrefl2ai']=sfrefl2ai

sfricker = rsf.doc.rsfprog('sfricker','system/seismic/Mricker.c','''Ricker wavelet estimation. ''')
sfricker.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfricker.par('m',rsf.doc.rsfpar('float','f0+0.25*(na-1)*df','','''initial frequency '''))
sfricker.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfricker.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfricker.version('2.1-git')
sfricker.synopsis('''sfricker < in.rsf > out.rsf ma=ma.rsf m=f0+0.25*(na-1)*df niter=100 verb=n''','''''')
rsf.doc.progs['sfricker']=sfricker

sfricker1 = rsf.doc.rsfprog('sfricker1','system/seismic/Mricker1.c','''Convolution with a Ricker wavelet. ''')
sfricker1.par('frequency',rsf.doc.rsfpar('float','','','''peak frequency for Ricker wavelet (in Hz) '''))
sfricker1.par('freq',rsf.doc.rsfpar('float','0.2','','''peak frequency for Ricker wavelet (as fraction of Nyquist) '''))
sfricker1.par('deriv',rsf.doc.rsfpar('bool','n','','''apply a half-order derivative filter '''))
sfricker1.version('2.1-git')
sfricker1.synopsis('''sfricker1 < in.rsf > out.rsf frequency= freq=0.2 deriv=n''','''
January 2013 program of the month:
http://ahay.org/blog/2013/01/08/program-of-the-month-sfricker1/
''')
rsf.doc.progs['sfricker1']=sfricker1

sfricker2 = rsf.doc.rsfprog('sfricker2','system/seismic/Mricker2.c','''Nonstationary convolution with a Ricker wavelet. Phase and Frequency can be time-varying. ''')
sfricker2.par('tfreq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfricker2.par('tphase',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfricker2.par('frequency',rsf.doc.rsfpar('float','','','''peak frequency for Ricker wavelet (in Hz) '''))
sfricker2.par('freq',rsf.doc.rsfpar('float','0.2','','''peak frequency for Ricker wavelet (as fraction of Nyquist) '''))
sfricker2.par('esp',rsf.doc.rsfpar('float','0.','','''if norm=y, stable parameter'''))
sfricker2.par('norm',rsf.doc.rsfpar('bool','n','',''''''))
sfricker2.par('hiborder',rsf.doc.rsfpar('int','6','','''Hilbert transformer order '''))
sfricker2.par('hibref',rsf.doc.rsfpar('float','1.','',''''''))
sfricker2.par('tphase',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfricker2.version('2.1-git')
sfricker2.synopsis('''sfricker2 < in.rsf > out.rsf tfreq=tfre.rsf tphase=tpha.rsf frequency= freq=0.2 esp=0. norm=n hiborder=6 hibref=1.''','''''')
rsf.doc.progs['sfricker2']=sfricker2

sfrweab = rsf.doc.rsfprog('sfrweab','system/seismic/Mrweab.c','''Riemannian Wavefield Extrapolation: a,b coefficients ''')
sfrweab.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrweab.par('abr',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrweab.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrweab.par('naref',rsf.doc.rsfpar('int','1','',''''''))
sfrweab.par('nbref',rsf.doc.rsfpar('int','1','',''''''))
sfrweab.par('peps',rsf.doc.rsfpar('float','0.01','',''''''))
sfrweab.version('2.1-git')
sfrweab.synopsis('''sfrweab < Fi.rsf slo=Fs.rsf > Fo.rsf abr=Fr.rsf verb=n naref=1 nbref=1 peps=0.01''','''''')
rsf.doc.progs['sfrweab']=sfrweab

sfrwesrmig = rsf.doc.rsfprog('sfrwesrmig','system/seismic/Mrwesrmig.c','''Riemannian Wavefield Extrapolation: shot-record migration. ''')
sfrwesrmig.par('abm',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwesrmig.par('abr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwesrmig.par('img',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwesrmig.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrwesrmig.par('method',rsf.doc.rsfpar('int','0','','''extrapolation method '''))
sfrwesrmig.par('adj',rsf.doc.rsfpar('bool','n','','''y=modeling; n=migration '''))
sfrwesrmig.version('2.1-git')
sfrwesrmig.synopsis('''sfrwesrmig abm=Fm.rsf abr=Fr.rsf < Fw_s.rsf > Fw_r.rsf img=Fi.rsf verb=n method=0 adj=n''','''''')
rsf.doc.progs['sfrwesrmig']=sfrwesrmig

sfrwezomig = rsf.doc.rsfprog('sfrwezomig','system/seismic/Mrwezomig.c','''Riemannian Wavefield Extrapolation: zero-offset modeling/migration ''')
sfrwezomig.par('abm',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwezomig.par('abr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwezomig.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrwezomig.par('method',rsf.doc.rsfpar('int','0','','''extrapolation method '''))
sfrwezomig.par('adj',rsf.doc.rsfpar('bool','n','','''y=modeling; n=migration '''))
sfrwezomig.par('nw',rsf.doc.rsfpar('int','','',''''''))
sfrwezomig.par('dw',rsf.doc.rsfpar('float','','',''''''))
sfrwezomig.par('ow',rsf.doc.rsfpar('float','0.','',''''''))
sfrwezomig.version('2.1-git')
sfrwezomig.synopsis('''sfrwezomig abm=Fm.rsf abr=Fr.rsf < Fi.rsf > Fd.rsf verb=n method=0 adj=n nw= dw= ow=0.''','''''')
rsf.doc.progs['sfrwezomig']=sfrwezomig

sfs2ofz = rsf.doc.rsfprog('sfs2ofz','system/seismic/Ms2ofz.c','''Analytical point-source traveltime in a linear slowness squared model. ''')
sfs2ofz.par('n',rsf.doc.rsfpar('int','','','''number of samples '''))
sfs2ofz.par('g',rsf.doc.rsfpar('float','-6.','','''slowness squared gradient '''))
sfs2ofz.par('v0',rsf.doc.rsfpar('float','4','','''initial slowness squared '''))
sfs2ofz.par('s',rsf.doc.rsfpar('float','0.5','','''shot location at the surface '''))
sfs2ofz.version('2.1-git')
sfs2ofz.synopsis('''sfs2ofz > out.rsf n= g=-6. v0=4 s=0.5''','''''')
rsf.doc.progs['sfs2ofz']=sfs2ofz

sfs2ofz2 = rsf.doc.rsfprog('sfs2ofz2','system/seismic/Ms2ofz2.c','''Analytical plane-wave traveltime in a linear slowness squared model. ''')
sfs2ofz2.par('n',rsf.doc.rsfpar('int','','','''number of samples '''))
sfs2ofz2.par('gz',rsf.doc.rsfpar('float','-6.','',''''''))
sfs2ofz2.par('gx',rsf.doc.rsfpar('float','2.','','''slowness squared gradient '''))
sfs2ofz2.par('v0',rsf.doc.rsfpar('float','4','','''initial slowness squared '''))
sfs2ofz2.version('2.1-git')
sfs2ofz2.synopsis('''sfs2ofz2 > out.rsf n= gz=-6. gx=2. v0=4''','''''')
rsf.doc.progs['sfs2ofz2']=sfs2ofz2

sfsegyheader = rsf.doc.rsfprog('sfsegyheader','system/seismic/Msegyheader.c','''Make a trace header file for segywrite.''')
sfsegyheader.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegyheader.par('n1',rsf.doc.rsfpar('int','','','''number of samples in a trace '''))
sfsegyheader.par('d1',rsf.doc.rsfpar('float','','','''trace sampling '''))
sfsegyheader.par('o1',rsf.doc.rsfpar('float','0','','''trace origin '''))
sfsegyheader.par('tfile',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsegyheader.version('2.1-git')
sfsegyheader.synopsis('''sfsegyheader < in.rsf > out.rsf tfile=tfile.rsf n1= d1= o1=0''','''
Use the output for tfile= argument in segywrite.
''')
rsf.doc.progs['sfsegyheader']=sfsegyheader

sfsegyread = rsf.doc.rsfprog('sfsegyread','system/seismic/Msegyread.c','''Convert a SEG-Y or SU dataset to RSF.''')
sfsegyread.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegyread.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsegyread.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfsegyread.par('su',rsf.doc.rsfpar('bool','','','''y if input is SU, n if input is SEGY '''))
sfsegyread.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support.  
           SU with xdr on (as downloaded), use endian=y suxdr=y
           SU with xdr off in the makefiles, use endian=n suxdr=n   
        '''))
sfsegyread.par('endian',rsf.doc.rsfpar('bool','y','','''Whether to automatically estimate endianness or not '''))
sfsegyread.par('n2',rsf.doc.rsfpar('int','0','','''number of traces to read (if 0, read all traces) '''))
sfsegyread.par('format',rsf.doc.rsfpar('int','','[1,2,3,5]','''Data format. 
           The default is taken from binary header for segy input.
	   Default is 5 for su input.
	   1 is IBM floating point
	   2 is 4-byte integer
	   3 is 2-byte integer
	   5 is IEEE floating point
           6 is native_float (same as RSF binary default)
	'''))
sfsegyread.par('ns',rsf.doc.rsfpar('int','0','','''Number of samples. The default is taken from binary header '''))
sfsegyread.par('tape',rsf.doc.rsfpar('string ',desc='''input data '''))
sfsegyread.par('hfile',rsf.doc.rsfpar('string ',desc='''output text data header file '''))
sfsegyread.par('bfile',rsf.doc.rsfpar('string ',desc='''output binary data header file '''))
sfsegyread.par('mask',rsf.doc.rsfpar('string ',desc='''optional header mask for reading only selected traces (auxiliary input file name)'''))
sfsegyread.par('read',rsf.doc.rsfpar('string ',desc='''what to read: h - header, d - data, b - both (default) '''))
sfsegyread.par('tfile',rsf.doc.rsfpar('string ',desc='''output trace header file (auxiliary output file name)'''))
sfsegyread.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsegyread')
sfsegyread.version('2.1-git')
sfsegyread.synopsis('''sfsegyread mask=msk.rsf > out.rsf tfile=hdr.rsf verb=n su= suxdr=n endian=y n2=0 format= ns=0 tape= hfile= bfile= read=''','''
Data headers and trace headers are separated from the data.

"suread" is equivalent to "segyread su=y"


SEGY key names:

tracl: trace sequence number within line 0

tracr: trace sequence number within reel 4

fldr:     field record number 8 

tracf:    trace number within field record 12 

ep:       energy source point number 16 

cdp:      CDP ensemble number 20 

cdpt:     trace number within CDP ensemble 24 

trid:     trace identification code:
1 = seismic data
2 = dead
3 = dummy
4 = time break
5 = uphole
6 = sweep
7 = timing
8 = water break
9---, N = optional use (N = 32,767) 28 

nvs:      number of vertically summed traces 30 

nhs:      number of horizontally summed traces 32 

duse:     data use:
1 = production
2 = test 34

offset:   distance from source point to receiver
group (negative if opposite to direction
in which the line was shot) 36 

gelev:    receiver group elevation from sea level
(above sea level is positive) 40 

selev:    source elevation from sea level
(above sea level is positive) 44 

sdepth:   source depth (positive) 48 

gdel:     datum elevation at receiver group 52 

sdel:     datum elevation at source 56 

swdep:    water depth at source 60 

gwdep:    water depth at receiver group 64 

scalel:   scale factor for previous 7 entries
with value plus or minus 10 to the
power 0, 1, 2, 3, or 4 (if positive,
multiply, if negative divide) 68 

scalco:   scale factor for next 4 entries
with value plus or minus 10 to the
power 0, 1, 2, 3, or 4 (if positive,
multiply, if negative divide) 70 

sx:       X source coordinate 72 

sy:       Y source coordinate 76 

gx:       X group coordinate 80 

gy:       Y group coordinate 84 

counit:   coordinate units code:
for previous four entries
1 = length (meters or feet)
2 = seconds of arc (in this case, the
X values are unsigned longitude and the Y values
are latitude, a positive value designates
the number of seconds east of Greenwich
or north of the equator 88 

wevel:     weathering velocity 90 

swevel:    subweathering velocity 92 

sut:       uphole time at source 94 

gut:       uphole time at receiver group 96 

sstat:     source static correction 98 

gstat:     group static correction 100 

tstat:     total static applied 102 

laga:      lag time A, time in ms between end of 240-
byte trace identification header and time
break, positive if time break occurs after
end of header, time break is defined as
the initiation pulse which maybe recorded
on an auxiliary trace or as otherwise
specified by the recording system 104 

lagb:      lag time B, time in ms between the time
break and the initiation time of the energy source,
may be positive or negative 106 

delrt:     delay recording time, time in ms between
initiation time of energy source and time
when recording of data samples begins
(for deep water work if recording does not
start at zero time) 108 

muts:      mute time--start 110 

mute:      mute time--end 112 

ns:        number of samples in this trace 114 

dt:        sample interval, in micro-seconds 116 

gain:      gain type of field instruments code:
1 = fixed
2 = binary
3 = floating point
4 ---- N = optional use 118 

igc:       instrument gain constant 120 

igi:       instrument early or initial gain 122 

corr:      correlated:
1 = no
2 = yes 124

sfs:       sweep frequency at start 126 

sfe:       sweep frequency at end 128 

slen:      sweep length in ms 130 

styp:      sweep type code:
1 = linear
2 = cos-squared
3 = other 132

stas:      sweep trace length at start in ms 134 

stae:      sweep trace length at end in ms 136 

tatyp:     taper type: 1=linear, 2=cos^2, 3=other 138 

afilf:     alias filter frequency if used 140 

afils:     alias filter slope 142 

nofilf:    notch filter frequency if used 144 

nofils:    notch filter slope 146 

lcf:       low cut frequency if used 148 

hcf:       high cut frequncy if used 150 

lcs:       low cut slope 152 

hcs:       high cut slope 154 

year:      year data recorded 156 

day:       day of year 158 

hour:      hour of day (24 hour clock) 160 

minute:    minute of hour 162 

sec:       second of minute 164 

timbas:    time basis code:
1 = local
2 = GMT
3 = other 166

trwf:      trace weighting factor, defined as 1/2^N
volts for the least sigificant bit 168 

grnors:    geophone group number of roll switch
position one 170

grnofr:    geophone group number of trace one within
original field record 172

grnlof:    geophone group number of last trace within
original field record 174

gaps:      gap size (total number of groups dropped) 176 

otrav:     overtravel taper code: 
1 = down (or behind)
2 = up (or ahead) 178

cdpx:   X coordinate of CDP 180

cdpy:   Y coordinate of CDP 184

iline:  in-line number 188 

xline:  cross-line number 192

shnum:  shotpoint number 196

shsca:  shotpoint scalar 200

tval:   trace value meas. 202

tconst4: transduction const 204

tconst2: transduction const 208

tunits:  transduction units 210

device:  device identifier 212

tscalar: time scalar 214

stype:   source type 216

sendir:  source energy dir. 218

unknown: unknown 222

smeas4:  source measurement 224

smeas2:  source measurement 228

smeasu:  source measurement unit 230 

unass1:  unassigned 232

unass2:  unassigned 236

additional keys can be created in the output trace headers
The parameters key1, key2, ... key# are used to additional keys.   
The keys must be unique and different from the SEGY key names above.
The input header byte location and lengths must also be defined.  
This capability is described in an example that defines a new keys 
iline1 from byte 220 and xline1 from byte 224:
	  key1=iline1 iline1=220 key1_len=4 \\ 
key2=xline1 xline1=224 key2_len=4 \\

key#_len defaults to 4
''')
rsf.doc.progs['sfsegyread']=sfsegyread

sfsegywrite = rsf.doc.rsfprog('sfsegywrite','system/seismic/Msegywrite.c','''Convert an RSF dataset to SEGY or SU.''')
sfsegywrite.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegywrite.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfsegywrite.par('endian',rsf.doc.rsfpar('bool','y','','''Whether to automatically estimate endianness or not '''))
sfsegywrite.par('su',rsf.doc.rsfpar('bool','','','''y if input is SU, n if input is SEGY '''))
sfsegywrite.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support '''))
sfsegywrite.par('suxdr',rsf.doc.rsfpar('bool','n','','''y, SU has XDR support '''))
sfsegywrite.par('tape',rsf.doc.rsfpar('string ',desc='''output data '''))
sfsegywrite.par('hfile',rsf.doc.rsfpar('string ',desc='''input text data header file '''))
sfsegywrite.par('bfile',rsf.doc.rsfpar('string ',desc='''input binary data header file '''))
sfsegywrite.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfsegywrite')
sfsegywrite.version('2.1-git')
sfsegywrite.synopsis('''sfsegywrite < in.rsf tfile=hdr.rsf verb=n endian=y su= suxdr=n suxdr=n tape= hfile= bfile=''','''
Merges trace headers with data.

"suwrite" is equivalent to "segywrite su=y"

If bfile= and/or hfile= are not provided, they will be created automatically
using information from the trace headers.

The file for tfile= can be generated with sfsegyheader.
''')
rsf.doc.progs['sfsegywrite']=sfsegywrite

sfshifts = rsf.doc.rsfprog('sfshifts','system/seismic/Mshifts.c','''Multiple shifts. ''')
sfshifts.par('np',rsf.doc.rsfpar('int','','','''number of slopes '''))
sfshifts.par('dp',rsf.doc.rsfpar('float','','','''slope sampling '''))
sfshifts.par('p0',rsf.doc.rsfpar('float','','','''first slope '''))
sfshifts.version('2.1-git')
sfshifts.synopsis('''sfshifts < inp.rsf > out.rsf np= dp= p0=''','''''')
rsf.doc.progs['sfshifts']=sfshifts

sfshoot2 = rsf.doc.rsfprog('sfshoot2','system/seismic/Mshoot2.c','''2-D ray shooting. ''')
sfshoot2.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshoot2.par('vel',rsf.doc.rsfpar('bool','y','','''If y, the input is velocity; if n, slowness '''))
sfshoot2.par('order',rsf.doc.rsfpar('int','4','','''Interpolation order '''))
sfshoot2.par('lsint',rsf.doc.rsfpar('bool','n','','''if use least-squares interpolation '''))
sfshoot2.par('nt',rsf.doc.rsfpar('int','nx*nz','','''Maximum number of time steps '''))
sfshoot2.par('nr',rsf.doc.rsfpar('int','1','','''number of recievers '''))
sfshoot2.par('r0',rsf.doc.rsfpar('float','x0','','''first receiver '''))
sfshoot2.par('dr',rsf.doc.rsfpar('float','dx','','''receiver increment '''))
sfshoot2.par('tol',rsf.doc.rsfpar('float','0.01','','''Shooting tolerance (in degrees) '''))
sfshoot2.par('shotfile',rsf.doc.rsfpar('string ',desc='''file with shot locations (auxiliary input file name)'''))
sfshoot2.version('2.1-git')
sfshoot2.synopsis('''sfshoot2 < vel.rsf > out.rsf shotfile=shots.rsf vel=y order=4 lsint=n nt=nx*nz nr=1 r0=x0 dr=dx tol=0.01''','''''')
rsf.doc.progs['sfshoot2']=sfshoot2

sfshot2cmp = rsf.doc.rsfprog('sfshot2cmp','system/seismic/Mshot2cmp.c','''Convert shots to CMPs for regular 2-D geometry. ''')
sfshot2cmp.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshot2cmp.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfshot2cmp.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset'''))
sfshot2cmp.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfshot2cmp.version('2.1-git')
sfshot2cmp.synopsis('''sfshot2cmp < in.rsf > out.rsf mask=msk.rsf positive=y half=y''','''
The axes in the input are {time,offset,shot}
The axes in the output are {time,offset,midpoint}
''')
rsf.doc.progs['sfshot2cmp']=sfshot2cmp

sfshotconstkirch = rsf.doc.rsfprog('sfshotconstkirch','system/seismic/Mshotconstkirch.c','''Prestack shot-profile Kirchhoff migration in constant velocity. ''')
sfshotconstkirch.par('aal',rsf.doc.rsfpar('bool','y','','''if y, apply antialiasing '''))
sfshotconstkirch.par('nx',rsf.doc.rsfpar('int','ns','',''''''))
sfshotconstkirch.par('dx',rsf.doc.rsfpar('float','ds','',''''''))
sfshotconstkirch.par('x0',rsf.doc.rsfpar('float','s0','',''''''))
sfshotconstkirch.par('offset',rsf.doc.rsfpar('bool','n','','''if y, the output is in offset '''))
sfshotconstkirch.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfshotconstkirch.version('2.1-git')
sfshotconstkirch.synopsis('''sfshotconstkirch < inp.rsf > out.rsf aal=y nx=ns dx=ds x0=s0 offset=n vel=''','''
Requires the input to be in (time,offset,shot)
''')
rsf.doc.progs['sfshotconstkirch']=sfshotconstkirch

sfshotholes = rsf.doc.rsfprog('sfshotholes','system/seismic/Mshotholes.c','''Remove random shot gathers from a 2-D dataset. ''')
sfshotholes.par('perc',rsf.doc.rsfpar('float','0.75','','''how many shots to remove '''))
sfshotholes.version('2.1-git')
sfshotholes.synopsis('''sfshotholes < in.rsf > mask.rsf perc=0.75''','''''')
rsf.doc.progs['sfshotholes']=sfshotholes

sfshotprop = rsf.doc.rsfprog('sfshotprop','system/seismic/Mshotprop.c','''Shot propagation. ''')
sfshotprop.par('ns',rsf.doc.rsfpar('int','','','''number of shots '''))
sfshotprop.par('ds',rsf.doc.rsfpar('float','','','''shot sampling '''))
sfshotprop.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sfshotprop.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfshotprop.version('2.1-git')
sfshotprop.synopsis('''sfshotprop < in.rsf > out.rsf ns= ds= eps=0.1 positive=y''','''''')
rsf.doc.progs['sfshotprop']=sfshotprop

sfsimivscan = rsf.doc.rsfprog('sfsimivscan','system/seismic/Msimivscan.c','''Velocity analysis using similarity-weighted semblance.''')
sfsimivscan.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimivscan.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimivscan.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimivscan.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimivscan.par('semblance',rsf.doc.rsfpar('bool','n','','''if y, compute semblance; if n, stack '''))
sfsimivscan.par('diffsemblance',rsf.doc.rsfpar('bool','n','','''if y, compute differential semblance '''))
sfsimivscan.par('avosemblance',rsf.doc.rsfpar('bool','n','','''if y, compute AVO-friendly semblance '''))
sfsimivscan.par('nb',rsf.doc.rsfpar('int','2','','''semblance averaging '''))
sfsimivscan.par('weight',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfsimivscan.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfsimivscan.par('smax',rsf.doc.rsfpar('float','2.0','','''maximum heterogeneity '''))
sfsimivscan.par('ns',rsf.doc.rsfpar('int','1','','''number of heterogeneity scans '''))
sfsimivscan.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfsimivscan.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfsimivscan.par('v1',rsf.doc.rsfpar('float','','','''( v1 reference velocity )'''))
sfsimivscan.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfsimivscan.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfsimivscan.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfsimivscan.par('thr',rsf.doc.rsfpar('float','0.3','',''''''))
sfsimivscan.par('eps',rsf.doc.rsfpar('float','0.01','',''''''))
sfsimivscan.par('niter',rsf.doc.rsfpar('int','10','',''''''))
sfsimivscan.par('v0',rsf.doc.rsfpar('float','','','''first scanned velocity '''))
sfsimivscan.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sfsimivscan.par('nv',rsf.doc.rsfpar('int','','','''number of scanned velocities '''))
sfsimivscan.par('v1',rsf.doc.rsfpar('float','','','''reference velocity '''))
sfsimivscan.par('type',rsf.doc.rsfpar('string ',desc='''type of semblance (avo,diff,sembl,power,weighted) '''))
sfsimivscan.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsimivscan.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file (auxiliary input file name)'''))
sfsimivscan.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsimivscan.version('2.1-git')
sfsimivscan.synopsis('''sfsimivscan < cmp.rsf > scan.rsf ref=ref.rsf offset=offset.rsf mask=msk.rsf grad=grd.rsf semblance=n diffsemblance=n avosemblance=n nb=2 weight=y half=y smax=2.0 ns=1 slowness=n squared=n v1= extend=4 mute=12 str=0.5 thr=0.3 eps=0.01 niter=10 v0= dv= nv= v1= type=''','''''')
rsf.doc.progs['sfsimivscan']=sfsimivscan

sfsin = rsf.doc.rsfprog('sfsin','system/seismic/Msin.c','''Simple operations with complex sinusoids ''')
sfsin.par('root',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsin.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsin.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfsin.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfsin.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfsin.par('rect',rsf.doc.rsfpar('int','1','','''smoothing radius (for oper=s) '''))
sfsin.par('perc',rsf.doc.rsfpar('float','50.','','''percentage for thresholding (used when oper=t and niter > 0) '''))
sfsin.par('eps',rsf.doc.rsfpar('float','1./n1','','''scaling for shaping inversion '''))
sfsin.par('oper',rsf.doc.rsfpar('string ',desc='''operation to perform '''))
sfsin.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biortho] type of the seislet transform '''))
sfsin.par('mask',rsf.doc.rsfpar('string ',desc='''missing data interpolation (auxiliary input file name)'''))
sfsin.version('2.1-git')
sfsin.synopsis('''sfsin < in.rsf > out.rsf root=root.rsf mask=mask.rsf adj=n verb=n niter=0 rect=1 perc=50. eps=1./n1 oper= type=''','''''')
rsf.doc.progs['sfsin']=sfsin

sfslant = rsf.doc.rsfprog('sfslant','system/seismic/Mslant.c','''Time-space-domain Radon transform (slant stack) ''')
sfslant.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfslant.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfslant.par('rho',rsf.doc.rsfpar('bool','y','','''rho filtering '''))
sfslant.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfslant.par('np',rsf.doc.rsfpar('int','','','''number of p values (if adj=y) '''))
sfslant.par('dp',rsf.doc.rsfpar('float','','','''p sampling (if adj=y) '''))
sfslant.par('p0',rsf.doc.rsfpar('float','','','''p origin (if adj=y) '''))
sfslant.par('x0',rsf.doc.rsfpar('float','','','''offset origin '''))
sfslant.par('dx',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfslant.par('nx',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfslant.par('p1',rsf.doc.rsfpar('float','0.','','''reference slope '''))
sfslant.version('2.1-git')
sfslant.synopsis('''sfslant < in.rsf > out.rsf verb=n adj=n rho=y anti=1. np= dp= p0= x0= dx= nx= p1=0.''','''
April 2015 program of the month:
http://ahay.org/blog/2015/04/21/program-of-the-month-sfslant/
''')
rsf.doc.progs['sfslant']=sfslant

sfsrmva = rsf.doc.rsfprog('sfsrmva','system/seismic/Msrmva.c','''3-D S/R WEMVA with extended split-step ''')
sfsrmva.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsrmva.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsrmva.par('rwf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsrmva.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfsrmva.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfsrmva.par('adj',rsf.doc.rsfpar('bool','n','','''y=ADJ scat; n=FWD scat '''))
sfsrmva.par('twoway',rsf.doc.rsfpar('bool','y','','''two-way traveltime '''))
sfsrmva.par('nrmax',rsf.doc.rsfpar('int','1','','''max number of refs '''))
sfsrmva.par('dtmax',rsf.doc.rsfpar('float','0.004','','''max time error '''))
sfsrmva.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfsrmva.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y '''))
sfsrmva.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x   '''))
sfsrmva.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y   '''))
sfsrmva.version('2.1-git')
sfsrmva.synopsis('''sfsrmva slo=Bs.rsf swf=Bw_s.rsf rwf=Bw_r.rsf < Pi.rsf > Ps.rsf verb=y eps=0.01 adj=n twoway=y nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0''','''''')
rsf.doc.progs['sfsrmva']=sfsrmva

sfsrseidel = rsf.doc.rsfprog('sfsrseidel','system/seismic/Msrseidel.c','''Amplitude balancing of a 2-D amplitude map. ''')
sfsrseidel.par('src',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrseidel.par('mid',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrseidel.par('rcv',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrseidel.par('so',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrseidel.par('rv',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrseidel.par('niter',rsf.doc.rsfpar('int','1 ','','''number of iterations '''))
sfsrseidel.version('2.1-git')
sfsrseidel.synopsis('''sfsrseidel < in.rsf > off.rsf src=src.rsf mid=mid.rsf rcv=rcv.rsf so=so.rsf rv=rv.rsf niter=1 ''','''''')
rsf.doc.progs['sfsrseidel']=sfsrseidel

sfsrsyn = rsf.doc.rsfprog('sfsrsyn','system/seismic/Msrsyn.c','''Synthesize shot/receiver wavefields for 3-D SR migration ''')
sfsrsyn.par('wav',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsrsyn.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrsyn.par('nx',rsf.doc.rsfpar('int','','','''x samples '''))
sfsrsyn.par('dx',rsf.doc.rsfpar('float','','','''x sampling '''))
sfsrsyn.par('ox',rsf.doc.rsfpar('float','','','''x origin '''))
sfsrsyn.par('ny',rsf.doc.rsfpar('int','1','','''y samples '''))
sfsrsyn.par('dy',rsf.doc.rsfpar('float','1','','''y sampling '''))
sfsrsyn.par('oy',rsf.doc.rsfpar('float','0','','''y origin '''))
sfsrsyn.version('2.1-git')
sfsrsyn.synopsis('''sfsrsyn < Fr.rsf wav=Fs.rsf swf=Fsw.rsf > Frw.rsf nx= dx= ox= ny=1 dy=1 oy=0''','''''')
rsf.doc.progs['sfsrsyn']=sfsrsyn

sfsstep2 = rsf.doc.rsfprog('sfsstep2','system/seismic/Msstep2.c','''3-D post-stack modeling/migration with extended split step. ''')
sfsstep2.par('slowness',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsstep2.par('inv',rsf.doc.rsfpar('bool','n','','''If y, modeling; if n, migration '''))
sfsstep2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfsstep2.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfsstep2.par('nt',rsf.doc.rsfpar('int','1','','''taper size '''))
sfsstep2.par('nr',rsf.doc.rsfpar('int','1','','''maximum number of references '''))
sfsstep2.par('padx',rsf.doc.rsfpar('int','0','','''cross-line padding '''))
sfsstep2.par('pady',rsf.doc.rsfpar('int','0','','''in-line padding '''))
sfsstep2.par('dt',rsf.doc.rsfpar('float','0.004','','''time error '''))
sfsstep2.par('nw',rsf.doc.rsfpar('int','','','''Length of frequency axis (for modeling) '''))
sfsstep2.par('dw',rsf.doc.rsfpar('float','','','''Frequency sampling (for modeling) '''))
sfsstep2.par('w0',rsf.doc.rsfpar('float','0.','','''Frequency origin (for modeling) '''))
sfsstep2.version('2.1-git')
sfsstep2.synopsis('''sfsstep2 < in.rsf > out.rsf slowness=vel.rsf inv=n verb=n eps=0.01 nt=1 nr=1 padx=0 pady=0 dt=0.004 nw= dw= w0=0.''','''''')
rsf.doc.progs['sfsstep2']=sfsstep2

sfstacks = rsf.doc.rsfprog('sfstacks','system/seismic/Mstacks.c','''Constant-velocity stacks. ''')
sfstacks.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstacks.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstacks.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfstacks.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfstacks.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfstacks.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfstacks.par('v0',rsf.doc.rsfpar('float','','','''first velocity '''))
sfstacks.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sfstacks.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfstacks.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfstacks.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfstacks.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfstacks.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfstacks.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfstacks.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfstacks.version('2.1-git')
sfstacks.synopsis('''sfstacks < cmp.rsf > stk.rsf offset=offset.rsf mask=msk.rsf half=y str=0.5 mute=12 nv= v0= dv= CDPtype= slowness=n squared=n h0=0. extend=4''','''''')
rsf.doc.progs['sfstacks']=sfstacks

sfstolt = rsf.doc.rsfprog('sfstolt','system/seismic/Mstolt.c','''Post-stack Stolt modeling/migration. ''')
sfstolt.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (use negative velocity for modeling) '''))
sfstolt.par('pad',rsf.doc.rsfpar('int','nt','','''padding on the time axis '''))
sfstolt.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfstolt.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfstolt.par('minstr',rsf.doc.rsfpar('float','0.0','','''minimum stretch allowed '''))
sfstolt.par('stretch',rsf.doc.rsfpar('float','1','','''Stolt stretch parameter '''))
sfstolt.version('2.1-git')
sfstolt.synopsis('''sfstolt < in.rsf > out.rsf vel= pad=nt extend=4 mute=12 minstr=0.0 stretch=1''','''
Requires the input to be cosine-transformed over the lateral axes.

August 2014 program of the month:
http://ahay.org/blog/2014/08/03/program-of-the-month-sfstolt/
''')
rsf.doc.progs['sfstolt']=sfstolt

sfstolt2 = rsf.doc.rsfprog('sfstolt2','system/seismic/Mstolt2.c','''Post-stack Stolt modeling/migration. ''')
sfstolt2.par('vel',rsf.doc.rsfpar('float','','','''Constant velocity (use negative velocity for modeling) '''))
sfstolt2.par('pad',rsf.doc.rsfpar('int','nt','','''padding on the time axis '''))
sfstolt2.par('nf',rsf.doc.rsfpar('int','2','','''Interpolation accuracy '''))
sfstolt2.version('2.1-git')
sfstolt2.synopsis('''sfstolt2 < in.rsf > out.rsf vel= pad=nt nf=2''','''
Requires the input to be cosine-transformed over the lateral axes.
''')
rsf.doc.progs['sfstolt2']=sfstolt2

sfstoltstretch = rsf.doc.rsfprog('sfstoltstretch','system/seismic/Mstoltstretch.c','''Stolt stretch. ''')
sfstoltstretch.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstoltstretch.par('inv',rsf.doc.rsfpar('bool','n','','''if y, inverse stretch '''))
sfstoltstretch.par('nstretch',rsf.doc.rsfpar('int','1','','''number of steps '''))
sfstoltstretch.par('pad',rsf.doc.rsfpar('int','nt','','''time axis padding '''))
sfstoltstretch.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfstoltstretch.par('vel',rsf.doc.rsfpar('float','','','''reference velocity '''))
sfstoltstretch.version('2.1-git')
sfstoltstretch.synopsis('''sfstoltstretch < in.rsf > st.rsf velocity=vel.rsf inv=n nstretch=1 pad=nt eps=0.01 vel=''','''''')
rsf.doc.progs['sfstoltstretch']=sfstoltstretch

sfstretch = rsf.doc.rsfprog('sfstretch','system/seismic/Mstretch.c','''Stretch of the time axis. ''')
sfstretch.par('datum',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstretch.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse stretching '''))
sfstretch.par('dens',rsf.doc.rsfpar('int','1','','''axis stretching factor '''))
sfstretch.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfstretch.par('v0',rsf.doc.rsfpar('float','','','''moveout velocity '''))
sfstretch.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfstretch.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfstretch.par('delay',rsf.doc.rsfpar('float','','','''time delay for rule=lmo '''))
sfstretch.par('tdelay',rsf.doc.rsfpar('float','','','''time delay for rule=rad '''))
sfstretch.par('hdelay',rsf.doc.rsfpar('float','','','''offset delay for rule=rad '''))
sfstretch.par('scale',rsf.doc.rsfpar('float','','','''scaling factor for rule=scale '''))
sfstretch.par('nout',rsf.doc.rsfpar('int','dens*n1','','''output axis length (if inv=n) '''))
sfstretch.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfstretch.par('mute',rsf.doc.rsfpar('int','0','','''tapering size '''))
sfstretch.par('maxstr',rsf.doc.rsfpar('float','0','','''maximum stretch '''))
sfstretch.par('rule',rsf.doc.rsfpar('string ',desc='''Stretch rule:
	   n - constant-velocity normal moveout (nmostretch), default
	   l - linear moveout (lmostretch)
	   L - logarithmic stretch (logstretch)
	   2 - t^2 stretch (t2stretch)
	   c - t^2 chebyshev stretch (t2chebstretch)
	   r - radial moveout (radstretch)
	   d - datuming (datstretch)
	   s - s*t scaling stretch (scalestretch)
	'''))
sfstretch.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfstretch')
sfstretch.version('2.1-git')
sfstretch.synopsis('''sfstretch < in.rsf > out.rsf datum=dat.rsf inv=n dens=1 verb=y v0= half=y CDPtype= delay= tdelay= hdelay= scale= nout=dens*n1 extend=4 mute=0 maxstr=0 rule=''','''''')
rsf.doc.progs['sfstretch']=sfstretch

sfstripes = rsf.doc.rsfprog('sfstripes','system/seismic/Mstripes.c','''Model the positions and dips of the constant offset, source, midpoint, and receiver strikes in a source vs. offset space. ''')
sfstripes.par('mo',rsf.doc.rsfpar('int','','','''offset parameter, a constant offset line will appear in the output every o offset '''))
sfstripes.par('ms',rsf.doc.rsfpar('int','','','''source parameter, a constant source line will appear in the output every s source '''))
sfstripes.par('my',rsf.doc.rsfpar('int','','','''midpoint parameter, a constant midpoint line will appear in the output every y midpoint '''))
sfstripes.par('mr',rsf.doc.rsfpar('int','','','''receiver parameter, a constant receiver line will appear in the output every r receiver '''))
sfstripes.version('2.1-git')
sfstripes.synopsis('''sfstripes < inp.rsf > out.rsf mo= ms= my= mr=''','''''')
rsf.doc.progs['sfstripes']=sfstripes

sftan2ang = rsf.doc.rsfprog('sftan2ang','system/seismic/Mtan2ang.c','''tangent to angle transformation ''')
sftan2ang.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftan2ang.par('na',rsf.doc.rsfpar('int','nt','',''''''))
sftan2ang.par('da',rsf.doc.rsfpar('float','90/(nt-1)','',''''''))
sftan2ang.par('a0',rsf.doc.rsfpar('float','0.','',''''''))
sftan2ang.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sftan2ang.par('top',rsf.doc.rsfpar('bool','n','',''''''))
sftan2ang.version('2.1-git')
sftan2ang.synopsis('''sftan2ang < Fstk.rsf > Fang.rsf velocity=velocity.rsf na=nt da=90/(nt-1) a0=0. extend=4 top=n''','''''')
rsf.doc.progs['sftan2ang']=sftan2ang

sftaupmo = rsf.doc.rsfprog('sftaupmo','system/seismic/Mtaupmo.c','''Normal moveout in tau-p domain. ''')
sftaupmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('slope',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('velx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupmo.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sftaupmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch '''))
sftaupmo.par('extend',rsf.doc.rsfpar('int','4','','''interpolation accuracy '''))
sftaupmo.par('interval',rsf.doc.rsfpar('bool','y','','''use interval velocity '''))
sftaupmo.par('slope',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftaupmo.par('velx',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftaupmo.version('2.1-git')
sftaupmo.synopsis('''sftaupmo < taup.rsf velocity=velocity.rsf > nmod.rsf slope=slope.rsf velx=velocityx.rsf mute=12 str=0.5 extend=4 interval=y''','''''')
rsf.doc.progs['sftaupmo']=sftaupmo

sftime2depth = rsf.doc.rsfprog('sftime2depth','system/seismic/Mtime2depth.c','''Time-to-depth conversion in V(z). ''')
sftime2depth.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftime2depth.par('intime',rsf.doc.rsfpar('bool','n','','''y if velocity is in time rather than depth '''))
sftime2depth.par('nz',rsf.doc.rsfpar('int','','','''Number of depth samples (default: n1) '''))
sftime2depth.par('dz',rsf.doc.rsfpar('float','','','''Depth sampling (default: d1) '''))
sftime2depth.par('z0',rsf.doc.rsfpar('float','0.','','''Depth origin '''))
sftime2depth.par('extend',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sftime2depth.par('slow',rsf.doc.rsfpar('bool','n','','''If y, input slowness; if n, velocity '''))
sftime2depth.par('twoway',rsf.doc.rsfpar('bool','y','','''if y, two-way traveltime '''))
sftime2depth.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sftime2depth.version('2.1-git')
sftime2depth.synopsis('''sftime2depth < in.rsf velocity=velocity.rsf > out.rsf intime=n nz= dz= z0=0. extend=4 slow=n twoway=y eps=0.01''','''
July 2013 program of the month:
http://www.ahay.org/blog/2013/07/01/program-of-the-month-sftime2depth/
''')
rsf.doc.progs['sftime2depth']=sftime2depth

sftlagtoang2d = rsf.doc.rsfprog('sftlagtoang2d','system/seismic/Mtlagtoang2d.c','''SS(t-lag) to angle transformation (PP or PS waves) ''')
sftlagtoang2d.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftlagtoang2d.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftlagtoang2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftlagtoang2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftlagtoang2d.par('inv',rsf.doc.rsfpar('bool','n','','''inverse transformation flag '''))
sftlagtoang2d.par('na',rsf.doc.rsfpar('int','sf_n(as)','',''''''))
sftlagtoang2d.par('da',rsf.doc.rsfpar('float','1./(sf_n(as)-1)','',''''''))
sftlagtoang2d.par('oa',rsf.doc.rsfpar('float','0.','',''''''))
sftlagtoang2d.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sftlagtoang2d.version('2.1-git')
sftlagtoang2d.synopsis('''sftlagtoang2d < Fstk.rsf > Fang.rsf vpvs=Fgam.rsf dip=Fdip.rsf vel=Fvel.rsf verb=n inv=n na=sf_n(as) da=1./(sf_n(as)-1) oa=0. extend=4''','''''')
rsf.doc.progs['sftlagtoang2d']=sftlagtoang2d

sftshift = rsf.doc.rsfprog('sftshift','system/seismic/Mtshift.c','''Compute angle gathers for time-shift imaging condition ''')
sftshift.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftshift.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftshift.par('na',rsf.doc.rsfpar('int','nv','',''''''))
sftshift.par('da',rsf.doc.rsfpar('float','1./(nv-1)','',''''''))
sftshift.par('a0',rsf.doc.rsfpar('float','0.','',''''''))
sftshift.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sftshift.par('cos',rsf.doc.rsfpar('bool','n','','''if n, convert pseudo-v to pseudo-tan(theta); 
       if y, compute cos(theta) from 1/|pm| '''))
sftshift.version('2.1-git')
sftshift.synopsis('''sftshift < Fstk.rsf velocity=Fvel.rsf dip=Fdip.rsf > Fang.rsf na=nv da=1./(nv-1) a0=0. extend=4 cos=n''','''''')
rsf.doc.progs['sftshift']=sftshift

sftxpscan = rsf.doc.rsfprog('sftxpscan','system/seismic/Mtxpscan.c','''Velocity analysis using T-X-P domain. ''')
sftxpscan.par('v0',rsf.doc.rsfpar('float','','','''first scanned velocity '''))
sftxpscan.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sftxpscan.par('nv',rsf.doc.rsfpar('int','','','''number of scanned velocities '''))
sftxpscan.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sftxpscan.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sftxpscan.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sftxpscan.par('smin',rsf.doc.rsfpar('float','1.0','','''minimum heterogeneity '''))
sftxpscan.par('smax',rsf.doc.rsfpar('float','2.0','','''maximum heterogeneity '''))
sftxpscan.version('2.1-git')
sftxpscan.synopsis('''sftxpscan < cmp.rsf > scan.rsf v0= dv= nv= extend=4 mute=12 str=0.5 smin=1.0 smax=2.0''','''''')
rsf.doc.progs['sftxpscan']=sftxpscan

sftxpnmo = rsf.doc.rsfprog('sftxpnmo','system/seismic/Mtxpnmo.c','''Normal moveout in TXP domain. ''')
sftxpnmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftxpnmo.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sftxpnmo.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sftxpnmo.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sftxpnmo.version('2.1-git')
sftxpnmo.synopsis('''sftxpnmo < cmp.rsf velocity=velocity.rsf > nmod.rsf str=0.5 mute=12 extend=4''','''''')
rsf.doc.progs['sftxpnmo']=sftxpnmo

sfvczo = rsf.doc.rsfprog('sfvczo','system/seismic/Mvczo.c','''Post-stack 2-D velocity continuation. ''')
sfvczo.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfvczo.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sfvczo.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfvczo.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfvczo.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfvczo.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfvczo.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfvczo.version('2.1-git')
sfvczo.synopsis('''sfvczo < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=y nv= dv= v0=''','''''')
rsf.doc.progs['sfvczo']=sfvczo

sfvczo2 = rsf.doc.rsfprog('sfvczo2','system/seismic/Mvczo2.c','''Post-stack 2-D velocity continuation in the time-stretch frequency domain. ''')
sfvczo2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfvczo2.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfvczo2.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfvczo2.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfvczo2.version('2.1-git')
sfvczo2.synopsis('''sfvczo2 < in.rsf > out.rsf verb=y nv= dv= v0=''','''''')
rsf.doc.progs['sfvczo2']=sfvczo2

sfvczo3 = rsf.doc.rsfprog('sfvczo3','system/seismic/Mvczo3.c','''Post-stack 3-D velocity continuation. ''')
sfvczo3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfvczo3.par('pad',rsf.doc.rsfpar('int','n1','','''padding for stretch '''))
sfvczo3.par('pad2',rsf.doc.rsfpar('int','2*kiss_fft_next_fast_size((n2+1)/2)','','''padding for FFT '''))
sfvczo3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfvczo3.par('nv',rsf.doc.rsfpar('int','','','''velocity steps '''))
sfvczo3.par('dv',rsf.doc.rsfpar('float','','','''velocity step size '''))
sfvczo3.par('v0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfvczo3.version('2.1-git')
sfvczo3.synopsis('''sfvczo3 < in.rsf > out.rsf eps=0.01 pad=n1 pad2=2*kiss_fft_next_fast_size((n2+1)/2) verb=y nv= dv= v0=''','''''')
rsf.doc.progs['sfvczo3']=sfvczo3

sfvelmod = rsf.doc.rsfprog('sfvelmod','system/seismic/Mvelmod.c','''Velocity transform.''')
sfvelmod.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfvelmod.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfvelmod.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfvelmod.version('2.1-git')
sfvelmod.synopsis('''sfvelmod < scan.rsf > cmp.rsf half=y extend=4 slowness=n''','''
Inverse of sfvscan.
''')
rsf.doc.progs['sfvelmod']=sfvelmod

sfveltran = rsf.doc.rsfprog('sfveltran','system/seismic/Mveltran.c','''Hyperbolic Radon transform ''')
sfveltran.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfveltran.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing '''))
sfveltran.par('s02',rsf.doc.rsfpar('float','0.','','''reference slowness squared (for antialiasing) '''))
sfveltran.par('pull',rsf.doc.rsfpar('bool','y','','''pull or push operator '''))
sfveltran.version('2.1-git')
sfveltran.synopsis('''sfveltran < in.rsf > out.rsf adj=n anti=1. s02=0. pull=y''','''''')
rsf.doc.progs['sfveltran']=sfveltran

sfvoft = rsf.doc.rsfprog('sfvoft','system/seismic/Mvoft.c','''V(t) function for a linear V(Z) profile.''')
sfvoft.par('v0',rsf.doc.rsfpar('float','1.5','','''initial velocity '''))
sfvoft.par('alpha',rsf.doc.rsfpar('float','0.5','','''velocity gradient '''))
sfvoft.version('2.1-git')
sfvoft.synopsis('''sfvoft < in.rsf > out.rsf v0=1.5 alpha=0.5''','''''')
rsf.doc.progs['sfvoft']=sfvoft

sfvofz = rsf.doc.rsfprog('sfvofz','system/seismic/Mvofz.c','''Analytical traveltime in a linear V(z) model. ''')
sfvofz.par('n1',rsf.doc.rsfpar('int','','','''vertical samples '''))
sfvofz.par('n',rsf.doc.rsfpar('int','','','''number of samples '''))
sfvofz.par('n2',rsf.doc.rsfpar('int','','','''horizontal samples '''))
sfvofz.par('n',rsf.doc.rsfpar('int','','','''number of samples '''))
sfvofz.par('g',rsf.doc.rsfpar('float','1.','','''velocity gradient '''))
sfvofz.par('v0',rsf.doc.rsfpar('float','0.5','','''initial velocity '''))
sfvofz.par('s',rsf.doc.rsfpar('float','0.5','','''shot location at the surface '''))
sfvofz.par('d1',rsf.doc.rsfpar('float','0.5/(n1-1)','','''vertical sampling '''))
sfvofz.par('d2',rsf.doc.rsfpar('float','1./(n2-1)','','''horizontal sampling '''))
sfvofz.par('o1',rsf.doc.rsfpar('float','0.','','''vertical origin '''))
sfvofz.par('o2',rsf.doc.rsfpar('float','0.','','''horizontal origin '''))
sfvofz.par('intime',rsf.doc.rsfpar('bool','n','','''if in vertical time coordinates '''))
sfvofz.version('2.1-git')
sfvofz.synopsis('''sfvofz > out.rsf n1= n= n2= n= g=1. v0=0.5 s=0.5 d1=0.5/(n1-1) d2=1./(n2-1) o1=0. o2=0. intime=n''','''''')
rsf.doc.progs['sfvofz']=sfvofz

sfvscan = rsf.doc.rsfprog('sfvscan','system/seismic/Mvscan.c','''Velocity analysis.''')
sfvscan.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('grad',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvscan.par('semblance',rsf.doc.rsfpar('bool','n','','''if y, compute semblance; if n, stack '''))
sfvscan.par('diffsemblance',rsf.doc.rsfpar('bool','n','','''if y, compute differential semblance '''))
sfvscan.par('avosemblance',rsf.doc.rsfpar('bool','n','','''if y, compute AVO-friendly semblance '''))
sfvscan.par('nb',rsf.doc.rsfpar('int','2','','''semblance averaging '''))
sfvscan.par('weight',rsf.doc.rsfpar('bool','y','','''if y, apply pseudo-unitary weighting '''))
sfvscan.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfvscan.par('smax',rsf.doc.rsfpar('float','2.0','','''maximum heterogeneity '''))
sfvscan.par('ns',rsf.doc.rsfpar('int','1','','''number of heterogeneity scans '''))
sfvscan.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfvscan.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfvscan.par('v1',rsf.doc.rsfpar('float','','','''( v1 reference velocity )'''))
sfvscan.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfvscan.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfvscan.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfvscan.par('v0',rsf.doc.rsfpar('float','','','''first scanned velocity '''))
sfvscan.par('dv',rsf.doc.rsfpar('float','','','''step in velocity '''))
sfvscan.par('nv',rsf.doc.rsfpar('int','','','''number of scanned velocities '''))
sfvscan.par('v1',rsf.doc.rsfpar('float','','','''reference velocity '''))
sfvscan.par('type',rsf.doc.rsfpar('string ',desc='''type of semblance (avo,diff,sembl,power,weighted) '''))
sfvscan.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvscan.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file (auxiliary input file name)'''))
sfvscan.par('grad',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvscan.version('2.1-git')
sfvscan.synopsis('''sfvscan < cmp.rsf > scan.rsf offset=offset.rsf mask=msk.rsf grad=grd.rsf semblance=n diffsemblance=n avosemblance=n nb=2 weight=y half=y smax=2.0 ns=1 slowness=n squared=n v1= extend=4 mute=12 str=0.5 v0= dv= nv= v1= type=''','''
Inverse of sfvelmod.

May 2013 program of the month:
http://www.ahay.org/blog/2013/05/04/program-of-the-month-sfvscan/
''')
rsf.doc.progs['sfvscan']=sfvscan

sfxlagtoang2d = rsf.doc.rsfprog('sfxlagtoang2d','system/seismic/Mxlagtoang2d.c','''SS(x-lag) to angle transformation (PP or PS waves) ''')
sfxlagtoang2d.par('vpvs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxlagtoang2d.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxlagtoang2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfxlagtoang2d.par('inv',rsf.doc.rsfpar('bool','n','','''inverse transformation flag '''))
sfxlagtoang2d.par('na',rsf.doc.rsfpar('int','sf_n(axs)','',''''''))
sfxlagtoang2d.par('da',rsf.doc.rsfpar('float','1./(sf_n(axs)-1)','',''''''))
sfxlagtoang2d.par('oa',rsf.doc.rsfpar('float','0.','',''''''))
sfxlagtoang2d.par('extend',rsf.doc.rsfpar('int','4','','''tmp extension '''))
sfxlagtoang2d.version('2.1-git')
sfxlagtoang2d.synopsis('''sfxlagtoang2d < Fstk.rsf > Fang.rsf vpvs=Fgam.rsf dip=Fdip.rsf verb=n inv=n na=sf_n(axs) da=1./(sf_n(axs)-1) oa=0. extend=4''','''''')
rsf.doc.progs['sfxlagtoang2d']=sfxlagtoang2d

sfzoeppritz = rsf.doc.rsfprog('sfzoeppritz','system/seismic/Mzoeppritz.c','''Testing Zoeppritz equation ''')
sfzoeppritz.par('na',rsf.doc.rsfpar('int','90','','''number of angles '''))
sfzoeppritz.par('a0',rsf.doc.rsfpar('float','0.','','''first angle '''))
sfzoeppritz.par('da',rsf.doc.rsfpar('float','90./na','','''angle increment '''))
sfzoeppritz.par('icoef',rsf.doc.rsfpar('int','4','[1,2,3,4]','''particle displacement, displacement potential, energy, real part '''))
sfzoeppritz.par('vp1',rsf.doc.rsfpar('float','','',''''''))
sfzoeppritz.par('vp2',rsf.doc.rsfpar('float','','',''''''))
sfzoeppritz.par('vs1',rsf.doc.rsfpar('float','','',''''''))
sfzoeppritz.par('vs2',rsf.doc.rsfpar('float','','',''''''))
sfzoeppritz.par('rho1',rsf.doc.rsfpar('float','1.','',''''''))
sfzoeppritz.par('rho2',rsf.doc.rsfpar('float','1.','',''''''))
sfzoeppritz.par('incp',rsf.doc.rsfpar('bool','y','','''incident P (or S) '''))
sfzoeppritz.par('outp',rsf.doc.rsfpar('bool','y','','''rellected/transmitted P (or S) '''))
sfzoeppritz.par('refl',rsf.doc.rsfpar('bool','y','','''reflection or transmission '''))
sfzoeppritz.version('2.1-git')
sfzoeppritz.synopsis('''sfzoeppritz > out.rsf na=90 a0=0. da=90./na icoef=4 vp1= vp2= vs1= vs2= rho1=1. rho2=1. incp=y outp=y refl=y''','''''')
rsf.doc.progs['sfzoeppritz']=sfzoeppritz

sfzomig = rsf.doc.rsfprog('sfzomig','system/seismic/Mzomig.c','''3-D zero-offset modeling/migration with extended split-step''')
sfzomig.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomig.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfzomig.par('incore',rsf.doc.rsfpar('bool','y','','''in core execution '''))
sfzomig.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfzomig.par('inv',rsf.doc.rsfpar('bool','n','','''y=modeling; n=migration '''))
sfzomig.par('causal',rsf.doc.rsfpar('bool','n','','''y=causal; n=anti-causal '''))
sfzomig.par('twoway',rsf.doc.rsfpar('bool','y','','''two-way traveltime '''))
sfzomig.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum references '''))
sfzomig.par('dtmax',rsf.doc.rsfpar('float','0.004','','''time error '''))
sfzomig.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfzomig.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfzomig.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfzomig.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfzomig.par('nw',rsf.doc.rsfpar('int','','',''''''))
sfzomig.par('dw',rsf.doc.rsfpar('float','','',''''''))
sfzomig.par('ow',rsf.doc.rsfpar('float','0.','',''''''))
sfzomig.par('mode',rsf.doc.rsfpar('string ',desc=''''''))
sfzomig.version('2.1-git')
sfzomig.synopsis('''sfzomig slo=Fs.rsf < Fd.rsf > Fw.rsf < Fi.rsf verb=n incore=y eps=0.01 inv=n causal=n twoway=y nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0 nw= dw= ow=0. mode=''','''To be deprecated in favor of zomig3 ''')
rsf.doc.progs['sfzomig']=sfzomig

sfzomva = rsf.doc.rsfprog('sfzomva','system/seismic/Mzomva.c','''3-D zero-offset WEMVA ''')
sfzomva.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomva.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfzomva.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfzomva.par('eps',rsf.doc.rsfpar('float','0.01','','''stability parameter '''))
sfzomva.par('inv',rsf.doc.rsfpar('bool','n','','''y=modeling; n=migration '''))
sfzomva.par('twoway',rsf.doc.rsfpar('bool','y','','''two-way traveltime '''))
sfzomva.par('nrmax',rsf.doc.rsfpar('int','1','','''maximum number of references '''))
sfzomva.par('dtmax',rsf.doc.rsfpar('float','0.004','','''time error '''))
sfzomva.par('pmx',rsf.doc.rsfpar('int','0','','''padding on x '''))
sfzomva.par('pmy',rsf.doc.rsfpar('int','0','','''padding on y'''))
sfzomva.par('tmx',rsf.doc.rsfpar('int','0','','''taper on x'''))
sfzomva.par('tmy',rsf.doc.rsfpar('int','0','','''taper on y '''))
sfzomva.version('2.1-git')
sfzomva.synopsis('''sfzomva slo=Bs.rsf wfl=Bw.rsf < Pi.rsf > Ps.rsf verb=n eps=0.01 inv=n twoway=y nrmax=1 dtmax=0.004 pmx=0 pmy=0 tmx=0 tmy=0''','''''')
rsf.doc.progs['sfzomva']=sfzomva

rsf.doc.progs['sft2chebstretch']=sfstretch
rsf.doc.progs['sfscalestretch']=sfstretch
rsf.doc.progs['sflogstretch']=sfstretch
rsf.doc.progs['sfsuread']=sfsegyread
rsf.doc.progs['sft2stretch']=sfstretch
rsf.doc.progs['sfradstretch']=sfstretch
rsf.doc.progs['sfsuwrite']=sfsegywrite
rsf.doc.progs['sfnmostretch']=sfstretch
rsf.doc.progs['sflmostretch']=sfstretch
rsf.doc.progs['sfdatstretch']=sfstretch
