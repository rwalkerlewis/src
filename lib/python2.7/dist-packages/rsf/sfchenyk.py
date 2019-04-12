import rsf.doc

sfdispelem = rsf.doc.rsfprog('sfdispelem','user/chenyk/Mdispelem.c','''Display element of rsf files. ''')
sfdispelem.par('i1',rsf.doc.rsfpar('int','','','''get the index of first axis '''))
sfdispelem.par('i2',rsf.doc.rsfpar('int','','','''get the index of second axis '''))
sfdispelem.version('2.1-git')
sfdispelem.synopsis('''sfdispelem < in.rsf > out.rsf i1= i2=''','''''')
rsf.doc.progs['sfdispelem']=sfdispelem

sfdiff = rsf.doc.rsfprog('sfdiff','user/chenyk/Mdiff.c','''Compare the difference of two rsf data sets with the same size. ''')
sfdiff.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiff.version('2.1-git')
sfdiff.synopsis('''sfdiff < inp1.rsf match=inp2.rsf > dif.rsf''','''''')
rsf.doc.progs['sfdiff']=sfdiff

sfmulawefd2d = rsf.doc.rsfprog('sfmulawefd2d','user/chenyk/Mmulawefd2d.c','''2D multisource acoustic time-domain FD modeling for testing''')
sfmulawefd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmulawefd2d.par('sou1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmulawefd2d.par('sou2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmulawefd2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmulawefd2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmulawefd2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmulawefd2d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfmulawefd2d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfmulawefd2d.par('free',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfmulawefd2d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfmulawefd2d.par('cden',rsf.doc.rsfpar('bool','n','','''Constant density '''))
sfmulawefd2d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfmulawefd2d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfmulawefd2d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfmulawefd2d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfmulawefd2d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfmulawefd2d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfmulawefd2d.version('2.1-git')
sfmulawefd2d.synopsis('''sfmulawefd2d < Fwav.rsf vel=Fvel.rsf sou1=Fsou1.rsf sou2=Fsou2.rsf rec=Frec.rsf > Fdat.rsf wfl=Fwfl.rsf den=Fden.rsf verb=n snap=n free=n dabc=n cden=n jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax)''','''4th order in space, 2nd order in time. Absorbing boundary conditions.
Invisible parameter due to self-doc parsing bug: 
nb=[2] Boundary padding in grid points ''')
rsf.doc.progs['sfmulawefd2d']=sfmulawefd2d

sfemd = rsf.doc.rsfprog('sfemd','user/chenyk/Memd.c','''Empirical Mode Decomposition ''')
sfemd.par('threshold',rsf.doc.rsfpar('float','DEFAULT_THRESHOLD','','''Sifting stoping parameter: threshold, the default is 0.05. '''))
sfemd.par('tolerance',rsf.doc.rsfpar('float','DEFAULT_TOLERANCE','','''Sifting stoping parameter: tolerance, the default is 0.05. '''))
sfemd.par('miter',rsf.doc.rsfpar('int','MAX_ITERATIONS','','''Maximum number of iterations during sifting, the default is 1000. '''))
sfemd.par('mimf',rsf.doc.rsfpar('int','0','','''Maximum number of IMFs, the default is as many as possible. '''))
sfemd.version('2.1-git')
sfemd.synopsis('''sfemd < inp.rsf > outp.rsf threshold=DEFAULT_THRESHOLD tolerance=DEFAULT_TOLERANCE miter=MAX_ITERATIONS mimf=0''','''''')
rsf.doc.progs['sfemd']=sfemd

sfnorm = rsf.doc.rsfprog('sfnorm','user/chenyk/Mnorm.c','''Normalize the data. ''')
sfnorm.par('apply',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnorm.par('max',rsf.doc.rsfpar('float','','',''''''))
sfnorm.version('2.1-git')
sfnorm.synopsis('''sfnorm > outp.rsf < inp.rsf apply=apply.rsf max=''','''Normalize by dividing the data set by its absolute maximum value. ''')
rsf.doc.progs['sfnorm']=sfnorm

sfblend = rsf.doc.rsfprog('sfblend','user/chenyk/Mblend.c','''Seismic blending operator.''')
sfblend.par('verbose',rsf.doc.rsfpar('int','1','','''0 terse, 1 informative, 2 chatty, 3 debug '''))
sfblend.par('shot_time_in',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.par('shot_time_out',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.version('2.1-git')
sfblend.synopsis('''sfblend < in.rsf > out.rsf verbose=1 shot_time_in= shot_time_out=''','''Custom program to blend the seismic data.
''')
rsf.doc.progs['sfblend']=sfblend

sfxcorr = rsf.doc.rsfprog('sfxcorr','user/chenyk/Mxcorr.c','''Cross-correlation function  ''')
sfxcorr.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfxcorr.par('lagfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfxcorr.par('l',rsf.doc.rsfpar('int','n1y-1','','''maxlag of auto/cross correlation function'''))
sfxcorr.par('lagfile',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfxcorr.version('2.1-git')
sfxcorr.synopsis('''sfxcorr < in.rsf match=match.rsf > out.rsf lagfile=lagfile.rsf l=n1y-1''','''C=XCORR(X,Y,L), computes the (auto/cross) correlation over the range of lags:
-L to L, i.e., 2*L+1 lags. If L is left out, default is L=n1-1, 
where n1 is the length of Y.
''')
rsf.doc.progs['sfxcorr']=sfxcorr

sfmatoper = rsf.doc.rsfprog('sfmatoper','user/chenyk/Mmatoper.c','''Matrix algebra operation''')
sfmatoper.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmatoper.par('type',rsf.doc.rsfpar('string ',desc='''[mul, add, sub, dotmul] operation type, the default is mul  '''))
sfmatoper.version('2.1-git')
sfmatoper.synopsis('''sfmatoper < in.rsf mat=mat.rsf > out.rsf type=''','''Implement C=Oper(A,B).
Specially, when "Oper" stands for multiplication, C=AB,  where: 
C is a m*k matrix, m corresponds to dimension 2 while k corrsponds to dimension 1.
A is a m*n matrix, m corresponds to dimension 2 while n corrsponds to dimension 1.
B is a n*k matrix, n corresponds to dimension 2 while k corrsponds to dimension 1.
Like matlab matrix operation.''')
rsf.doc.progs['sfmatoper']=sfmatoper

sflesolver = rsf.doc.rsfprog('sflesolver','user/chenyk/Mlesolver.c','''Linear equations solver using Gauss Elimination ''')
sflesolver.par('d',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflesolver.version('2.1-git')
sflesolver.synopsis('''sflesolver < in.rsf d=d.rsf > out.rsf''','''''')
rsf.doc.progs['sflesolver']=sflesolver

sfpclipc2 = rsf.doc.rsfprog('sfpclipc2','user/chenyk/Mpclipc2.c','''One-or Two-sided Percentile Data clipping (C language).''')
sfpclipc2.par('upclip',rsf.doc.rsfpar('float','99','','''percentile upper cliping value '''))
sfpclipc2.par('lpclip',rsf.doc.rsfpar('float','0','','''percentile lower cliping value '''))
sfpclipc2.version('2.1-git')
sfpclipc2.synopsis('''sfpclipc2 < in.rsf > out.rsf upclip=99 lpclip=0''','''For example: 
A=1,2,3,...,100 
sfpclipc2 upclip=98 lpclip=3 
A'=3,3,3,...,98,98,98	
''')
rsf.doc.progs['sfpclipc2']=sfpclipc2

sfdwtdenoise = rsf.doc.rsfprog('sfdwtdenoise','user/chenyk/Mdwtdenoise.c','''2D Digital Wavelet Transoform Denoising ''')
sfdwtdenoise.par('pclip',rsf.doc.rsfpar('float','99.','','''data clip percentile (default is 99)'''))
sfdwtdenoise.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfdwtdenoise.version('2.1-git')
sfdwtdenoise.synopsis('''sfdwtdenoise < in.rsf > out.rsf pclip=99. type=''','''''')
rsf.doc.progs['sfdwtdenoise']=sfdwtdenoise

sftrisolver = rsf.doc.rsfprog('sftrisolver','user/chenyk/Mtrisolver.c','''Tridiagonal matrix solver using chasing method''')
sftrisolver.par('rhs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftrisolver.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sftrisolver.version('2.1-git')
sftrisolver.synopsis('''sftrisolver < in.rsf rhs=rhs.rsf > out.rsf verb=n''','''Ax=d-> LUx=d -> Ly=d -> Ux=y -> x
''')
rsf.doc.progs['sftrisolver']=sftrisolver

sfsymposolver = rsf.doc.rsfprog('sfsymposolver','user/chenyk/Msymposolver.c','''Symmetric positive definite matrix equation solver using square root method (cholesky decomposition method)''')
sfsymposolver.par('rhs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsymposolver.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfsymposolver.par('n',rsf.doc.rsfpar('int','','',''''''))
sfsymposolver.version('2.1-git')
sfsymposolver.synopsis('''sfsymposolver < in.rsf rhs=rhs.rsf > out.rsf verb=n n=''','''Ax=d-> LL'x=d -> Ly=d -> L'x=y -> x
Input is the down triangle of A.
''')
rsf.doc.progs['sfsymposolver']=sfsymposolver

sfseiscut = rsf.doc.rsfprog('sfseiscut','user/chenyk/Mseiscut.c','''Seislet Transform Denoising using Mask Operator''')
sfseiscut.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseiscut.par('slet',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseiscut.par('sletcut',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseiscut.par('cut',rsf.doc.rsfpar('int','n2/4','','''cut threshold value '''))
sfseiscut.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseiscut.par('order1',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfseiscut.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseiscut.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseiscut.par('slet',rsf.doc.rsfpar('string ',desc='''seismic domain (auxiliary output file name)'''))
sfseiscut.par('sletcut',rsf.doc.rsfpar('string ',desc='''cutted seislet domain (auxiliary output file name)'''))
sfseiscut.version('2.1-git')
sfseiscut.synopsis('''sfseiscut < in.rsf dip=dip.rsf > out.rsf slet=slet.rsf sletcut=sletcut.rsf cut=n2/4 eps=0.01 order1=1 eps=0.01 type=''','''''')
rsf.doc.progs['sfseiscut']=sfseiscut

sfseisthr = rsf.doc.rsfprog('sfseisthr','user/chenyk/Mseisthr.c','''Seislet Transform Denoising using Thresholding''')
sfseisthr.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisthr.par('slet',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseisthr.par('sletthr',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseisthr.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseisthr.par('pclip',rsf.doc.rsfpar('float','99.','','''data clip percentile (default is 99)'''))
sfseisthr.par('order1',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfseisthr.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseisthr.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseisthr.par('thrtype',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfseisthr.par('slet',rsf.doc.rsfpar('string ',desc='''seismic domain (auxiliary output file name)'''))
sfseisthr.par('sletthr',rsf.doc.rsfpar('string ',desc='''thresholded seislet domain (auxiliary output file name)'''))
sfseisthr.version('2.1-git')
sfseisthr.synopsis('''sfseisthr < in.rsf > out.rsf dip=dip.rsf slet=slet.rsf sletthr=sletthr.rsf eps=0.01 pclip=99. order1=1 eps=0.01 type= thrtype=''','''''')
rsf.doc.progs['sfseisthr']=sfseisthr

sfTestsolver = rsf.doc.rsfprog('sfTestsolver','user/chenyk/MTestsolver.c','''Test for conjugate gradient, steepest descent, jacobi iteration, gauss-seidel iteration, successive over relaxation (SOR) iteration ''')
sfTestsolver.version('2.1-git')
sfTestsolver.synopsis('''sfTestsolver''','''''')
rsf.doc.progs['sfTestsolver']=sfTestsolver

sfTestsolver1 = rsf.doc.rsfprog('sfTestsolver1','user/chenyk/MTestsolver1.c','''Test for conjugate gradient, steepest descent, jacobi iteration, gauss-seidel iteration, successive over relaxation (SOR) iteration ''')
sfTestsolver1.version('2.1-git')
sfTestsolver1.synopsis('''sfTestsolver1''','''''')
rsf.doc.progs['sfTestsolver1']=sfTestsolver1

sftrapepass = rsf.doc.rsfprog('sftrapepass','user/chenyk/Mtrapepass.c','''Trapezoid bandpass filter in the frequency domain. ''')
sftrapepass.version('2.1-git')
sftrapepass.synopsis('''sftrapepass < in.rsf > out.rsf''','''f1, f2, f3, f4 correspond to four key points of the trapezoid bandpass filter.''')
rsf.doc.progs['sftrapepass']=sftrapepass

sflagrange = rsf.doc.rsfprog('sflagrange','user/chenyk/Mlagrange.c','''A forward interpolation using Lagrange method. ''')
sflagrange.par('ox',rsf.doc.rsfpar('float','o1','',''''''))
sflagrange.par('dx',rsf.doc.rsfpar('float','d1','',''''''))
sflagrange.par('nx',rsf.doc.rsfpar('int','n1','',''''''))
sflagrange.version('2.1-git')
sflagrange.synopsis('''sflagrange < in.rsf > out.rsf ox=o1 dx=d1 nx=n1''','''Specify ox= dx= nx=
''')
rsf.doc.progs['sflagrange']=sflagrange

sfheatexplitest = rsf.doc.rsfprog('sfheatexplitest','user/chenyk/Mheatexplitest.c','''Solving 1-D heat equation using explicit finite difference ''')
sfheatexplitest.par('nt',rsf.doc.rsfpar('int','','','''number of temporal points '''))
sfheatexplitest.par('dt',rsf.doc.rsfpar('float','','','''temporal sampling '''))
sfheatexplitest.par('nx',rsf.doc.rsfpar('int','','','''number of spatial points '''))
sfheatexplitest.par('dx',rsf.doc.rsfpar('float','','','''spatial sampling '''))
sfheatexplitest.version('2.1-git')
sfheatexplitest.synopsis('''sfheatexplitest > out.rsf nt= dt= nx= dx=''','''\partial(u)/\partial(t)=a^2\partial^2(u)/\partial(x^2), 0<x<l & t>0,
u(0,t)=u(l,t)=0, t>0, 
u(x,0)=f(x), 0<=x<=l.  ''')
rsf.doc.progs['sfheatexplitest']=sfheatexplitest

sfheatimplitest = rsf.doc.rsfprog('sfheatimplitest','user/chenyk/Mheatimplitest.c','''Solving 1-D heat equation using implicit finite difference ''')
sfheatimplitest.par('nt',rsf.doc.rsfpar('int','','','''number of temporal points '''))
sfheatimplitest.par('dt',rsf.doc.rsfpar('float','','','''temporal sampling '''))
sfheatimplitest.par('nx',rsf.doc.rsfpar('int','','','''number of spatial points '''))
sfheatimplitest.par('dx',rsf.doc.rsfpar('float','','','''spatial sampling '''))
sfheatimplitest.version('2.1-git')
sfheatimplitest.synopsis('''sfheatimplitest > out.rsf nt= dt= nx= dx=''','''\partial(u)/\partial(t)=a^2\partial^2(u)/\partial(x^2), 0<x<l & t>0,
u(0,t)=u(l,t)=0, t>0, 
u(x,0)=f(x), 0<=x<=l.  ''')
rsf.doc.progs['sfheatimplitest']=sfheatimplitest

sfhyperdif = rsf.doc.rsfprog('sfhyperdif','user/chenyk/Mhyperdif.c','''Solving 1-D transportation equation using finite difference algorithm ''')
sfhyperdif.par('dinit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfhyperdif.par('dtrue',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfhyperdif.par('wanttrue',rsf.doc.rsfpar('bool','n','[y/n]','''if want true solution. y: want, n: don't want. '''))
sfhyperdif.par('wantinit',rsf.doc.rsfpar('bool','n','[y/n]','''if want initial value. y: want, n: don't want. '''))
sfhyperdif.par('nt',rsf.doc.rsfpar('int','','','''number of temporal points '''))
sfhyperdif.par('dt',rsf.doc.rsfpar('float','','','''temporal sampling '''))
sfhyperdif.par('ox',rsf.doc.rsfpar('float','','','''spatial starting point '''))
sfhyperdif.par('nx',rsf.doc.rsfpar('int','','','''number of spatial points '''))
sfhyperdif.par('dx',rsf.doc.rsfpar('float','','','''spatial sampling '''))
sfhyperdif.par('type',rsf.doc.rsfpar('string ',desc='''[upwind, friedrichs, wendroff] get the type for solving hyperbola partial differential equation, the default is upwind '''))
sfhyperdif.version('2.1-git')
sfhyperdif.synopsis('''sfhyperdif > out.rsf dinit=dinit.rsf dtrue=dtrue.rsf wanttrue=n wantinit=n nt= dt= ox= nx= dx= type=''','''\partial(u)/\partial(t)+a(x,t)\partial(u)/\partial(x), 0<t<=T, x->unlimited,
u(x,0)=f(x).  ''')
rsf.doc.progs['sfhyperdif']=sfhyperdif

sfzerotrace = rsf.doc.rsfprog('sfzerotrace','user/chenyk/Mzerotrace.c','''Zero part of traces in order to make aliasing ''')
sfzerotrace.par('beg',rsf.doc.rsfpar('float','o2','','''zero part beginning point '''))
sfzerotrace.par('j',rsf.doc.rsfpar('int','2','','''jump step between two consecutive zero parts '''))
sfzerotrace.par('l',rsf.doc.rsfpar('int','1','','''length of each zero part '''))
sfzerotrace.version('2.1-git')
sfzerotrace.synopsis('''sfzerotrace < in.rsf > out.rsf beg=o2 j=2 l=1''','''''')
rsf.doc.progs['sfzerotrace']=sfzerotrace

sfhilbert = rsf.doc.rsfprog('sfhilbert','user/chenyk/Mhilbert.c','''Compute hilbert transform using different methods. ''')
sfhilbert.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order if type=m '''))
sfhilbert.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) if type=m '''))
sfhilbert.par('phase',rsf.doc.rsfpar('float','90.','','''phase shift (in degrees) '''))
sfhilbert.par('type',rsf.doc.rsfpar('string ',desc='''Choosing hilbert transform method, type=t means time domain, 
       type=f means freqency domain, type=m means using more robust algorithm
       the default is type=m '''))
sfhilbert.version('2.1-git')
sfhilbert.synopsis('''sfhilbert < in.rsf > out.rsf order=100 ref=1. phase=90. type=''','''type=t -> time domain convolution
type=f -> frequency domain multiplication and use FFT
type=m -> closed-form design of maximally flat FIR hilbert transformer
''')
rsf.doc.progs['sfhilbert']=sfhilbert

sfcdivdir = rsf.doc.rsfprog('sfcdivdir','user/chenyk/Mcdivdir.c','''Direct division for complex data. ''')
sfcdivdir.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdivdir.version('2.1-git')
sfcdivdir.synopsis('''sfcdivdir < fnum.rsf den=fden.rsf > frat.rsf''','''''')
rsf.doc.progs['sfcdivdir']=sfcdivdir

sfcabs = rsf.doc.rsfprog('sfcabs','user/chenyk/Mcabs.c','''Absolute value complex data. ''')
sfcabs.version('2.1-git')
sfcabs.synopsis('''sfcabs < fin.rsf > fout.rsf''','''''')
rsf.doc.progs['sfcabs']=sfcabs

sfcemd1 = rsf.doc.rsfprog('sfcemd1','user/chenyk/Mcemd1.c','''Bivariate empirical mode decomposition using first algorithm. ''')
sfcemd1.par('threshold',rsf.doc.rsfpar('float','DEFAULT_THRESHOLD','','''Sifting stoping parameter: threshold, the default is 0.05. '''))
sfcemd1.par('tolerance',rsf.doc.rsfpar('float','DEFAULT_TOLERANCE','','''Sifting stoping parameter: tolerance, the default is 0.05. '''))
sfcemd1.par('miter',rsf.doc.rsfpar('int','MAX_ITERATIONS','','''Maximum number of iterations during sifting, the default is 1000. '''))
sfcemd1.par('mimf',rsf.doc.rsfpar('int','0','','''Maximum number of IMFs, the default is as many as possible. '''))
sfcemd1.par('nbdir',rsf.doc.rsfpar('int','DEFAULT_NBPHASES','','''Number of directions used to compute the local mean, the default is 4. '''))
sfcemd1.version('2.1-git')
sfcemd1.synopsis('''sfcemd1 < inp.rsf > outp.rsf threshold=DEFAULT_THRESHOLD tolerance=DEFAULT_TOLERANCE miter=MAX_ITERATIONS mimf=0 nbdir=DEFAULT_NBPHASES''','''''')
rsf.doc.progs['sfcemd1']=sfcemd1

sfcemd2 = rsf.doc.rsfprog('sfcemd2','user/chenyk/Mcemd2.c','''Bivariate empirical mode decomposition using second algorithm. ''')
sfcemd2.par('threshold',rsf.doc.rsfpar('float','DEFAULT_THRESHOLD','','''Sifting stoping parameter: threshold, the default is 0.05. '''))
sfcemd2.par('tolerance',rsf.doc.rsfpar('float','DEFAULT_TOLERANCE','','''Sifting stoping parameter: tolerance, the default is 0.05. '''))
sfcemd2.par('miter',rsf.doc.rsfpar('int','MAX_ITERATIONS','','''Maximum number of iterations during sifting, the default is 1000. '''))
sfcemd2.par('mimf',rsf.doc.rsfpar('int','0','','''Maximum number of IMFs, the default is as many as possible. '''))
sfcemd2.par('nbdir',rsf.doc.rsfpar('int','DEFAULT_NBPHASES','','''Number of directions used to compute the local mean, the default is 4. '''))
sfcemd2.version('2.1-git')
sfcemd2.synopsis('''sfcemd2 < inp.rsf > outp.rsf threshold=DEFAULT_THRESHOLD tolerance=DEFAULT_TOLERANCE miter=MAX_ITERATIONS mimf=0 nbdir=DEFAULT_NBPHASES''','''''')
rsf.doc.progs['sfcemd2']=sfcemd2

sfsnr2 = rsf.doc.rsfprog('sfsnr2','user/chenyk/Msnr2.c','''Compute signal-noise-ratio.''')
sfsnr2.par('noise',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsnr2.version('2.1-git')
sfsnr2.synopsis('''sfsnr2 < signal.rsf noise=noise.rsf > snrf.rsf''','''SNR=10 log10(sum(clean)/sum(noise))''')
rsf.doc.progs['sfsnr2']=sfsnr2

sfsnr3 = rsf.doc.rsfprog('sfsnr3','user/chenyk/Msnr3.c','''Compute signal-noise-ratio.''')
sfsnr3.par('noise',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsnr3.version('2.1-git')
sfsnr3.synopsis('''sfsnr3 < signal.rsf noise=noise.rsf > snrf.rsf''','''SNR=10 log10(sum(clean)/sum(noise))''')
rsf.doc.progs['sfsnr3']=sfsnr3

sfsnrcyk = rsf.doc.rsfprog('sfsnrcyk','user/chenyk/Msnrcyk.c','''Compute signal-noise-ratio.''')
sfsnrcyk.par('noisy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsnrcyk.version('2.1-git')
sfsnrcyk.synopsis('''sfsnrcyk < signal.rsf noisy=noise.rsf > snrf.rsf''','''SNR=10 log10(sum(clean)/sum(noise))''')
rsf.doc.progs['sfsnrcyk']=sfsnrcyk

sfpreerror = rsf.doc.rsfprog('sfpreerror','user/chenyk/Mpreerror.c','''Prediction error ''')
sfpreerror.par('predict',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpreerror.par('type',rsf.doc.rsfpar('int','1','','''if compute relative error, 1: yes, 0: no, default is yes. '''))
sfpreerror.version('2.1-git')
sfpreerror.synopsis('''sfpreerror < in.rsf predict=pre.rsf > out.rsf type=1''','''''')
rsf.doc.progs['sfpreerror']=sfpreerror

sfthreshold1 = rsf.doc.rsfprog('sfthreshold1','user/chenyk/Mthreshold1.c','''Soft or hard thresholding using exact-value or percentile thresholding.''')
sfthreshold1.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfthreshold1.par('ifperc',rsf.doc.rsfpar('int','1','','''0, exact-value thresholding; 1, percentile thresholding. '''))
sfthreshold1.par('ifverb',rsf.doc.rsfpar('int','0','','''0, not print threshold value; 1, print threshold value. '''))
sfthreshold1.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfthreshold1.par('type',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfthreshold1.par('other',rsf.doc.rsfpar('string ',desc='''If output the difference between the thresholded part and the original one (auxiliary output file name)'''))
sfthreshold1.version('2.1-git')
sfthreshold1.synopsis('''sfthreshold1 < in.rsf > out.rsf other=other.rsf ifperc=1 ifverb=0 thr= type=''','''When type=soft and ifperc=1, sfthreshold1 is equal to sfthreshold.
''')
rsf.doc.progs['sfthreshold1']=sfthreshold1

sftsmf = rsf.doc.rsfprog('sftsmf','user/chenyk/Mtsmf.c','''Two-step space varying median filtering. ''')
sftsmf.par('L',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftsmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sftsmf.par('ns',rsf.doc.rsfpar('int','0','','''processing window starting point, corresponding to the temporal axis '''))
sftsmf.par('ne',rsf.doc.rsfpar('int','n2-1','','''processing window ending point, corresponding to the temporal axis, n2 means transposed first-axis dimension. '''))
sftsmf.par('N',rsf.doc.rsfpar('int','(f2-f1+1)*n1','','''average energy level (AEL) computing number '''))
sftsmf.par('ael',rsf.doc.rsfpar('float','0.0','','''get the average energy level (AEL) empirically defined '''))
sftsmf.par('verb',rsf.doc.rsfpar('bool','n','','''if print the computed average energy level (AEL) '''))
sftsmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>l4, positive and odd integer)'''))
sftsmf.par('l1',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l1" (default=2)'''))
sftsmf.par('l2',rsf.doc.rsfpar('int','0','','''space-varying window parameter "l2" (default=0)'''))
sftsmf.par('l3',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l3" (default=2)'''))
sftsmf.par('l4',rsf.doc.rsfpar('int','4','','''space-varying window parameter "l4" (default=4)'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftsmf.version('2.1-git')
sftsmf.synopsis('''sftsmf < in.rsf > out.rsf L=lengthout.rsf boundary=n ns=0 ne=n2-1 N=(f2-f1+1)*n1 ael=0.0 verb=n nfw= l1=2 l2=0 l3=2 l4=4''','''In default case, sftsmf is equal to sftvmf.
''')
rsf.doc.progs['sftsmf']=sftsmf

sffxdecon = rsf.doc.rsfprog('sffxdecon','user/chenyk/Mfxdecon.c','''Random noise attenuation using f-x deconvolution ''')
sffxdecon.par('verb',rsf.doc.rsfpar('bool','n','','''flag to get advisory messages '''))
sffxdecon.par('taper',rsf.doc.rsfpar('float','.1','','''length of taper '''))
sffxdecon.par('fmin',rsf.doc.rsfpar('float','1.','','''minimum frequency to process in Hz '''))
sffxdecon.par('fmax',rsf.doc.rsfpar('float','1./(2*dt)','','''maximum frequency to process in Hz '''))
sffxdecon.par('twlen',rsf.doc.rsfpar('float','(float)(n1-1)*dt','','''time window length '''))
sffxdecon.par('n2w',rsf.doc.rsfpar('int','10','','''number of traces in window '''))
sffxdecon.par('lenf',rsf.doc.rsfpar('int','4','','''number of traces for filter '''))
sffxdecon.version('2.1-git')
sffxdecon.synopsis('''sffxdecon < in.rsf > out.rsf verb=n taper=.1 fmin=1. fmax=1./(2*dt) twlen=(float)(n1-1)*dt n2w=10 lenf=4''','''''')
rsf.doc.progs['sffxdecon']=sffxdecon

sfsimidenoise = rsf.doc.rsfprog('sfsimidenoise','user/chenyk/Msimidenoise.c','''Random noise attenuation using local similarity ''')
sfsimidenoise.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfsimidenoise.version('2.1-git')
sfsimidenoise.synopsis('''sfsimidenoise < in.rsf > out.rsf similarity=simi.rsf thr=''','''''')
rsf.doc.progs['sfsimidenoise']=sfsimidenoise

sfbin2rsf = rsf.doc.rsfprog('sfbin2rsf','user/chenyk/Mbin2rsf.c','''Binary file to RSF file ''')
sfbin2rsf.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfbin2rsf.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfbin2rsf.par('d1',rsf.doc.rsfpar('float','0.004','',''''''))
sfbin2rsf.par('d2',rsf.doc.rsfpar('float','1','',''''''))
sfbin2rsf.par('o1',rsf.doc.rsfpar('float','0','',''''''))
sfbin2rsf.par('o2',rsf.doc.rsfpar('float','0','',''''''))
sfbin2rsf.par('bfile',rsf.doc.rsfpar('string ',desc=''''''))
sfbin2rsf.version('2.1-git')
sfbin2rsf.synopsis('''sfbin2rsf > out.rsf n1= n2= d1=0.004 d2=1 o1=0 o2=0 bfile=''','''Convert a file containing a two dimensional array of binary floats to 
.rsf format.  n1*n2*sizeof(float) bytes are read from the input file
and the rsf file is written to standard output.  If you have a higher
dimension file (3d, 4d, ..) you can change n2, n3, etc using sfput.  

Example that converts and plots a binary velocity grid:

<Vp sfbin2rsf n1=400 d1=1 n2=1600 d2=1 o2=101 \\
| sfgrey color=jet scalebar=y allpos=y | sfpen

''')
rsf.doc.progs['sfbin2rsf']=sfbin2rsf

sfrsf2bin = rsf.doc.rsfprog('sfrsf2bin','user/chenyk/Mrsf2bin.c','''RSF file to Binary file ''')
sfrsf2bin.par('bfile',rsf.doc.rsfpar('string ',desc=''''''))
sfrsf2bin.version('2.1-git')
sfrsf2bin.synopsis('''sfrsf2bin < in.rsf bfile=''','''''')
rsf.doc.progs['sfrsf2bin']=sfrsf2bin

sfhalfthr = rsf.doc.rsfprog('sfhalfthr','user/chenyk/Mhalfthr.c','''Half thresholding using exact-value or percentile thresholding.''')
sfhalfthr.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfhalfthr.par('ifverb',rsf.doc.rsfpar('int','0','','''0, not print threshold value; 1, print threshold value. '''))
sfhalfthr.par('ifperc',rsf.doc.rsfpar('int','1','','''0, exact-value thresholding; 1, percentile thresholding. '''))
sfhalfthr.par('thr',rsf.doc.rsfpar('float','','','''thresholding level '''))
sfhalfthr.par('other',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfhalfthr.version('2.1-git')
sfhalfthr.synopsis('''sfhalfthr < in.rsf > out.rsf other=other.rsf ifverb=0 ifperc=1 thr=''','''''')
rsf.doc.progs['sfhalfthr']=sfhalfthr

sfhradon = rsf.doc.rsfprog('sfhradon','user/chenyk/Mhradon.c','''Time domain high-resolution hyperbolic Radon transform. ''')
sfhradon.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhradon.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhradon.par('inv',rsf.doc.rsfpar('bool','y','','''if implement the inverse transform '''))
sfhradon.par('adj',rsf.doc.rsfpar('bool','n','','''if implement the adjoint transform instead of the inverse transform '''))
sfhradon.par('solver',rsf.doc.rsfpar('bool','n','','''if use Madagascar bigsolver, default is not '''))
sfhradon.par('v0',rsf.doc.rsfpar('float','','',''''''))
sfhradon.par('dv',rsf.doc.rsfpar('float','','',''''''))
sfhradon.par('nv',rsf.doc.rsfpar('int','','',''''''))
sfhradon.par('N1',rsf.doc.rsfpar('int','10','','''CG Iterations (Internal loop) '''))
sfhradon.par('N2',rsf.doc.rsfpar('int','3','','''Update of weights for the sparse solution, N1 = 1 LS , N2 > 3 for High Res (Sparse) solution '''))
sfhradon.par('verb',rsf.doc.rsfpar('int','0','','''If output the debugging process '''))
sfhradon.par('h0',rsf.doc.rsfpar('float','','',''''''))
sfhradon.par('dh',rsf.doc.rsfpar('float','','',''''''))
sfhradon.par('nh',rsf.doc.rsfpar('int','','',''''''))
sfhradon.par('vel',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhradon.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhradon.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhradon.version('2.1-git')
sfhradon.synopsis('''sfhradon < in.rsf > out.rsf vel=vel.rsf offset=offset.rsf inv=y adj=n solver=n v0= dv= nv= N1=10 N2=3 verb=0 h0= dh= nh=''','''m(tau,p) = \sum_{ih=1}^{nh} d(tau=\sqrt{tau^2+h[ih]^2/p^2),h}
inv=true do inverse
adj=true do adjoint
inv=false && adj=false do forward
''')
rsf.doc.progs['sfhradon']=sfhradon

sfsuplane = rsf.doc.rsfprog('sfsuplane','user/chenyk/Msuplane.c','''Create common offset data file with up to 3 planes ''')
sfsuplane.par('nt',rsf.doc.rsfpar('int','NT','',''''''))
sfsuplane.par('ntr',rsf.doc.rsfpar('int','NTR','',''''''))
sfsuplane.par('dt',rsf.doc.rsfpar('float','DT','',''''''))
sfsuplane.par('offset',rsf.doc.rsfpar('float','OFF','',''''''))
sfsuplane.par('npl',rsf.doc.rsfpar('int','NPL','',''''''))
sfsuplane.par('taper',rsf.doc.rsfpar('int','0','','''set defaults and/or get parameters for plane 1 '''))
sfsuplane.par('dip1',rsf.doc.rsfpar('float','0','',''''''))
sfsuplane.par('len1',rsf.doc.rsfpar('int','3*ntr/4','',''''''))
sfsuplane.par('ct1',rsf.doc.rsfpar('int','nt/2-1','',''''''))
sfsuplane.par('cx1',rsf.doc.rsfpar('int','ntr/2-1','','''set defaults and/or get parameters for plane 2 '''))
sfsuplane.par('dip2',rsf.doc.rsfpar('float','4','',''''''))
sfsuplane.par('len2',rsf.doc.rsfpar('int','3*ntr/4','',''''''))
sfsuplane.par('ct2',rsf.doc.rsfpar('int','nt/2-1','',''''''))
sfsuplane.par('cx2',rsf.doc.rsfpar('int','ntr/2-1','','''set defaults and/or get parameters for plane 3 '''))
sfsuplane.par('dip3',rsf.doc.rsfpar('float','8','',''''''))
sfsuplane.par('len3',rsf.doc.rsfpar('int','3*ntr/4','',''''''))
sfsuplane.par('ct3',rsf.doc.rsfpar('int','nt/2-1','',''''''))
sfsuplane.par('cx3',rsf.doc.rsfpar('int','ntr/2-1','','''check if user wants the special output specified '''))
sfsuplane.par('liner',rsf.doc.rsfpar('int','0','',''''''))
sfsuplane.version('2.1-git')
sfsuplane.synopsis('''sfsuplane > out.rsf nt=NT ntr=NTR dt=DT offset=OFF npl=NPL taper=0 dip1=0 len1=3*ntr/4 ct1=nt/2-1 cx1=ntr/2-1 dip2=4 len2=3*ntr/4 ct2=nt/2-1 cx2=ntr/2-1 dip3=8 len3=3*ntr/4 ct3=nt/2-1 cx3=ntr/2-1 liner=0''','''Command line should be: sfsuplane in=NULL >file.rsf 
(There should be at least one parameter in command line because of sf_init(argc,argv))
''')
rsf.doc.progs['sfsuplane']=sfsuplane

sfsimidenoise1 = rsf.doc.rsfprog('sfsimidenoise1','user/chenyk/Msimidenoise1.c','''Random noise attenuation using local similarity (different weighting approach) ''')
sfsimidenoise1.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise1.par('s1',rsf.doc.rsfpar('float','','','''thresholding level 1 '''))
sfsimidenoise1.par('s2',rsf.doc.rsfpar('float','','','''thresholding level 2 '''))
sfsimidenoise1.version('2.1-git')
sfsimidenoise1.synopsis('''sfsimidenoise1 < in.rsf > out.rsf similarity=simi.rsf s1= s2=''','''The weighting function is defined as
W(s) = 1				if s>s2
	 = (s-s1)/(s2-s1)	if s1<=s<=s2
	 = 0				if s<s1
''')
rsf.doc.progs['sfsimidenoise1']=sfsimidenoise1

sfrmtrace = rsf.doc.rsfprog('sfrmtrace','user/chenyk/Mrmtrace.c','''Remove part of traces (resample) in order to make aliasing ''')
sfrmtrace.par('factor',rsf.doc.rsfpar('int','2','','''zero part beginning point '''))
sfrmtrace.version('2.1-git')
sfrmtrace.synopsis('''sfrmtrace < in.rsf > out.rsf factor=2''','''''')
rsf.doc.progs['sfrmtrace']=sfrmtrace

sfprekirch = rsf.doc.rsfprog('sfprekirch','user/chenyk/Mprekirch.c','''2-D Prestack Kirchhoff time migration with antialiasing. ''')
sfprekirch.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfprekirch.par('nz',rsf.doc.rsfpar('int','nt','',''''''))
sfprekirch.par('dz',rsf.doc.rsfpar('float','dt','',''''''))
sfprekirch.par('z0',rsf.doc.rsfpar('float','t0','',''''''))
sfprekirch.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfprekirch.version('2.1-git')
sfprekirch.synopsis('''sfprekirch < inp.rsf vel=vel.rsf > mig.rsf nz=nt dz=dt z0=t0 antialias=1.0''','''The axes in the input are {time,midpoint,offset}
The axes in the output are {time,midpoint}
''')
rsf.doc.progs['sfprekirch']=sfprekirch

sfpsmig = rsf.doc.rsfprog('sfpsmig','user/chenyk/Mpsmig.c','''2-D Phase-shift modeling and migration. ''')
sfpsmig.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpsmig.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag, 0: modeling, 1: migration '''))
sfpsmig.par('nw',rsf.doc.rsfpar('int','','',''''''))
sfpsmig.par('dw',rsf.doc.rsfpar('float','','',''''''))
sfpsmig.par('eps',rsf.doc.rsfpar('float','0.1f','','''stabilization parameter '''))
sfpsmig.version('2.1-git')
sfpsmig.synopsis('''sfpsmig < inp.rsf > out.rsf vel=vel.rsf adj=n nw= dw= eps=0.1f''','''''')
rsf.doc.progs['sfpsmig']=sfpsmig

sfpocssemb = rsf.doc.rsfprog('sfpocssemb','user/chenyk/Mpocssemb.c','''POCS using semblance thresholding or amplitude thresholding.''')
sfpocssemb.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocssemb.par('spec2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpocssemb.par('spec1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpocssemb.par('snr',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpocssemb.par('true',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocssemb.par('niter',rsf.doc.rsfpar('int','10','','''Get the number of iterations '''))
sfpocssemb.par('ifsnr',rsf.doc.rsfpar('int','0','','''If compute SNR during iteration '''))
sfpocssemb.par('pmin',rsf.doc.rsfpar('float','-2','','''minimum p '''))
sfpocssemb.par('np',rsf.doc.rsfpar('int','nx','','''number of p '''))
sfpocssemb.par('type',rsf.doc.rsfpar('string ',desc='''[amplitude, semblance] thresholding type, the default is amplitude thresholding  '''))
sfpocssemb.par('spec2',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpocssemb.par('spec1',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpocssemb.par('true',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocssemb.par('spec2',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpocssemb.par('spec1',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpocssemb.par('true',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocssemb.par('true',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocssemb.version('2.1-git')
sfpocssemb.synopsis('''sfpocssemb < inp.rsf mask=m.rsf > outp.rsf spec2=spec2.rsf spec1=spec1.rsf snr=snr.rsf true=trued.rsf niter=10 ifsnr=0 pmin=-2 np=nx type=''','''''')
rsf.doc.progs['sfpocssemb']=sfpocssemb

sfafd2d = rsf.doc.rsfprog('sfafd2d','user/chenyk/Mafd2d.c','''2D coustic time-domain FD modeling with different boundary conditions''')
sfafd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfafd2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfafd2d.par('verb',rsf.doc.rsfpar('bool','0','',''''''))
sfafd2d.par('free',rsf.doc.rsfpar('bool','n','',''''''))
sfafd2d.par('ifoneway',rsf.doc.rsfpar('bool','y','',''''''))
sfafd2d.par('ifsponge',rsf.doc.rsfpar('bool','y','',''''''))
sfafd2d.par('nb',rsf.doc.rsfpar('int','5','','''setup I/O files '''))
sfafd2d.version('2.1-git')
sfafd2d.synopsis('''sfafd2d < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=0 free=n ifoneway=y ifsponge=y nb=5''','''''')
rsf.doc.progs['sfafd2d']=sfafd2d

sfprekirchsr = rsf.doc.rsfprog('sfprekirchsr','user/chenyk/Mprekirchsr.c','''2-D Prestack Kirchhoff time migration with antialiasing in source-receiver domain. ''')
sfprekirchsr.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfprekirchsr.par('nz',rsf.doc.rsfpar('int','nt','',''''''))
sfprekirchsr.par('dz',rsf.doc.rsfpar('float','dt','',''''''))
sfprekirchsr.par('z0',rsf.doc.rsfpar('float','t0','',''''''))
sfprekirchsr.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfprekirchsr.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfprekirchsr.version('2.1-git')
sfprekirchsr.synopsis('''sfprekirchsr vel=vel.rsf < inp.rsf > outp.rsf nz=nt dz=dt z0=t0 adj=n antialias=1.0''','''The axes in the input are {time,receiver,source}
The axes in the output are {time,receiver}
I(t0,x0)=\int (W(t0,y0,s,r) * u(s,r,T(s,t0,x0)+T(r,t0,x0)) dsdr
''')
rsf.doc.progs['sfprekirchsr']=sfprekirchsr

sfsimpostkirch = rsf.doc.rsfprog('sfsimpostkirch','user/chenyk/Msimpostkirch.c','''2-D simplest-form post-stack Kirchhoff time modeling and migration. ''')
sfsimpostkirch.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimpostkirch.par('adj',rsf.doc.rsfpar('bool','y','','''yes: migration, no: modeling '''))
sfsimpostkirch.par('aa',rsf.doc.rsfpar('bool','n','','''yes: apply reciprocal antialiaising operator '''))
sfsimpostkirch.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfsimpostkirch.par('v0',rsf.doc.rsfpar('float','','','''constant velocity (if no velocity=) '''))
sfsimpostkirch.par('vel',rsf.doc.rsfpar('string ',desc='''velocity file (auxiliary input file name)'''))
sfsimpostkirch.version('2.1-git')
sfsimpostkirch.synopsis('''sfsimpostkirch < in.rsf > out.rsf vel=vel.rsf adj=y aa=n sw=0 v0=''','''Suppose the input_image & output_data or input_data & output_image have the same dimensions, samplings.
The dottest has been past. ''')
rsf.doc.progs['sfsimpostkirch']=sfsimpostkirch

sfpresr = rsf.doc.rsfprog('sfpresr','user/chenyk/Mpresr.c','''2-D simplest-form post-stack Kirchhoff time modeling and migration. ''')
sfpresr.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpresr.par('adj',rsf.doc.rsfpar('bool','y','','''yes: migration, no: modeling '''))
sfpresr.par('aa',rsf.doc.rsfpar('bool','n','','''yes: apply reciprocal antialiaising operator '''))
sfpresr.par('sw',rsf.doc.rsfpar('int','0','','''if > 0, select a branch of the antialiasing operation '''))
sfpresr.par('v0',rsf.doc.rsfpar('float','','','''constant velocity (if no velocity=) '''))
sfpresr.par('vel',rsf.doc.rsfpar('string ',desc='''velocity file (auxiliary input file name)'''))
sfpresr.version('2.1-git')
sfpresr.synopsis('''sfpresr < in.rsf > out.rsf vel=vel.rsf adj=y aa=n sw=0 v0=''','''Suppose the input_image & output_data or input_data & output_image have the same dimensions, samplings.
The dottest has been past. ''')
rsf.doc.progs['sfpresr']=sfpresr

sfnlm1 = rsf.doc.rsfprog('sfnlm1','user/chenyk/Mnlm1.c','''1D non-local median filtering. ''')
sfnlm1.par('t',rsf.doc.rsfpar('int','5','','''radio of search window '''))
sfnlm1.par('f',rsf.doc.rsfpar('int','2','','''radio of similarity window '''))
sfnlm1.par('h',rsf.doc.rsfpar('float','0.5','','''degree of filtering '''))
sfnlm1.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfnlm1.version('2.1-git')
sfnlm1.synopsis('''sfnlm1 < in.rsf > out.rsf t=5 f=2 h=0.5 boundary=n''','''''')
rsf.doc.progs['sfnlm1']=sfnlm1

sfnlm2 = rsf.doc.rsfprog('sfnlm2','user/chenyk/Mnlm2.c','''2D non-local median filtering. ''')
sfnlm2.par('t1',rsf.doc.rsfpar('int','5','','''radio of search window '''))
sfnlm2.par('t2',rsf.doc.rsfpar('int','5','','''radio of search window '''))
sfnlm2.par('f1',rsf.doc.rsfpar('int','2','','''radio of similarity window '''))
sfnlm2.par('f2',rsf.doc.rsfpar('int','2','','''radio of similarity window '''))
sfnlm2.par('h',rsf.doc.rsfpar('float','0.5','','''degree of filtering '''))
sfnlm2.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfnlm2.version('2.1-git')
sfnlm2.synopsis('''sfnlm2 < in.rsf > out.rsf t1=5 t2=5 f1=2 f2=2 h=0.5 boundary=n''','''''')
rsf.doc.progs['sfnlm2']=sfnlm2

sfdblendseis = rsf.doc.rsfprog('sfdblendseis','user/chenyk/Mdblendseis.c','''Blending, or Deblending using seislet domain thresholding.''')
sfdblendseis.par('shottime',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdblendseis.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdblendseis.par('init',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdblendseis.par('niter',rsf.doc.rsfpar('int','30','','''number of iterations '''))
sfdblendseis.par('thr',rsf.doc.rsfpar('float','10','','''threshold value (coefficients preserved in percentage) '''))
sfdblendseis.par('lambda',rsf.doc.rsfpar('float','0.5','','''update step size '''))
sfdblendseis.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfdblendseis.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfdblendseis.par('verb',rsf.doc.rsfpar('int','0','','''output verbosity information '''))
sfdblendseis.par('mode',rsf.doc.rsfpar('string ',desc='''[b-blending,d-deblending] function mode, the default is d  '''))
sfdblendseis.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfdblendseis.par('thrtype',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfdblendseis.par('init',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdblendseis.version('2.1-git')
sfdblendseis.synopsis('''sfdblendseis < in.rsf > out.rsf shottime=shottime.rsf dip=dip.rsf init=init.rsf niter=30 thr=10 lambda=0.5 eps=0.01 order=1 verb=0 mode= type= thrtype=''','''''')
rsf.doc.progs['sfdblendseis']=sfdblendseis

sfsvmf = rsf.doc.rsfprog('sfsvmf','user/chenyk/Msvmf.c','''Space varying median filtering. ''')
sfsvmf.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsvmf.par('L',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsvmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfsvmf.par('ns',rsf.doc.rsfpar('int','0','','''processing window starting point, corresponding to the temporal axis '''))
sfsvmf.par('ne',rsf.doc.rsfpar('int','n2-1','','''processing window ending point, corresponding to the temporal axis, n2 means transposed first-axis dimension. '''))
sfsvmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>l4, positive and odd integer)'''))
sfsvmf.par('l1',rsf.doc.rsfpar('int','4','','''space-varying window parameter "l1" (default=4)'''))
sfsvmf.par('l2',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l2" (default=2)'''))
sfsvmf.par('l3',rsf.doc.rsfpar('int','2','','''space-varying window parameter "l3" (default=2)'''))
sfsvmf.par('l4',rsf.doc.rsfpar('int','4','','''space-varying window parameter "l4" (default=4)'''))
sfsvmf.par('lambda1',rsf.doc.rsfpar('float','0.15','','''space-varying window parameter "lambda1" (default=0.15)'''))
sfsvmf.par('lambda2',rsf.doc.rsfpar('float','0.25','','''space-varying window parameter "lambda2" (default=0.25)'''))
sfsvmf.par('lambda3',rsf.doc.rsfpar('float','0.75','','''space-varying window parameter "lambda3" (default=0.75)'''))
sfsvmf.par('lambda4',rsf.doc.rsfpar('float','0.85','','''space-varying window parameter "lambda4" (default=0.85)'''))
sfsvmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfsvmf.par('L',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfsvmf.version('2.1-git')
sfsvmf.synopsis('''sfsvmf < in.rsf > out.rsf similarity=similarity.rsf L=lengthout.rsf boundary=n ns=0 ne=n2-1 nfw= l1=4 l2=2 l3=2 l4=4 lambda1=0.15 lambda2=0.25 lambda3=0.75 lambda4=0.85''','''Using local similarity as a reference.
''')
rsf.doc.progs['sfsvmf']=sfsvmf

sfgenshotscyk = rsf.doc.rsfprog('sfgenshotscyk','user/chenyk/Mgenshotscyk.c','''Generate shots for FWI test ''')
sfgenshotscyk.par('wfd',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshotscyk.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfgenshotscyk.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgenshotscyk.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgenshotscyk.par('ns',rsf.doc.rsfpar('int','','','''number of shots '''))
sfgenshotscyk.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfgenshotscyk.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfgenshotscyk.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfgenshotscyk.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgenshotscyk.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgenshotscyk.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgenshotscyk.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgenshotscyk.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgenshotscyk.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgenshotscyk.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgenshotscyk.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgenshotscyk.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfgenshotscyk.version('2.1-git')
sfgenshotscyk.synopsis('''sfgenshotscyk < vel.rsf > shots.rsf wfd=wfd.rsf verb=y nt= ng= ns= dt= amp=1000 fm=10 jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''''')
rsf.doc.progs['sfgenshotscyk']=sfgenshotscyk

sfafd2domp = rsf.doc.rsfprog('sfafd2domp','user/chenyk/Mafd2domp.c','''2D coustic time-domain FD modeling with different boundary conditions using OpenMP''')
sfafd2domp.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfafd2domp.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfafd2domp.par('verb',rsf.doc.rsfpar('bool','0','',''''''))
sfafd2domp.par('free',rsf.doc.rsfpar('bool','n','',''''''))
sfafd2domp.par('ifoneway',rsf.doc.rsfpar('bool','y','',''''''))
sfafd2domp.par('ifsponge',rsf.doc.rsfpar('bool','y','',''''''))
sfafd2domp.par('nb',rsf.doc.rsfpar('int','5','','''setup I/O files '''))
sfafd2domp.version('2.1-git')
sfafd2domp.synopsis('''sfafd2domp < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=0 free=n ifoneway=y ifsponge=y nb=5''','''''')
rsf.doc.progs['sfafd2domp']=sfafd2domp

sflow = rsf.doc.rsfprog('sflow','user/chenyk/Mlow.c','''Calculating local (signal-and-noise) orthogonalization weight (LOW)  ''')
sflow.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflow.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflow.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflow.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflow.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sflow.version('2.1-git')
sflow.synopsis('''sflow < fnoi.rsf sig=fsig.rsf > flow.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sflow']=sflow

sfaddtrace = rsf.doc.rsfprog('sfaddtrace','user/chenyk/Maddtrace.c','''Add zero trace to original profile in order to improve lateral resolution ''')
sfaddtrace.par('ratio',rsf.doc.rsfpar('int','2','',''''''))
sfaddtrace.version('2.1-git')
sfaddtrace.synopsis('''sfaddtrace < in.rsf > out.rsf ratio=2''','''''')
rsf.doc.progs['sfaddtrace']=sfaddtrace

sfmatlr = rsf.doc.rsfprog('sfmatlr','user/chenyk/Mmatlr.c','''Flip a matrix ''')
sfmatlr.version('2.1-git')
sfmatlr.synopsis('''sfmatlr < Fin.rsf > Fout.rsf''','''''')
rsf.doc.progs['sfmatlr']=sfmatlr

sfpnmomf = rsf.doc.rsfprog('sfpnmomf','user/chenyk/Mpnmomf.c','''Normal moveout.''')
sfpnmomf.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmomf.par('s',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmomf.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmomf.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmomf.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpnmomf.par('str',rsf.doc.rsfpar('float','0.5','','''maximum stretch allowed '''))
sfpnmomf.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfpnmomf.par('CDPtype',rsf.doc.rsfpar('int','','',''''''))
sfpnmomf.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfpnmomf.par('squared',rsf.doc.rsfpar('bool','n','','''if y, the slowness or velocity is squared '''))
sfpnmomf.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfpnmomf.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfpnmomf.par('s',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmomf.par('a',rsf.doc.rsfpar('string ',desc=''''''))
sfpnmomf.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmomf.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmomf.version('2.1-git')
sfpnmomf.synopsis('''sfpnmomf < cmp.rsf velocity=velocity.rsf > nmod.rsf s=het.rsf offset=offset.rsf mask=msk.rsf half=y str=0.5 mute=12 CDPtype= slowness=n squared=n h0=0. extend=4 a=''','''
Compatible with sfvscan.

Copyright (C) 2004 University of Texas at Austin

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
''')
rsf.doc.progs['sfpnmomf']=sfpnmomf

sfexpd = rsf.doc.rsfprog('sfexpd','user/chenyk/Mexpd.c','''Expand 2D data corret version with true spatial cooridinates  ''')
sfexpd.par('left',rsf.doc.rsfpar('int','0.5*nx','',''''''))
sfexpd.par('right',rsf.doc.rsfpar('int','0.5*nx','',''''''))
sfexpd.par('top',rsf.doc.rsfpar('int','0','',''''''))
sfexpd.par('bottom',rsf.doc.rsfpar('int','0','',''''''))
sfexpd.version('2.1-git')
sfexpd.synopsis('''sfexpd > out.rsf < in.rsf left=0.5*nx right=0.5*nx top=0 bottom=0''','''''')
rsf.doc.progs['sfexpd']=sfexpd

sfdiffcxx = rsf.doc.rsfprog('sfdiffcxx','user/chenyk/Mdiffcxx.cc','''Compare the difference of two rsf data sets with the same size. ''')
sfdiffcxx.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdiffcxx.version('2.1-git')
sfdiffcxx.synopsis('''sfdiffcxx < inp1.rsf match=inp2.rsf > dif.rsf''','''''')
rsf.doc.progs['sfdiffcxx']=sfdiffcxx

sfpyran = rsf.doc.rsfprog('sfpyran','user/chenyk/Mpyran.py','''Add random noise using python.''')
sfpyran.par('axis',rsf.doc.rsfpar('int','2','',''''''))
sfpyran.par('range',rsf.doc.rsfpar('float','1','','''noise range (default=1)'''))
sfpyran.par('seed',rsf.doc.rsfpar('int','n2','','''random seed (default=n2)'''))
sfpyran.par('type',rsf.doc.rsfpar('string','y','','''noise type, y: normal, n: uniform'''))
sfpyran.par('mean',rsf.doc.rsfpar('float','0','','''noise mean (default=0)'''))
sfpyran.par('var',rsf.doc.rsfpar('float','1','','''noise variance (default=1)'''))
sfpyran.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise'''))
sfpyran.version('2.1-git')
sfpyran.synopsis('''sfpyran < pi.rsf > po.rsf axis=2 range=1 seed=n2 type=y mean=0 var=1 rep=n''','''''')
rsf.doc.progs['sfpyran']=sfpyran

