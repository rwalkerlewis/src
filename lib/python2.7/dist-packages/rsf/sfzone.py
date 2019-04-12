import rsf.doc

sfcij2moveout = rsf.doc.rsfprog('sfcij2moveout','user/zone/Mcij2moveout.c','''Converting interval Cij to interval/effective moveout coefficients in 3D layered orthorhombic with possible phimuthal rotation (Sripanich and Fomel, 2016) ''')
sfcij2moveout.par('a12o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a22o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a1111o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a1112o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a1122o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a1222o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('a2222o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcij2moveout.par('c55',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c33',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c66',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c12',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c13',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c23',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c22',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('c44',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcij2moveout.par('scalecij',rsf.doc.rsfpar('float','1','','''Scaling of input Cij in case of GPa or km^2/s^2'''))
sfcij2moveout.par('scalequartic',rsf.doc.rsfpar('bool','n','','''Scaling the output quartic coefficients y--multiplied by 2 t0^2 (t0 = two-way) to look at the property of the layer -> input for GMA'''))
sfcij2moveout.par('eff',rsf.doc.rsfpar('bool','n','','''Output effective parameters instead of interval'''))
sfcij2moveout.version('2.1-git')
sfcij2moveout.synopsis('''sfcij2moveout > a11o.rsf a12o=a12o.rsf a22o=a22o.rsf a1111o=a1111o.rsf a1112o=a1112o.rsf a1122o=a1122o.rsf a1222o=a1222o.rsf a2222o=a2222o.rsf < C11.rsf c55=C55.rsf c33=C33.rsf c66=C66.rsf c12=C12.rsf c13=C13.rsf c23=C23.rsf c22=C22.rsf c44=C44.rsf phi=Phi.rsf scalecij=1 scalequartic=n eff=n''','''''')
rsf.doc.progs['sfcij2moveout']=sfcij2moveout

sfisaac0 = rsf.doc.rsfprog('sfisaac0','user/zone/Misaac0.c','''Zero-offset bending ray tracing in one-layered media''')
sfisaac0.par('xrefl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisaac0.par('ns',rsf.doc.rsfpar('int','nr','','''Number of sources '''))
sfisaac0.par('ds',rsf.doc.rsfpar('float','dr','','''source sampling '''))
sfisaac0.par('s0',rsf.doc.rsfpar('float','r0','','''source origin '''))
sfisaac0.par('order',rsf.doc.rsfpar('int','3','','''interpolation order '''))
sfisaac0.par('velocity',rsf.doc.rsfpar('float','2.0','','''assign velocity km/s'''))
sfisaac0.par('tol',rsf.doc.rsfpar('float','0.0001/velocity','','''assign a default value for tolerance'''))
sfisaac0.version('2.1-git')
sfisaac0.synopsis('''sfisaac0 < refl.rsf > ttime.rsf xrefl=xrefl.rsf ns=nr ds=dr s0=r0 order=3 velocity=2.0 tol=0.0001/velocity''','''''')
rsf.doc.progs['sfisaac0']=sfisaac0

sfisaac1 = rsf.doc.rsfprog('sfisaac1','user/zone/Misaac1.c','''Pre-stack bending ray tracing in one-layered media''')
sfisaac1.par('xrefl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisaac1.par('ns',rsf.doc.rsfpar('int','nr','','''number of sources for midpoint'''))
sfisaac1.par('ns2',rsf.doc.rsfpar('int','nr','','''number of sources for offset'''))
sfisaac1.par('ds',rsf.doc.rsfpar('float','dr','','''source sampling for midpoint'''))
sfisaac1.par('ds2',rsf.doc.rsfpar('float','dr','','''source sampling for offset'''))
sfisaac1.par('s0',rsf.doc.rsfpar('float','r0','','''origin for midpoint'''))
sfisaac1.par('s02',rsf.doc.rsfpar('float','r0','','''origin for offset'''))
sfisaac1.par('type',rsf.doc.rsfpar('int','1','','''Interpolation type 0=sf_eno and 1=central finite difference'''))
sfisaac1.par('order',rsf.doc.rsfpar('int','4','','''Interpolation order if choose to use sf_eno'''))
sfisaac1.par('velocity',rsf.doc.rsfpar('float','2.0','','''Assign velocity km/s'''))
sfisaac1.par('tol',rsf.doc.rsfpar('float','1/(1000000*velocity)','','''Assign a default value for tolerance'''))
sfisaac1.par('break',rsf.doc.rsfpar('bool','n','','''Go beyond zero or not'''))
sfisaac1.version('2.1-git')
sfisaac1.synopsis('''sfisaac1 < refl.rsf > ttime.rsf xrefl=xrefl.rsf ns=nr ns2=nr ds=dr ds2=dr s0=r0 s02=r0 type=1 order=4 velocity=2.0 tol=1/(1000000*velocity) break=n''','''''')
rsf.doc.progs['sfisaac1']=sfisaac1

sfisaac2 = rsf.doc.rsfprog('sfisaac2','user/zone/Misaac2.c','''2D Bending ray tracing in multi-layered media''')
sfisaac2.par('aniso',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisaac2.par('layer',rsf.doc.rsfpar('floats','','','''Layer sequence [nr2+1]'''))
sfisaac2.par('velocity',rsf.doc.rsfpar('floats','','','''Assign velocity km/s [N-1]'''))
sfisaac2.par('xgradient',rsf.doc.rsfpar('floats','','','''Assign x-gradient [N-1]'''))
sfisaac2.par('zgradient',rsf.doc.rsfpar('floats','','','''Assign z-gradient  [N-1]'''))
sfisaac2.par('xref',rsf.doc.rsfpar('floats','','','''Assign x-reference point [N-1]'''))
sfisaac2.par('zref',rsf.doc.rsfpar('floats','','','''Assign z-reference point [N-1]'''))
sfisaac2.par('velocity',rsf.doc.rsfpar('floats','','','''Assign velocity km/s [N-1]'''))
sfisaac2.par('xinitial',rsf.doc.rsfpar('floats','','',''' [nr2]'''))
sfisaac2.par('number',rsf.doc.rsfpar('int','','','''Number of intersecting points [nr2]'''))
sfisaac2.par('xs',rsf.doc.rsfpar('float','','','''Source'''))
sfisaac2.par('xr',rsf.doc.rsfpar('float','','','''Receiver'''))
sfisaac2.par('vstatus',rsf.doc.rsfpar('int','','','''Velocity status (0 for constant v, 1 for gradient v, and 2 for VTI)'''))
sfisaac2.par('min',rsf.doc.rsfpar('float','(xx[0]<xx[nr2+1])? xx[0]:xx[nr2+1]','','''The minimum boundary if not entered, set to min(xs,xr)'''))
sfisaac2.par('max',rsf.doc.rsfpar('float','(xx[0]>xx[nr2+1])? xx[0]:xx[nr2+1]','','''The maximum boundary if not entered, set to max(xs,xr)'''))
sfisaac2.par('niter',rsf.doc.rsfpar('int','100','','''The number of iterations'''))
sfisaac2.par('debug',rsf.doc.rsfpar('bool','n','','''Debug flag'''))
sfisaac2.par('tol',rsf.doc.rsfpar('double','0.000001/v_inp[0]','','''Assign a default value for tolerance'''))
sfisaac2.par('ns',rsf.doc.rsfpar('int','2','','''Dimension of output reflection points (x,z)'''))
sfisaac2.par('ns2',rsf.doc.rsfpar('int','nr2+2','','''Dimension of output reflection points (the number of points)'''))
sfisaac2.par('ds',rsf.doc.rsfpar('float','1','','''Step increment'''))
sfisaac2.par('s0',rsf.doc.rsfpar('float','0','','''Staring position'''))
sfisaac2.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sfisaac2.version('2.1-git')
sfisaac2.synopsis('''sfisaac2 < refl.rsf > xrefl.rsf aniso=vti.rsf layer= velocity= xgradient= zgradient= xref= zref= velocity= xinitial= number= xs= xr= vstatus= min=(xx[0]<xx[nr2+1])? xx[0]:xx[nr2+1] max=(xx[0]>xx[nr2+1])? xx[0]:xx[nr2+1] niter=100 debug=n tol=0.000001/v_inp[0] ns=2 ns2=nr2+2 ds=1 s0=0 order=3''','''''')
rsf.doc.progs['sfisaac2']=sfisaac2

sfisaac3 = rsf.doc.rsfprog('sfisaac3','user/zone/Misaac3.c','''3D Bending ray tracing in Multi-layered media''')
sfisaac3.par('aniso',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisaac3.par('layer',rsf.doc.rsfpar('floats','','','''Layer sequence [nr3+1]'''))
sfisaac3.par('velocity',rsf.doc.rsfpar('floats','','','''Assign velocity km/s [N-1]'''))
sfisaac3.par('xgradient',rsf.doc.rsfpar('floats','','','''Assign x-gradient [N-1]'''))
sfisaac3.par('ygradient',rsf.doc.rsfpar('floats','','','''Assign y-gradient [N-1]'''))
sfisaac3.par('zgradient',rsf.doc.rsfpar('floats','','','''Assign z-gradient  [N-1]'''))
sfisaac3.par('xref',rsf.doc.rsfpar('floats','','','''Assign x-reference point [N-1]'''))
sfisaac3.par('yref',rsf.doc.rsfpar('floats','','','''Assign y-reference point [N-1]'''))
sfisaac3.par('zref',rsf.doc.rsfpar('floats','','','''Assign z-reference point [N-1]'''))
sfisaac3.par('xinitial',rsf.doc.rsfpar('floats','','',''' [nr3]'''))
sfisaac3.par('yinitial',rsf.doc.rsfpar('floats','','',''' [nr3]'''))
sfisaac3.par('xinitial',rsf.doc.rsfpar('floats','','',''' [nr3]'''))
sfisaac3.par('number',rsf.doc.rsfpar('int','','','''Number of reflectors'''))
sfisaac3.par('xs',rsf.doc.rsfpar('float','','','''x-Source'''))
sfisaac3.par('ys',rsf.doc.rsfpar('float','','','''y-Source'''))
sfisaac3.par('xr',rsf.doc.rsfpar('float','','','''x-Receiver'''))
sfisaac3.par('yr',rsf.doc.rsfpar('float','','','''y-Receiver'''))
sfisaac3.par('vstatus',rsf.doc.rsfpar('int','','','''Velocity status (0 for constant v, 1 for gradient v, and 2 for VTI)'''))
sfisaac3.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sfisaac3.par('xmin',rsf.doc.rsfpar('float','','',''''''))
sfisaac3.par('ymin',rsf.doc.rsfpar('float','','',''''''))
sfisaac3.par('xmax',rsf.doc.rsfpar('float','','',''''''))
sfisaac3.par('ymax',rsf.doc.rsfpar('float','','',''''''))
sfisaac3.par('niter',rsf.doc.rsfpar('int','','','''The number of iterations'''))
sfisaac3.par('debug',rsf.doc.rsfpar('bool','n','','''Debug flag'''))
sfisaac3.par('tol',rsf.doc.rsfpar('double','0.000001/v_inp[0]','','''Assign a default value for tolerance'''))
sfisaac3.par('ns',rsf.doc.rsfpar('int','3 ','','''Dimension of output reflection points (x,y,z) '''))
sfisaac3.par('ns2',rsf.doc.rsfpar('int','nr3+2','','''Dimension of output reflection points (the number of points)'''))
sfisaac3.par('ds',rsf.doc.rsfpar('float','1','','''Step increment'''))
sfisaac3.par('s0',rsf.doc.rsfpar('float','0','','''Staring position'''))
sfisaac3.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sfisaac3.version('2.1-git')
sfisaac3.synopsis('''sfisaac3 < refl.rsf > xrefl.rsf aniso=vti.rsf layer= velocity= xgradient= ygradient= zgradient= xref= yref= zref= xinitial= yinitial= xinitial= number= xs= ys= xr= yr= vstatus= order=3 xmin= ymin= xmax= ymax= niter= debug=n tol=0.000001/v_inp[0] ns=3  ns2=nr3+2 ds=1 s0=0 order=3''','''''')
rsf.doc.progs['sfisaac3']=sfisaac3

sfkirmod_newton = rsf.doc.rsfprog('sfkirmod_newton','user/zone/Mkirmod_newton.c','''Kirchhoff 2-D/2.5-D modeling in layered media with bending ray tracing.  ''')
sfkirmod_newton.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod_newton.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod_newton.par('picks',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkirmod_newton.par('slopes',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfkirmod_newton.par('aniso',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkirmod_newton.par('velocity',rsf.doc.rsfpar('floats','','','''Assign velocity km/s [nc]'''))
sfkirmod_newton.par('xgradient',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfkirmod_newton.par('zgradient',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfkirmod_newton.par('xref',rsf.doc.rsfpar('floats','','','''Assign x-reference point [nc]'''))
sfkirmod_newton.par('zref',rsf.doc.rsfpar('floats','','','''Assign z-reference point [nc]'''))
sfkirmod_newton.par('lin',rsf.doc.rsfpar('bool','n','','''if linear operator '''))
sfkirmod_newton.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfkirmod_newton.par('absoff',rsf.doc.rsfpar('bool','n','','''y - h0 is not in shot coordinate system '''))
sfkirmod_newton.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfkirmod_newton.par('dt',rsf.doc.rsfpar('float','0.004','','''time sampling '''))
sfkirmod_newton.par('t0',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfkirmod_newton.par('ns',rsf.doc.rsfpar('int','nx','','''number of shots (midpoints if cmp=y) '''))
sfkirmod_newton.par('s0',rsf.doc.rsfpar('float','x0','','''first shot (midpoint if cmp=y) '''))
sfkirmod_newton.par('ds',rsf.doc.rsfpar('float','dx','','''shot/midpoint increment '''))
sfkirmod_newton.par('nh',rsf.doc.rsfpar('int','nx','','''number of offsets '''))
sfkirmod_newton.par('h0',rsf.doc.rsfpar('float','0.','','''first offset '''))
sfkirmod_newton.par('dh',rsf.doc.rsfpar('float','dx','','''offset increment '''))
sfkirmod_newton.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkirmod_newton.par('r0',rsf.doc.rsfpar('float','1.','','''normal reflectivity (if constant) '''))
sfkirmod_newton.par('r0',rsf.doc.rsfpar('float','1.','','''normal reflectivity (if constant) '''))
sfkirmod_newton.par('debug',rsf.doc.rsfpar('bool','n','','''debug flag '''))
sfkirmod_newton.par('fwdxini',rsf.doc.rsfpar('bool','n','','''use the result of previous iteration to be the xinitial of the next one '''))
sfkirmod_newton.par('vstatus',rsf.doc.rsfpar('int','','','''Velocity status (0 for constant v,1 for gradient v, and 2 for vti)'''))
sfkirmod_newton.par('niter',rsf.doc.rsfpar('int','500','','''The number of iterations'''))
sfkirmod_newton.par('tol',rsf.doc.rsfpar('double','0.00001','','''Assign a default value for tolerance'''))
sfkirmod_newton.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sfkirmod_newton.par('cmp',rsf.doc.rsfpar('bool','n','','''compute CMP instead of shot gathers '''))
sfkirmod_newton.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfkirmod_newton.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirmod_newton.par('rgrad',rsf.doc.rsfpar('string ',desc='''AVO gradient file (B/A) '''))
sfkirmod_newton.par('dip',rsf.doc.rsfpar('string ',desc='''reflector dip file '''))
sfkirmod_newton.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfkirmod_newton.par('picks',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfkirmod_newton.par('slopes',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfkirmod_newton.version('2.1-git')
sfkirmod_newton.synopsis('''sfkirmod_newton < modl.rsf > data.rsf curv=curv.rsf refl=refl.rsf picks=picks.rsf slopes=slopes.rsf aniso=vti.rsf velocity= xgradient= zgradient= xref= zref= lin=n adj=n absoff=n nt= dt=0.004 t0=0. ns=nx s0=x0 ds=dx nh=nx h0=0. dh=dx verb=n r0=1. r0=1. debug=n fwdxini=n vstatus= niter=500 tol=0.00001 order=3 cmp=n freq=0.2/dt rgrad= dip=''','''''')
rsf.doc.progs['sfkirmod_newton']=sfkirmod_newton

sfmpikirmodnewton = rsf.doc.rsfprog('sfmpikirmodnewton','user/zone/Mmpikirmodnewton.c','''Kirchhoff 2-D/2.5-D modeling in layered media with bending ray tracing.  ''')
sfmpikirmodnewton.par('input',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpikirmodnewton.par('output',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpikirmodnewton.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpikirmodnewton.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpikirmodnewton.par('aniso',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpikirmodnewton.par('velocity',rsf.doc.rsfpar('floats','','','''Assign velocity km/s [nc]'''))
sfmpikirmodnewton.par('xgradient',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfmpikirmodnewton.par('zgradient',rsf.doc.rsfpar('floats','','',''' [nc]'''))
sfmpikirmodnewton.par('xref',rsf.doc.rsfpar('floats','','','''Assign x-reference point [nc]'''))
sfmpikirmodnewton.par('zref',rsf.doc.rsfpar('floats','','','''Assign z-reference point [nc]'''))
sfmpikirmodnewton.par('newton',rsf.doc.rsfpar('bool','y','','''To switch between analytical and newton kirmod'''))
sfmpikirmodnewton.par('lin',rsf.doc.rsfpar('bool','n','','''if linear operator '''))
sfmpikirmodnewton.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfmpikirmodnewton.par('absoff',rsf.doc.rsfpar('bool','n','','''y - h0 is not in shot coordinate system '''))
sfmpikirmodnewton.par('nt',rsf.doc.rsfpar('int','','','''time samples '''))
sfmpikirmodnewton.par('dt',rsf.doc.rsfpar('float','0.004','','''time sampling '''))
sfmpikirmodnewton.par('t0',rsf.doc.rsfpar('float','0.','','''time origin '''))
sfmpikirmodnewton.par('ns',rsf.doc.rsfpar('int','nx','','''number of shots (midpoints if cmp=y) '''))
sfmpikirmodnewton.par('s0',rsf.doc.rsfpar('float','x0','','''first shot (midpoint if cmp=y) '''))
sfmpikirmodnewton.par('ds',rsf.doc.rsfpar('float','dx','','''shot/midpoint increment '''))
sfmpikirmodnewton.par('nh',rsf.doc.rsfpar('int','nx','','''number of offsets '''))
sfmpikirmodnewton.par('h0',rsf.doc.rsfpar('float','0.','','''first offset '''))
sfmpikirmodnewton.par('dh',rsf.doc.rsfpar('float','dx','','''offset increment '''))
sfmpikirmodnewton.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmpikirmodnewton.par('r0',rsf.doc.rsfpar('float','1.','','''normal reflectivity (if constant) '''))
sfmpikirmodnewton.par('debug',rsf.doc.rsfpar('bool','n','','''debug flag '''))
sfmpikirmodnewton.par('fwdxini',rsf.doc.rsfpar('bool','n','','''use the result of previous iteration to be the xinitial of the next one '''))
sfmpikirmodnewton.par('vstatus',rsf.doc.rsfpar('int','','','''Velocity status (0 for constant v,1 for gradient v, and 2 for vti)'''))
sfmpikirmodnewton.par('niter',rsf.doc.rsfpar('int','500','','''The number of iterations'''))
sfmpikirmodnewton.par('tol',rsf.doc.rsfpar('double','0.00001','','''Assign a default value for tolerance'''))
sfmpikirmodnewton.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sfmpikirmodnewton.par('twod',rsf.doc.rsfpar('bool','n','','''2-D or 2.5-D '''))
sfmpikirmodnewton.par('cmp',rsf.doc.rsfpar('bool','n','','''compute CMP instead of shot gathers '''))
sfmpikirmodnewton.par('freq',rsf.doc.rsfpar('float','0.2/dt','','''peak frequency for Ricker wavelet '''))
sfmpikirmodnewton.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfmpikirmodnewton.par('gradx',rsf.doc.rsfpar('float','','','''horizontal velocity gradient '''))
sfmpikirmodnewton.par('gradz',rsf.doc.rsfpar('float','','','''vertical velocity gradient '''))
sfmpikirmodnewton.par('velz',rsf.doc.rsfpar('float','','','''vertical velocity for VTI anisotropy '''))
sfmpikirmodnewton.par('eta',rsf.doc.rsfpar('float','','','''parameter for VTI anisotropy '''))
sfmpikirmodnewton.par('refx',rsf.doc.rsfpar('float','','','''reference x-coordinate for velocity '''))
sfmpikirmodnewton.par('refz',rsf.doc.rsfpar('float','','','''reference z-coordinate for velocity '''))
sfmpikirmodnewton.par('vel2',rsf.doc.rsfpar('float','','','''converted velocity '''))
sfmpikirmodnewton.par('gradx2',rsf.doc.rsfpar('float','','','''converted velocity, horizontal gradient '''))
sfmpikirmodnewton.par('gradz2',rsf.doc.rsfpar('float','','','''converted velocity, vertical gradient '''))
sfmpikirmodnewton.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmpikirmodnewton.par('rgrad',rsf.doc.rsfpar('string ',desc='''AVO gradient file (B/A) '''))
sfmpikirmodnewton.par('dip',rsf.doc.rsfpar('string ',desc='''reflector dip file '''))
sfmpikirmodnewton.par('type',rsf.doc.rsfpar('string ',desc='''type of velocity, 'c': constant, 's': linear sloth, 'v': linear velocity, 'a': VTI anisotropy '''))
sfmpikirmodnewton.par('type2',rsf.doc.rsfpar('string ',desc='''type of velocity for the converted (receiver side) branch '''))
sfmpikirmodnewton.version('2.1-git')
sfmpikirmodnewton.synopsis('''sfmpikirmodnewton input=modl.rsf output=data.rsf curv=curv.rsf refl=refl.rsf aniso=vti.rsf velocity= xgradient= zgradient= xref= zref= newton=y lin=n adj=n absoff=n nt= dt=0.004 t0=0. ns=nx s0=x0 ds=dx nh=nx h0=0. dh=dx verb=n r0=1. debug=n fwdxini=n vstatus= niter=500 tol=0.00001 order=3 twod=n cmp=n freq=0.2/dt vel= gradx= gradz= velz= eta= refx= refz= vel2= gradx2= gradz2= rgrad= dip= type= type2=''','''''')
rsf.doc.progs['sfmpikirmodnewton']=sfmpikirmodnewton

sfnmo3gmaprep = rsf.doc.rsfprog('sfnmo3gmaprep','user/zone/Mnmo3gmaprep.c','''3D NMO GMA  linearized operator preparation for lsfit''')
sfnmo3gmaprep.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gmaprep.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfnmo3gmaprep.version('2.1-git')
sfnmo3gmaprep.synopsis('''sfnmo3gmaprep < inp.rsf coef=inicoef.rsf > out.rsf fit=fit.rsf''','''''')
rsf.doc.progs['sfnmo3gmaprep']=sfnmo3gmaprep

sfnmo3gmafit = rsf.doc.rsfprog('sfnmo3gmafit','user/zone/Mnmo3gmafit.c','''3D NMO GMA  linearized operator preparation for lsfit''')
sfnmo3gmafit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gmafit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfnmo3gmafit.par('offsetx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gmafit.par('offsety',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3gmafit.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfnmo3gmafit.par('gather',rsf.doc.rsfpar('bool','n','','''Memory allocation'''))
sfnmo3gmafit.version('2.1-git')
sfnmo3gmafit.synopsis('''sfnmo3gmafit < inp.rsf coef=inicoef.rsf > out.rsf fit=fit.rsf offsetx=offsx.rsf offsety=offsy.rsf verb=n gather=n''','''''')
rsf.doc.progs['sfnmo3gmafit']=sfnmo3gmafit

sfrotater = rsf.doc.rsfprog('sfrotater','user/zone/Mrotater.c','''Roatation with Interpolation from a regular grid in 2-D. ''')
sfrotater.par('angle',rsf.doc.rsfpar('float','90.','','''rotation angle '''))
sfrotater.par('interp',rsf.doc.rsfpar('string ',desc='''[n,l,c] interpolation type '''))
sfrotater.version('2.1-git')
sfrotater.synopsis('''sfrotater < inp.rsf > out.rsf angle=90. interp=''','''''')
rsf.doc.progs['sfrotater']=sfrotater

sftime2depthweak = rsf.doc.rsfprog('sftime2depthweak','user/zone/Mtime2depthweak.c','''Time-to-depth conversion in media with weak lateral variations 2D (Sripanich and Fomel, 2017). ''')
sftime2depthweak.par('dvdx0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftime2depthweak.par('dvdt0',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftime2depthweak.par('refvelocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftime2depthweak.par('outdt0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftime2depthweak.par('outdx0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftime2depthweak.par('outdv',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftime2depthweak.par('zsubsample',rsf.doc.rsfpar('int','100','','''Additional subsampling in depth for stability '''))
sftime2depthweak.par('nderiv',rsf.doc.rsfpar('int','10','','''Derivative filter order '''))
sftime2depthweak.par('refderiv',rsf.doc.rsfpar('float','1.','','''Deriveative filter reference (0.5 < ref <= 1) '''))
sftime2depthweak.par('smoothlen',rsf.doc.rsfpar('int','nx/20','','''Smoothing filter length '''))
sftime2depthweak.par('nsmooth',rsf.doc.rsfpar('int','10','','''Smoothing repeat '''))
sftime2depthweak.version('2.1-git')
sftime2depthweak.synopsis('''sftime2depthweak < in.rsf dvdx0=dveldx0.rsf dvdt0=dveldt0.rsf refvelocity=refvelocity.rsf > out.rsf outdt0=outdeltime.rsf outdx0=outdeldist.rsf outdv=outdelv.rsf zsubsample=100 nderiv=10 refderiv=1. smoothlen=nx/20 nsmooth=10''','''''')
rsf.doc.progs['sftime2depthweak']=sftime2depthweak

sffermatrecursion = rsf.doc.rsfprog('sffermatrecursion','user/zone/Mfermatrecursion.c','''2D traveltime derivatives computation with the recursion from Fermat's principle (Sripanich and Fomel, 2017)''')
sffermatrecursion.par('slow',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffermatrecursion.par('vnmosq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffermatrecursion.par('t0sum',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffermatrecursion.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffermatrecursion.par('curv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffermatrecursion.par('dipcurv',rsf.doc.rsfpar('bool','n','','''if get dip/curvature from separate files '''))
sffermatrecursion.par('order',rsf.doc.rsfpar('int','3','','''Interpolation order'''))
sffermatrecursion.version('2.1-git')
sffermatrecursion.synopsis('''sffermatrecursion < refl.rsf slow=slow.rsf vnmosq=vnmo.rsf t0sum=t0.rsf dip=dipf.rsf curv=curvf.rsf > vnmohet.rsf dipcurv=n order=3''','''''')
rsf.doc.progs['sffermatrecursion']=sffermatrecursion

sfvtihti2ort = rsf.doc.rsfprog('sfvtihti2ort','user/zone/Mvtihti2ort.c','''Combining VTI and HTI parameters to orthorhombic according to Schoenberg & Sayer (1995)''')
sfvtihti2ort.par('c22o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c33o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c44o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c55o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c66o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c12o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c13o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c23o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c55',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c11v',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c66v',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c12v',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c13v',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c11h',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c55h',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c12h',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c13h',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('phi',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvtihti2ort.par('c16o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c26o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c36o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('c45o',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvtihti2ort.par('rotate',rsf.doc.rsfpar('bool','n','','''Doing azimuthal rotation (y-> mono, n-> ortho)'''))
sfvtihti2ort.version('2.1-git')
sfvtihti2ort.synopsis('''sfvtihti2ort > c11o.rsf c22o=c22o.rsf c33o=c33o.rsf c44o=c44o.rsf c55o=c55o.rsf c66o=c66o.rsf c12o=c12o.rsf c13o=c13o.rsf c23o=c23o.rsf < c33.rsf c55=c55.rsf c11v=c11v.rsf c66v=c66v.rsf c12v=c12v.rsf c13v=c13v.rsf c11h=c11h.rsf c55h=c55h.rsf c12h=c12h.rsf c13h=c13h.rsf phi=phi.rsf c16o=c16o.rsf c26o=c26o.rsf c36o=c36o.rsf c45o=c45o.rsf rotate=n''','''NOTE: HTI is defined in VTI grid with respect to the vertical (Ruger(1997)) 
Refer to SEAM 2 notes for detailed description

''')
rsf.doc.progs['sfvtihti2ort']=sfvtihti2ort

sfnmo3mcmc = rsf.doc.rsfprog('sfnmo3mcmc','user/zone/Mnmo3mcmc.c','''3D NMO GMA MCMC inversion with Metropolis rule (Mosegaard and Tarantola, 1995) ''')
sfnmo3mcmc.par('t0sq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmc.par('rangecoef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmc.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfnmo3mcmc.par('sigma',rsf.doc.rsfpar('float','1.0','','''noise variance '''))
sfnmo3mcmc.par('saveiter',rsf.doc.rsfpar('int','20','','''save state every iter  '''))
sfnmo3mcmc.par('prior',rsf.doc.rsfpar('bool','n','','''generate prior or posterior '''))
sfnmo3mcmc.par('nmodel',rsf.doc.rsfpar('int','1000','','''Get the number of MC models'''))
sfnmo3mcmc.version('2.1-git')
sfnmo3mcmc.synopsis('''sfnmo3mcmc < inp.rsf t0sq=t0sqf.rsf rangecoef=rangecoeff.rsf > out.rsf seed=time(NULL) sigma=1.0 saveiter=20 prior=n nmodel=1000''','''''')
rsf.doc.progs['sfnmo3mcmc']=sfnmo3mcmc

sfnmo3mcmcspiral = rsf.doc.rsfprog('sfnmo3mcmcspiral','user/zone/Mnmo3mcmcspiral.c','''3D NMO GMA MCMC inversion for spiral sorted gather with Metropolis rule (Mosegaard and Tarantola, 1995) ''')
sfnmo3mcmcspiral.par('t0sq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmcspiral.par('rangecoef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmcspiral.par('offsetx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmcspiral.par('offsety',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3mcmcspiral.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfnmo3mcmcspiral.par('sigma',rsf.doc.rsfpar('float','1.0','','''noise variance '''))
sfnmo3mcmcspiral.par('saveiter',rsf.doc.rsfpar('int','20','','''save state every iter  '''))
sfnmo3mcmcspiral.par('prior',rsf.doc.rsfpar('bool','n','','''generate prior or posterior '''))
sfnmo3mcmcspiral.par('rational',rsf.doc.rsfpar('bool','n','','''use rational approximation form of GMA '''))
sfnmo3mcmcspiral.par('nmodel',rsf.doc.rsfpar('int','1000','','''Get the number of MC models'''))
sfnmo3mcmcspiral.version('2.1-git')
sfnmo3mcmcspiral.synopsis('''sfnmo3mcmcspiral < inp.rsf t0sq=t0sqf.rsf rangecoef=rangecoeff.rsf offsetx=ofx.rsf offsety=ofy.rsf > out.rsf seed=time(NULL) sigma=1.0 saveiter=20 prior=n rational=n nmodel=1000''','''''')
rsf.doc.progs['sfnmo3mcmcspiral']=sfnmo3mcmcspiral

