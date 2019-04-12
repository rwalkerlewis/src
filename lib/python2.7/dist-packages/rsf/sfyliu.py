import rsf.doc

sfapef = rsf.doc.rsfprog('sfapef','user/yliu/Mapef.c','''Estimate adaptive nonstationary PEF on aliased traces. ''')
sfapef.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef.par('maskin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfapef.par('maskout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef.par('a',rsf.doc.rsfpar('ints','','',''' [ndim]'''))
sfapef.par('jump',rsf.doc.rsfpar('int','2','','''Jump parameter '''))
sfapef.par('dim',rsf.doc.rsfpar('int','mdim','','''number of dimensions '''))
sfapef.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfapef.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfapef.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfapef.par('maskin',rsf.doc.rsfpar('string ',desc='''optional input mask file (auxiliary input file name)'''))
sfapef.par('maskout',rsf.doc.rsfpar('string ',desc='''optional output mask file (auxiliary output file name)'''))
sfapef.version('2.1-git')
sfapef.synopsis('''sfapef < mat.rsf > flt.rsf pred=pre.rsf maskin=maskin.rsf maskout=maskout.rsf a= jump=2 dim=mdim niter=100 verb=n''','''''')
rsf.doc.progs['sfapef']=sfapef

sfapef2 = rsf.doc.rsfprog('sfapef2','user/yliu/Mapef2.c','''2D adaptive nonstationary PEF on aliased traces. ''')
sfapef2.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef2.par('maskin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfapef2.par('maskout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfapef2.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sfapef2.par('jump',rsf.doc.rsfpar('int','2','','''Jump parameter '''))
sfapef2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfapef2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfapef2.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfapef2.par('maskin',rsf.doc.rsfpar('string ',desc='''optional input mask file (auxiliary input file name)'''))
sfapef2.par('maskout',rsf.doc.rsfpar('string ',desc='''optional output mask file (auxiliary output file name)'''))
sfapef2.version('2.1-git')
sfapef2.synopsis('''sfapef2 < mat.rsf > flt.rsf pred=pre.rsf maskin=maskin.rsf maskout=maskout.rsf a= jump=2 niter=100 verb=n''','''''')
rsf.doc.progs['sfapef2']=sfapef2

sfapefsignoi = rsf.doc.rsfprog('sfapefsignoi','user/yliu/Mapefsignoi.c','''Signal and noise separation using adaptive PEFs. ''')
sfapefsignoi.par('sfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfapefsignoi.par('nfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfapefsignoi.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfapefsignoi.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfapefsignoi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfapefsignoi.version('2.1-git')
sfapefsignoi.synopsis('''sfapefsignoi < in.rsf sfilt=sfilt.rsf nfilt=nfilt.rsf > out.rsf niter=100 eps=0. verb=n''','''''')
rsf.doc.progs['sfapefsignoi']=sfapefsignoi

sfatm1 = rsf.doc.rsfprog('sfatm1','user/yliu/Matm1.c','''1D alpha-trimmed-mean filtering. ''')
sfatm1.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfatm1.par('alpha',rsf.doc.rsfpar('float','','','''0.0 <= alpha <= 0.5: median filter (alpha=0.5); mean filter (alpha=0.) '''))
sfatm1.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfatm1.version('2.1-git')
sfatm1.synopsis('''sfatm1 < in.rsf > out.rsf nfw= alpha= boundary=n''','''median filter (alpha=0.5); mean filter (alpha=0.)
''')
rsf.doc.progs['sfatm1']=sfatm1

sfatm2 = rsf.doc.rsfprog('sfatm2','user/yliu/Matm2.c','''2D alpha-trimmed-mean filtering. ''')
sfatm2.par('nfw1',rsf.doc.rsfpar('int','','','''filter-window length in n1 direction (positive and odd integer)'''))
sfatm2.par('nfw2',rsf.doc.rsfpar('int','nfw1','','''filter-window length in n2 direction (default=nfw1)'''))
sfatm2.par('alpha',rsf.doc.rsfpar('float','','','''0.0 <= alpha <= 0.5: median filter (alpha=0.5); mean filter (alpha=0.)'''))
sfatm2.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfatm2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfatm2.par('type',rsf.doc.rsfpar('string ',desc='''[rectangular,cross] 2-D window type, the default is rectangular  '''))
sfatm2.version('2.1-git')
sfatm2.synopsis('''sfatm2 < in.rsf > out.rsf nfw1= nfw2=nfw1 alpha= boundary=n verb=n type=''','''1D filter (nfw2=1); 2D filter (otherwise)
median filter (alpha=0.5); mean filter (alpha=0.)
''')
rsf.doc.progs['sfatm2']=sfatm2

sfbilstack = rsf.doc.rsfprog('sfbilstack','user/yliu/Mbilstack.c','''Bilateral stacking. ''')
sfbilstack.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbilstack.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfbilstack.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfbilstack.par('bilat',rsf.doc.rsfpar('bool','n','','''if y, bilateral smoothing '''))
sfbilstack.par('ax',rsf.doc.rsfpar('float','','','''Gaussian weight for the range distance '''))
sfbilstack.par('bx',rsf.doc.rsfpar('float','','','''Exponential weight for the domain distance '''))
sfbilstack.version('2.1-git')
sfbilstack.synopsis('''sfbilstack < in.rsf > out.rsf weight=weight.rsf verb=n niter=20 bilat=n ax= bx=''','''''')
rsf.doc.progs['sfbilstack']=sfbilstack

sfc1coh = rsf.doc.rsfprog('sfc1coh','user/yliu/Mc1coh.c','''C1 coherency algorithm. ''')
sfc1coh.par('ntw',rsf.doc.rsfpar('int','3','','''Temporal length of the correlation window (default=3) '''))
sfc1coh.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfc1coh.par('lag1',rsf.doc.rsfpar('int','3','','''Inline time lag (default=3) '''))
sfc1coh.par('lag2',rsf.doc.rsfpar('int','3','','''Crossline time lag (default=3) '''))
sfc1coh.version('2.1-git')
sfc1coh.synopsis('''sfc1coh < in.rsf > out.rsf ntw=3 verb=y lag1=3 lag2=3''','''''')
rsf.doc.progs['sfc1coh']=sfc1coh

sfdifference = rsf.doc.rsfprog('sfdifference','user/yliu/Mdifference.c','''Difference profile of two data ''')
sfdifference.par('subtracter',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdifference.version('2.1-git')
sfdifference.synopsis('''sfdifference < in.rsf > out.rsf subtracter=sub.rsf''','''''')
rsf.doc.progs['sfdifference']=sfdifference

sfdoeps = rsf.doc.rsfprog('sfdoeps','user/yliu/Mdoeps.c','''2D dip-oriented edge-preserving smoothing (DOEPS). ''')
sfdoeps.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdoeps.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer) '''))
sfdoeps.par('nw',rsf.doc.rsfpar('int','','','''data-window length (positive and odd integer) '''))
sfdoeps.par('boundary',rsf.doc.rsfpar('bool','y','','''if y, boundary is data, whereas zero'''))
sfdoeps.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdoeps.version('2.1-git')
sfdoeps.synopsis('''sfdoeps < in.rsf > out.rsf dip=dip.rsf nfw= nw= boundary=y verb=n''','''''')
rsf.doc.progs['sfdoeps']=sfdoeps

sfdomf = rsf.doc.rsfprog('sfdomf','user/yliu/Mdomf.c','''2D dip-oriented median/mean filter (DOMF). ''')
sfdomf.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdomf.par('nw',rsf.doc.rsfpar('int','','','''data-window length (positive and odd integer) '''))
sfdomf.par('boundary',rsf.doc.rsfpar('bool','y','','''if y, boundary is data, whereas zero'''))
sfdomf.par('stack',rsf.doc.rsfpar('bool','n','','''if y, mean filter, whereas median filter'''))
sfdomf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdomf.version('2.1-git')
sfdomf.synopsis('''sfdomf < in.rsf > out.rsf dip=dip.rsf nw= boundary=y stack=n verb=n''','''''')
rsf.doc.progs['sfdomf']=sfdomf

sfdominantf = rsf.doc.rsfprog('sfdominantf','user/yliu/Mdominantf.c','''Calculate dominant frequency of amplitude spectra dataset.''')
sfdominantf.version('2.1-git')
sfdominantf.synopsis('''sfdominantf < in.rsf''','''''')
rsf.doc.progs['sfdominantf']=sfdominantf

sfdonf = rsf.doc.rsfprog('sfdonf','user/yliu/Mdonf.c','''2D dip-oriented nonlocal (bilateral) smoothing. ''')
sfdonf.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdonf.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer) '''))
sfdonf.par('nw',rsf.doc.rsfpar('int','','','''data-window length (positive and odd integer) '''))
sfdonf.par('boundary',rsf.doc.rsfpar('bool','y','','''if y, boundary is data, whereas zero'''))
sfdonf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdonf.par('bx',rsf.doc.rsfpar('float','','','''exponential weight for the domain distance (different if gaussian)'''))
sfdonf.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, Gaussian weight, whereas Triangle weight '''))
sfdonf.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfdonf.par('ax',rsf.doc.rsfpar('float','','','''Gaussian weight for the range distance '''))
sfdonf.version('2.1-git')
sfdonf.synopsis('''sfdonf < in.rsf > out.rsf dip=dip.rsf nfw= nw= boundary=y verb=n bx= gauss=n repeat=1 ax=''','''''')
rsf.doc.progs['sfdonf']=sfdonf

sfdowmf = rsf.doc.rsfprog('sfdowmf','user/yliu/Mdowmf.c','''2D dip-oriented weighted median filter (DOWMF). ''')
sfdowmf.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdowmf.par('nw',rsf.doc.rsfpar('int','','','''data-window length (positive and odd integer) '''))
sfdowmf.par('rect',rsf.doc.rsfpar('int','nw','','''Correlation window '''))
sfdowmf.par('boundary',rsf.doc.rsfpar('bool','y','','''if y, boundary is data, whereas zero'''))
sfdowmf.par('var',rsf.doc.rsfpar('bool','n','','''if y, variance weights, whereas correlation weights'''))
sfdowmf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdowmf.version('2.1-git')
sfdowmf.synopsis('''sfdowmf < in.rsf > out.rsf dip=dip.rsf nw= rect=nw boundary=y var=n verb=n''','''''')
rsf.doc.progs['sfdowmf']=sfdowmf

sfduffing = rsf.doc.rsfprog('sfduffing','user/yliu/Mduffing.c','''Duffing differential equation solved by 4th order Runge-Kutta method. ''')
sfduffing.par('sfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfduffing.par('gamma',rsf.doc.rsfpar('float','0.75','','''strength of external force'''))
sfduffing.par('omega',rsf.doc.rsfpar('float','1','','''angular frequence of external force'''))
sfduffing.par('kxi',rsf.doc.rsfpar('float','1','','''adjustment for input signal'''))
sfduffing.par('x0',rsf.doc.rsfpar('float','0','','''initial value of x0'''))
sfduffing.par('y0',rsf.doc.rsfpar('float','0','','''initial value of y0'''))
sfduffing.par('pow1',rsf.doc.rsfpar('int','1','','''power of first non-linear restitution term'''))
sfduffing.par('pow2',rsf.doc.rsfpar('int','3','','''power of second non-linear restitution term'''))
sfduffing.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfduffing.par('ricker',rsf.doc.rsfpar('bool','n','','''if y need extenal input for external force '''))
sfduffing.par('sfile',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfduffing.version('2.1-git')
sfduffing.synopsis('''sfduffing < in.rsf > out.rsf sfile=sfile.rsf gamma=0.75 omega=1 kxi=1 x0=0 y0=0 pow1=1 pow2=3 verb=n ricker=n''','''Duffing equation: x'' + 0.5 x' - x + x^3 = gamma cos(omega t) + kxi input(t)
''')
rsf.doc.progs['sfduffing']=sfduffing

sfduffing1 = rsf.doc.rsfprog('sfduffing1','user/yliu/Mduffing1.c','''1D signal analysis by using Duffing differential equation solved by 4th order Runge-Kutta method. ''')
sfduffing1.par('restor',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfduffing1.par('gamma',rsf.doc.rsfpar('float','0.75','','''strength of external force'''))
sfduffing1.par('omega',rsf.doc.rsfpar('float','1','','''angular frequence of external force'''))
sfduffing1.par('kxi',rsf.doc.rsfpar('float','1','','''adjustment for input signal'''))
sfduffing1.par('x0',rsf.doc.rsfpar('float','0','','''initial value of x0'''))
sfduffing1.par('y0',rsf.doc.rsfpar('float','0','','''initial value of y0'''))
sfduffing1.par('pow1',rsf.doc.rsfpar('int','1','','''power of first non-linear restitution term'''))
sfduffing1.par('pow2',rsf.doc.rsfpar('int','3','','''power of second non-linear restitution term'''))
sfduffing1.par('phi',rsf.doc.rsfpar('float','0.','','''phase of cosine signal unit=pi'''))
sfduffing1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfduffing1.par('cosine',rsf.doc.rsfpar('bool','y','','''if n need extenal input for periodic restoring force '''))
sfduffing1.par('restor',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfduffing1.version('2.1-git')
sfduffing1.synopsis('''sfduffing1 < in.rsf > out.rsf restor=restor.rsf gamma=0.75 omega=1 kxi=1 x0=0 y0=0 pow1=1 pow2=3 phi=0. verb=n cosine=y''','''Duffing equation: x''/(omega^2)+0.5 x'/omega-x+x^3=gamma cos(omega t+phi)+kxi R(t)
''')
rsf.doc.progs['sfduffing1']=sfduffing1

sfduffing2 = rsf.doc.rsfprog('sfduffing2','user/yliu/Mduffing2.c','''2D/3D Velocity analysis by using Duffing differential equation solved by 4th order Runge-Kutta method. ''')
sfduffing2.par('restor',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfduffing2.par('winsz',rsf.doc.rsfpar('int','200','','''for each trace,the width of window. Unit:samples'''))
sfduffing2.par('v0',rsf.doc.rsfpar('float','1000','','''init Vel for velocity scan '''))
sfduffing2.par('dv',rsf.doc.rsfpar('float','20','','''step lenth for velocity scan '''))
sfduffing2.par('vn',rsf.doc.rsfpar('int','100','','''numbers of velscan'''))
sfduffing2.par('t0',rsf.doc.rsfpar('float','o1','','''t0 scan start point '''))
sfduffing2.par('deltat0',rsf.doc.rsfpar('float','dt','','''step lenth for t0 scan '''))
sfduffing2.par('t0n',rsf.doc.rsfpar('int','n1','','''numbers of t0scan'''))
sfduffing2.par('gamma',rsf.doc.rsfpar('float','0.75','','''strength of external force'''))
sfduffing2.par('omega',rsf.doc.rsfpar('float','1','','''angular frequence of external force'''))
sfduffing2.par('kxi',rsf.doc.rsfpar('float','1','','''adjustment for input signal'''))
sfduffing2.par('x0',rsf.doc.rsfpar('float','0','','''initial value of x0'''))
sfduffing2.par('y0',rsf.doc.rsfpar('float','0','','''initial value of y0'''))
sfduffing2.par('pow1',rsf.doc.rsfpar('int','1','','''power of first non-linear restitution term'''))
sfduffing2.par('pow2',rsf.doc.rsfpar('int','3','','''power of second non-linear restitution term'''))
sfduffing2.par('phi',rsf.doc.rsfpar('float','0.','','''phase of cosine signal unit=pi'''))
sfduffing2.par('cosine',rsf.doc.rsfpar('bool','y','','''if n need extenal input for periodic restoring force '''))
sfduffing2.par('delta',rsf.doc.rsfpar('float','0.01','','''The density of judgement grid'''))
sfduffing2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfduffing2.par('gx',rsf.doc.rsfpar('float','2.0','','''Size of grid'''))
sfduffing2.par('restor',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfduffing2.version('2.1-git')
sfduffing2.synopsis('''sfduffing2 < cmp.rsf > outf.rsf restor=restor.rsf winsz=200 v0=1000 dv=20 vn=100 t0=o1 deltat0=dt t0n=n1 gamma=0.75 omega=1 kxi=1 x0=0 y0=0 pow1=1 pow2=3 phi=0. cosine=y delta=0.01 verb=n gx=2.0''','''Duffing equation: x''/(omega^2)+0.5 x'/omega-x+x^3=gamma cos(omega t+phi)+kxi R(t)
''')
rsf.doc.progs['sfduffing2']=sfduffing2

sfduwt = rsf.doc.rsfprog('sfduwt','user/yliu/Mduwt.c','''1-D digital undecimated (stationary) wavelet transform by lifting scheme ''')
sfduwt.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfduwt.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfduwt.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfduwt.par('scale',rsf.doc.rsfpar('int','max','','''decomposition scale '''))
sfduwt.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfduwt.version('2.1-git')
sfduwt.synopsis('''sfduwt < in.rsf > out.rsf inv=n adj=n unit=n scale=max type=''','''''')
rsf.doc.progs['sfduwt']=sfduwt

sfdwt2 = rsf.doc.rsfprog('sfdwt2','user/yliu/Mdwt2.c','''1-D digital wavelet transform (another version)''')
sfdwt2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfdwt2.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfdwt2.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfdwt2.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfdwt2.version('2.1-git')
sfdwt2.synopsis('''sfdwt2 < in.rsf > out.rsf inv=n adj=n unit=n type=''','''Forward transform (adj=y inv=y)   m=T[d]
Adjoint transform (adj=y inv=n)   m=T^(-1)'[d]
Inverse transform (adj=n inv=y/n) d=T^(-1)[m]
''')
rsf.doc.progs['sfdwt2']=sfdwt2

sfdwt97 = rsf.doc.rsfprog('sfdwt97','user/yliu/Mdwt97.c','''1-D CDF 9/7 biorthogonal digital wavelet transform ''')
sfdwt97.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfdwt97.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfdwt97.version('2.1-git')
sfdwt97.synopsis('''sfdwt97 < in.rsf > out.rsf inv=n adj=n''','''''')
rsf.doc.progs['sfdwt97']=sfdwt97

sfepsf = rsf.doc.rsfprog('sfepsf','user/yliu/Mepsf.c','''1-D and 2-D edge-preserving smoothing (EPS) filter. ''')
sfepsf.par('nfw1',rsf.doc.rsfpar('int','','','''filter-window length in n1 direction (positive and odd integer) '''))
sfepsf.par('nfw2',rsf.doc.rsfpar('int','1','','''filter-window length in n2 direction (default=1, 1D case)'''))
sfepsf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfepsf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfepsf.par('weight',rsf.doc.rsfpar('bool','n','','''Gaussian weight flag (only for stack) '''))
sfepsf.par('sigma',rsf.doc.rsfpar('float','3.','','''Gaussian weight radius (only for stack) '''))
sfepsf.par('type',rsf.doc.rsfpar('string ',desc='''[stack,median] filter choice, the default is stack (mean) '''))
sfepsf.version('2.1-git')
sfepsf.synopsis('''sfepsf < in.rsf > out.rsf nfw1= nfw2=1 boundary=n verb=n weight=n sigma=3. type=''','''1D filter (nfw2=1); 2D filter (otherwise)
''')
rsf.doc.progs['sfepsf']=sfepsf

sffagrad = rsf.doc.rsfprog('sffagrad','user/yliu/Mfagrad.c','''Calculating frequency attenuation gradient. ''')
sffagrad.par('grad',rsf.doc.rsfpar('bool','y','','''If y, output attenuation gradient; if n, output absorption factor '''))
sffagrad.par('lperc',rsf.doc.rsfpar('float','65.','','''Low percentage of total energy '''))
sffagrad.par('hperc',rsf.doc.rsfpar('float','85.','','''High percentage of total energy '''))
sffagrad.par('freq',rsf.doc.rsfpar('float','','','''Frequency corresponding to energy ratio, valid when type=ratio '''))
sffagrad.par('type',rsf.doc.rsfpar('string ',desc='''[low,full,ratio,attenuation] attribute type, the default is attenuation  '''))
sffagrad.version('2.1-git')
sffagrad.synopsis('''sffagrad < in.rsf > out.rsf grad=y lperc=65. hperc=85. freq= type=''','''''')
rsf.doc.progs['sffagrad']=sffagrad

sffbpick = rsf.doc.rsfprog('sffbpick','user/yliu/Mfbpick.c','''First break picking from instantaneous traveltime attribute. ''')
sffbpick.par('type',rsf.doc.rsfpar('string ',desc='''[traveltime,position] type, the default is traveltime  '''))
sffbpick.version('2.1-git')
sffbpick.synopsis('''sffbpick < in.rsf > out.rsf type=''','''''')
rsf.doc.progs['sffbpick']=sffbpick

sffindwellcoord = rsf.doc.rsfprog('sffindwellcoord','user/yliu/Mfindwellcoord.c','''Find well location by using well coordinates. ''')
sffindwellcoord.par('xcoord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffindwellcoord.par('ycoord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffindwellcoord.par('wellx',rsf.doc.rsfpar('float','','','''X coordinate for well '''))
sffindwellcoord.par('welly',rsf.doc.rsfpar('float','','','''Y coordinate for well '''))
sffindwellcoord.version('2.1-git')
sffindwellcoord.synopsis('''sffindwellcoord xcoord=xcoord.rsf ycoord=ycoord.rsf wellx= welly=''','''''')
rsf.doc.progs['sffindwellcoord']=sffindwellcoord

sffkoclet = rsf.doc.rsfprog('sffkoclet','user/yliu/Mfkoclet.c','''1-D seislet transform using omega-wavenumber offset continuation ''')
sffkoclet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffkoclet.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sffkoclet.par('dwt',rsf.doc.rsfpar('bool','n','','''if y, do wavelet transform '''))
sffkoclet.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffkoclet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffkoclet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sffkoclet.version('2.1-git')
sffkoclet.synopsis('''sffkoclet < in.rsf > out.rsf inv=n adj=n dwt=n verb=y eps=0.01 type=''','''Forward transform (adj=n inv=y/n) m=T[d]
Inverse transform (adj=y inv=y)   d=T^(-1)[d]
Adjoint transform (adj=y inv=n)   d=T'[d]
''')
rsf.doc.progs['sffkoclet']=sffkoclet

sffkoclet3 = rsf.doc.rsfprog('sffkoclet3','user/yliu/Mfkoclet3.c','''2-D seislet transform using frequency-wavenumber offset-azimuth continuation ''')
sffkoclet3.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffkoclet3.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sffkoclet3.par('dwt',rsf.doc.rsfpar('bool','n','','''if y, do wavelet transform '''))
sffkoclet3.par('amp',rsf.doc.rsfpar('bool','n','','''if y, true amplitudes continuation '''))
sffkoclet3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffkoclet3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffkoclet3.par('maxe',rsf.doc.rsfpar('float','10.','','''stability constraint '''))
sffkoclet3.par('dir',rsf.doc.rsfpar('string ',desc='''[azimuth,offset,both] direction, the default is both directions  '''))
sffkoclet3.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sffkoclet3.version('2.1-git')
sffkoclet3.synopsis('''sffkoclet3 < in.rsf > out.rsf inv=n adj=n dwt=n amp=n verb=y eps=0.01 maxe=10. dir= type=''','''Forward transform (adj=n inv=y/n) m=T[d]
Inverse transform (adj=y inv=y)   d=T^(-1)[d]
Adjoint transform (adj=y inv=n)   d=T'[d]
''')
rsf.doc.progs['sffkoclet3']=sffkoclet3

sffourbreg2 = rsf.doc.rsfprog('sffourbreg2','user/yliu/Mfourbreg2.c','''Missing data interpolation in 2-D using Fourier Bregman shaping iteration. ''')
sffourbreg2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffourbreg2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourbreg2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sffourbreg2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourbreg2.par('error',rsf.doc.rsfpar('bool','n','','''error verbosity flag '''))
sffourbreg2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft-thresholding '''))
sffourbreg2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourbreg2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourbreg2.version('2.1-git')
sffourbreg2.synopsis('''sffourbreg2 < in.rsf > out.rsf mask=mask.rsf res=res.rsf ref=ref.rsf niter=20 verb=n error=n perc=99.''','''''')
rsf.doc.progs['sffourbreg2']=sffourbreg2

sffourmis2 = rsf.doc.rsfprog('sffourmis2','user/yliu/Mfourmis2.c','''Missing data interpolation in 2-D using Fourier transform and compressive sensing. ''')
sffourmis2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffourmis2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffourmis2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sffourmis2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffourmis2.par('error',rsf.doc.rsfpar('bool','n','','''error verbosity flag '''))
sffourmis2.par('cut',rsf.doc.rsfpar('bool','n','','''cutting verbosity flag, the default is soft-thresholding '''))
sffourmis2.par('f0',rsf.doc.rsfpar('float','0.','','''initial cutting frequency '''))
sffourmis2.par('k0',rsf.doc.rsfpar('float','0.','','''initial cutting wavenumber '''))
sffourmis2.par('parf',rsf.doc.rsfpar('float','0.','','''Ajustable parameter for frequency window, default is fixed window '''))
sffourmis2.par('parw',rsf.doc.rsfpar('float','0.','','''Ajustable parameter for wavenumber window, default is fixed window '''))
sffourmis2.par('orderf',rsf.doc.rsfpar('float','1.','','''Curve order for frequency window, default is linear '''))
sffourmis2.par('orderw',rsf.doc.rsfpar('float','1.','','''Curve order for frequency window, default is linear '''))
sffourmis2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft-thresholding '''))
sffourmis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sffourmis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sffourmis2.par('oper',rsf.doc.rsfpar('string ',desc='''[shaping,pocs,bregman] method, the default is shaping '''))
sffourmis2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.par('res',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffourmis2.version('2.1-git')
sffourmis2.synopsis('''sffourmis2 < in.rsf > out.rsf mask=mask.rsf res=res.rsf ref=ref.rsf niter=20 verb=n error=n cut=n f0=0. k0=0. parf=0. parw=0. orderf=1. orderw=1. perc=99. ordert=1. ordert=1. oper=''','''''')
rsf.doc.progs['sffourmis2']=sffourmis2

sffreqreg = rsf.doc.rsfprog('sffreqreg','user/yliu/Mfreqreg.c','''Local frequency interpolation. ''')
sffreqreg.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreqreg.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sffreqreg.par('dw',rsf.doc.rsfpar('float','','','''frequency step '''))
sffreqreg.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sffreqreg.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius '''))
sffreqreg.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sffreqreg.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sffreqreg.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffreqreg.version('2.1-git')
sffreqreg.synopsis('''sffreqreg < in.rsf > out.rsf mask=mask.rsf nw= dw= w0=0. rect=10 niter=100 verb=n''','''''')
rsf.doc.progs['sffreqreg']=sffreqreg

sffreshape = rsf.doc.rsfprog('sffreshape','user/yliu/Mfreshape.c','''Nonstationary spectral balancing in frequency domain. ''')
sffreshape.par('in2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('out2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffreshape.par('dim',rsf.doc.rsfpar('int','1','','''data dimensionality '''))
sffreshape.par('in2',rsf.doc.rsfpar('string ',desc='''optional second input file (auxiliary input file name)'''))
sffreshape.version('2.1-git')
sffreshape.synopsis('''sffreshape < in.rsf in2=in2.rsf ma=ma.rsf ma2=ma2.rsf > out.rsf out2=out2.rsf dim=1''','''''')
rsf.doc.progs['sffreshape']=sffreshape

sfgeoconvert = rsf.doc.rsfprog('sfgeoconvert','user/yliu/Mgeoconvert.c','''2-D regular geometry conversion ''')
sfgeoconvert.par('ns',rsf.doc.rsfpar('int','','','''shot number '''))
sfgeoconvert.par('nr',rsf.doc.rsfpar('int','','','''receiver number per shot '''))
sfgeoconvert.par('ds',rsf.doc.rsfpar('float','0.05','','''shot interval '''))
sfgeoconvert.par('dr',rsf.doc.rsfpar('float','0.025','','''receiver interval '''))
sfgeoconvert.par('os',rsf.doc.rsfpar('float','0.','','''shot origin '''))
sfgeoconvert.par('or',rsf.doc.rsfpar('float','0.','','''receiver origin '''))
sfgeoconvert.version('2.1-git')
sfgeoconvert.synopsis('''sfgeoconvert < in.rsf > out.rsf ns= nr= ds=0.05 dr=0.025 os=0. or=0.''','''''')
rsf.doc.progs['sfgeoconvert']=sfgeoconvert

sfgravcon = rsf.doc.rsfprog('sfgravcon','user/yliu/Mgravcon.c','''Continuation for gravity data by using FFT or intergral iteration ''')
sfgravcon.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfgravcon.par('iter',rsf.doc.rsfpar('bool','n','','''if y, perform iteration method '''))
sfgravcon.par('z',rsf.doc.rsfpar('float','','','''for iteration method '''))
sfgravcon.par('niter',rsf.doc.rsfpar('int','0','','''continuation factor allocate memory '''))
sfgravcon.version('2.1-git')
sfgravcon.synopsis('''sfgravcon < in.rsf > out.rsf verb=n iter=n z= niter=0''','''''')
rsf.doc.progs['sfgravcon']=sfgravcon

sfgroll = rsf.doc.rsfprog('sfgroll','user/yliu/Mgroll.c','''Add linear-chirp ground-roll noise to the data ''')
sfgroll.par('begf',rsf.doc.rsfpar('float','10.','','''beginning frequency of ground roll '''))
sfgroll.par('endf',rsf.doc.rsfpar('float','5.','','''ending frequency of ground roll '''))
sfgroll.par('theta',rsf.doc.rsfpar('float','0.2','','''direction of central ground roll '''))
sfgroll.par('alpha',rsf.doc.rsfpar('float','0.1','','''width parameter of ground roll '''))
sfgroll.par('beg1',rsf.doc.rsfpar('float','0.','','''radial beginning point at first axis '''))
sfgroll.par('beg2',rsf.doc.rsfpar('float','0.','','''radial beginning point at second axis '''))
sfgroll.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfgroll.version('2.1-git')
sfgroll.synopsis('''sfgroll < in.rsf > out.rsf begf=10. endf=5. theta=0.2 alpha=0.1 beg1=0. beg2=0. rep=n''','''''')
rsf.doc.progs['sfgroll']=sfgroll

sfhv2d = rsf.doc.rsfprog('sfhv2d','user/yliu/Mhv2d.c','''Velocity with heterogeneity convert to dip. ''')
sfhv2d.par('heterog',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhv2d.par('n',rsf.doc.rsfpar('int','32','','''offset number '''))
sfhv2d.par('d',rsf.doc.rsfpar('float','12.5','','''offset interval '''))
sfhv2d.par('o',rsf.doc.rsfpar('float','0.','','''offset origin '''))
sfhv2d.par('mute',rsf.doc.rsfpar('bool','n','','''if y, use mutter '''))
sfhv2d.par('half',rsf.doc.rsfpar('bool','n','','''if y, half-offset instead of full offset '''))
sfhv2d.par('tp',rsf.doc.rsfpar('float','0.150','','''end time (available when mute=y) '''))
sfhv2d.par('t0',rsf.doc.rsfpar('float','0.','','''starting time (available when mute=y) '''))
sfhv2d.par('v0',rsf.doc.rsfpar('float','10000','','''velocity (available when mute=y) '''))
sfhv2d.par('x0',rsf.doc.rsfpar('float','0.','','''starting space (available when mute=y) '''))
sfhv2d.par('abs',rsf.doc.rsfpar('bool','y','','''if y, use absolute value |x-x0| (available when mute=y) '''))
sfhv2d.par('inner',rsf.doc.rsfpar('bool','n','','''if y, do inner muter (available when mute=y) '''))
sfhv2d.par('hyper',rsf.doc.rsfpar('bool','n','','''if y, do hyperbolic mute (available when mute=y) '''))
sfhv2d.version('2.1-git')
sfhv2d.synopsis('''sfhv2d < in.rsf > out.rsf heterog=heterog.rsf n=32 d=12.5 o=0. mute=n half=n tp=0.150 t0=0. v0=10000 x0=0. abs=y inner=n hyper=n''','''''')
rsf.doc.progs['sfhv2d']=sfhv2d

sfjudgechaos = rsf.doc.rsfprog('sfjudgechaos','user/yliu/Mjudgechaos.c','''Judgement of chaos  ''')
sfjudgechaos.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfjudgechaos.par('gx',rsf.doc.rsfpar('float','2.0','','''Total Size of fixed grid'''))
sfjudgechaos.par('delta',rsf.doc.rsfpar('float','0.01','','''The cell size of grid'''))
sfjudgechaos.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfjudgechaos.par('fixgrid',rsf.doc.rsfpar('bool','n','','''if y ,the total size of grid determined by gx '''))
sfjudgechaos.par('ma',rsf.doc.rsfpar('bool','n','','''if y ,output auxilily file = mask'''))
sfjudgechaos.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfjudgechaos.version('2.1-git')
sfjudgechaos.synopsis('''sfjudgechaos < in.rsf > out.rsf mask=mask.rsf gx=2.0 delta=0.01 verb=n fixgrid=n ma=n''','''Input  - Complex;
Output - Float
''')
rsf.doc.progs['sfjudgechaos']=sfjudgechaos

sfinitial = rsf.doc.rsfprog('sfinitial','user/yliu/Minitial.c','''Initialize a data ''')
sfinitial.par('sign',rsf.doc.rsfpar('bool','y','','''if y, initialize data with "1", or with "0" '''))
sfinitial.version('2.1-git')
sfinitial.synopsis('''sfinitial < in.rsf > out.rsf sign=y''','''''')
rsf.doc.progs['sfinitial']=sfinitial

sfinstattr = rsf.doc.rsfprog('sfinstattr','user/yliu/Minstattr.c','''Estimate of instantaneous attributes. ''')
sfinstattr.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfinstattr.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfinstattr.par('hertz',rsf.doc.rsfpar('bool','y','','''if y, convert output to Hertz '''))
sfinstattr.par('hires',rsf.doc.rsfpar('bool','n','','''if y, compute high resolution instantaneous attributes '''))
sfinstattr.par('der2',rsf.doc.rsfpar('bool','n','','''if y, compute 2nd-order derivative to use with hires=y '''))
sfinstattr.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfinstattr.par('type',rsf.doc.rsfpar('string ',desc='''[amplitude,phase,frequency] attribute type, the default is amplitude '''))
sfinstattr.version('2.1-git')
sfinstattr.synopsis('''sfinstattr < in.rsf > out.rsf order=10 ref=1. hertz=y hires=n der2=n verb=n type=''','''''')
rsf.doc.progs['sfinstattr']=sfinstattr

sfinstsnr = rsf.doc.rsfprog('sfinstsnr','user/yliu/Minstsnr.c','''Instantaneous signal-to-noise ratio (SNR) estimation. ''')
sfinstsnr.par('en',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinstsnr.version('2.1-git')
sfinstsnr.synopsis('''sfinstsnr < in.rsf > out.rsf en=en.rsf''','''''')
rsf.doc.progs['sfinstsnr']=sfinstsnr

sfintbin4 = rsf.doc.rsfprog('sfintbin4','user/yliu/Mintbin4.c','''5-D data binning. ''')
sfintbin4.par('xkey',rsf.doc.rsfpar('int','','','''x key number (if no xk), default is fldr '''))
sfintbin4.par('ykey',rsf.doc.rsfpar('int','','','''y key number (if no yk), default is tracf '''))
sfintbin4.par('skey',rsf.doc.rsfpar('int','','','''s key number (if no sk), default is swdep '''))
sfintbin4.par('rkey',rsf.doc.rsfpar('int','','','''r key number (if no rk), default is gwdep '''))
sfintbin4.par('xmin',rsf.doc.rsfpar('int','','','''x minimum '''))
sfintbin4.par('xmax',rsf.doc.rsfpar('int','','','''x maximum '''))
sfintbin4.par('ymin',rsf.doc.rsfpar('int','','','''y minimum '''))
sfintbin4.par('ymax',rsf.doc.rsfpar('int','','','''y maximum '''))
sfintbin4.par('smin',rsf.doc.rsfpar('int','','','''s minimum '''))
sfintbin4.par('smax',rsf.doc.rsfpar('int','','','''s maximum '''))
sfintbin4.par('rmin',rsf.doc.rsfpar('int','','','''r minimum '''))
sfintbin4.par('rmax',rsf.doc.rsfpar('int','','','''r maximum '''))
sfintbin4.par('dx',rsf.doc.rsfpar('int','1','',''''''))
sfintbin4.par('dy',rsf.doc.rsfpar('int','1','',''''''))
sfintbin4.par('ds',rsf.doc.rsfpar('int','1','',''''''))
sfintbin4.par('dr',rsf.doc.rsfpar('int','1','',''''''))
sfintbin4.par('head',rsf.doc.rsfpar('string ',desc='''header file '''))
sfintbin4.par('xk',rsf.doc.rsfpar('string ',desc='''x key name '''))
sfintbin4.par('yk',rsf.doc.rsfpar('string ',desc='''y key name '''))
sfintbin4.par('sk',rsf.doc.rsfpar('string ',desc='''s key name '''))
sfintbin4.par('rk',rsf.doc.rsfpar('string ',desc='''r key name '''))
sfintbin4.par('fold',rsf.doc.rsfpar('string ',desc='''output fold file '''))
sfintbin4.version('2.1-git')
sfintbin4.synopsis('''sfintbin4 < in.rsf > out.rsf xkey= ykey= skey= rkey= xmin= xmax= ymin= ymax= smin= smax= rmin= rmax= dx=1 dy=1 ds=1 dr=1 head= xk= yk= sk= rk= fold=''','''''')
rsf.doc.progs['sfintbin4']=sfintbin4

sfinternalmult = rsf.doc.rsfprog('sfinternalmult','user/yliu/Minternalmult.c','''Generate internal multiples by using virtual seismic data. ''')
sfinternalmult.par('dif',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinternalmult.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfinternalmult.par('stack',rsf.doc.rsfpar('bool','n','','''stack flag, if y, no common multiple gather '''))
sfinternalmult.par('both',rsf.doc.rsfpar('bool','n','','''receiver flag, if y, receiver with both sides '''))
sfinternalmult.par('jumpo',rsf.doc.rsfpar('int','1','','''jump in offset dimension, only for stack=n '''))
sfinternalmult.par('jumps',rsf.doc.rsfpar('int','1','','''jump in shot dimension, only for stack=n  '''))
sfinternalmult.par('dif',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfinternalmult.version('2.1-git')
sfinternalmult.synopsis('''sfinternalmult < in.rsf > out.rsf dif=dif.rsf verb=n stack=n both=n jumpo=1 jumps=1''','''''')
rsf.doc.progs['sfinternalmult']=sfinternalmult

sfkuwahara = rsf.doc.rsfprog('sfkuwahara','user/yliu/Mkuwahara.c','''1-D and 2-D Kuwahara filter. ''')
sfkuwahara.par('nfw1',rsf.doc.rsfpar('int','','','''filter-window length in n1 direction (positive and odd integer) '''))
sfkuwahara.par('nfw2',rsf.doc.rsfpar('int','1','','''filter-window length in n2 direction (default=1, 1D case)'''))
sfkuwahara.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfkuwahara.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkuwahara.par('weight',rsf.doc.rsfpar('bool','n','','''Gaussian weight flag '''))
sfkuwahara.par('sigma',rsf.doc.rsfpar('float','3.','','''Gaussian weight radius '''))
sfkuwahara.version('2.1-git')
sfkuwahara.synopsis('''sfkuwahara < in.rsf > out.rsf nfw1= nfw2=1 boundary=n verb=n weight=n sigma=3.''','''1D filter (nfw2=1); 2D filter (otherwise)
''')
rsf.doc.progs['sfkuwahara']=sfkuwahara

sflocalsnr = rsf.doc.rsfprog('sflocalsnr','user/yliu/Mlocalsnr.c','''Local signal-to-noise ratio (SNR) estimation. ''')
sflocalsnr.par('en',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflocalsnr.par('nw',rsf.doc.rsfpar('int','','','''window length'''))
sflocalsnr.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sflocalsnr.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflocalsnr.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflocalsnr.par('stack',rsf.doc.rsfpar('bool','y','','''if y, window centre point, whereas window average'''))
sflocalsnr.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sflocalsnr.version('2.1-git')
sflocalsnr.synopsis('''sflocalsnr < in.rsf en=en.rsf > out.rsf nw= niter=100 verb=y eps=0.0f stack=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sflocalsnr']=sflocalsnr

sflocorr = rsf.doc.rsfprog('sflocorr','user/yliu/Mlocorr.c','''Local correlation measure between two datasets. ''')
sflocorr.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflocorr.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflocorr.par('rect#',rsf.doc.rsfpar('int','(1,1,1)','','''smoothing radius on #-th axis '''))
sflocorr.version('2.1-git')
sflocorr.synopsis('''sflocorr < in.rsf > out.rsf other=other.rsf verb=n rect#=(1,1,1)''','''''')
rsf.doc.progs['sflocorr']=sflocorr

sflpad2 = rsf.doc.rsfprog('sflpad2','user/yliu/Mlpad2.c','''2D pad and interleave traces.''')
sflpad2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpad2.par('jump',rsf.doc.rsfpar('int','2','','''aliasing '''))
sflpad2.version('2.1-git')
sflpad2.synopsis('''sflpad2 < in.rsf > out.rsf mask=mask.rsf jump=2''','''
Each initial trace is followed by "jump" zero traces.
''')
rsf.doc.progs['sflpad2']=sflpad2

sflpf2 = rsf.doc.rsfprog('sflpf2','user/yliu/Mlpf2.c','''2D Local prediction filter. ''')
sflpf2.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpf2.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpf2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpf2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflpf2.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflpf2.par('pef',rsf.doc.rsfpar('string ',desc='''signal PEF file (optional) '''))
sflpf2.par('lag',rsf.doc.rsfpar('string ',desc='''file with PEF lags (optional) '''))
sflpf2.version('2.1-git')
sflpf2.synopsis('''sflpf2 < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y pef= lag=''','''''')
rsf.doc.progs['sflpf2']=sflpf2

sflpfdenoise1 = rsf.doc.rsfprog('sflpfdenoise1','user/yliu/Mlpfdenoise1.c','''1D denoising using edge-preserving local polynomial fitting (ELPF). ''')
sflpfdenoise1.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer) '''))
sflpfdenoise1.par('rect',rsf.doc.rsfpar('int','','','''local smoothing radius '''))
sflpfdenoise1.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflpfdenoise1.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpfdenoise1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflpfdenoise1.version('2.1-git')
sflpfdenoise1.synopsis('''sflpfdenoise1 < in.rsf > out.rsf nfw= rect= boundary=n niter=100 verb=n''','''''')
rsf.doc.progs['sflpfdenoise1']=sflpfdenoise1

sflpfdenoise2 = rsf.doc.rsfprog('sflpfdenoise2','user/yliu/Mlpfdenoise2.c','''2D denoising using edge-preserving local polynomial fitting (ELPF). ''')
sflpfdenoise2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpfdenoise2.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer) '''))
sflpfdenoise2.par('nw',rsf.doc.rsfpar('int','','','''data-window length (positive and odd integer) '''))
sflpfdenoise2.par('rect',rsf.doc.rsfpar('int','','','''local smoothing radius '''))
sflpfdenoise2.par('boundary',rsf.doc.rsfpar('bool','y','','''if y, boundary is data, whereas zero'''))
sflpfdenoise2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpfdenoise2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflpfdenoise2.version('2.1-git')
sflpfdenoise2.synopsis('''sflpfdenoise2 < in.rsf > out.rsf dip=dip.rsf nfw= nw= rect= boundary=y niter=100 verb=n''','''''')
rsf.doc.progs['sflpfdenoise2']=sflpfdenoise2

sflrmf = rsf.doc.rsfprog('sflrmf','user/yliu/Mlrmf.c','''Local radial median filtering. ''')
sflrmf.par('nfw',rsf.doc.rsfpar('int','','','''filter window of median filter '''))
sflrmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflrmf.par('vmin',rsf.doc.rsfpar('float','','','''minimum velocity '''))
sflrmf.par('vmax',rsf.doc.rsfpar('float','','','''maximum velocity '''))
sflrmf.par('tmin',rsf.doc.rsfpar('float','','','''zero-offset time for maximum velocity '''))
sflrmf.par('tmax',rsf.doc.rsfpar('float','','','''zero-offset time for mimumum velocity '''))
sflrmf.version('2.1-git')
sflrmf.synopsis('''sflrmf < in.rsf > out.rsf nfw= boundary=n vmin= vmax= tmin= tmax=''','''''')
rsf.doc.progs['sflrmf']=sflrmf

sfltft = rsf.doc.rsfprog('sfltft','user/yliu/Mltft.c','''Local time-frequency transform (LTFT). ''')
sfltft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfltft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfltft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfltft.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sfltft.par('dw',rsf.doc.rsfpar('float','','','''frequency step '''))
sfltft.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sfltft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius (in time, samples) '''))
sfltft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfltft.par('alpha',rsf.doc.rsfpar('float','0.','','''frequency adaptivity '''))
sfltft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfltft.par('mask',rsf.doc.rsfpar('string ',desc='''data weight (auxiliary input file name)'''))
sfltft.par('weight',rsf.doc.rsfpar('string ',desc='''model weight (auxiliary input file name)'''))
sfltft.version('2.1-git')
sfltft.synopsis('''sfltft < in.rsf > out.rsf basis=basis.rsf mask=mask.rsf weight=weight.rsf inv=n verb=n nw= dw= w0=0. rect=10 niter=100 alpha=0.''','''
July 2014 program of the month:
http://ahay.org/blog/2014/07/13/program-of-the-month-sfltft/
''')
rsf.doc.progs['sfltft']=sfltft

sflum = rsf.doc.rsfprog('sflum','user/yliu/Mlum.c','''1D LUM filter''')
sflum.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sflum.par('smnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''smoother tuning parameter (1 <= smnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('shnclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''sharpener tuning parameter (1 <= shnclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflum.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflum.version('2.1-git')
sflum.synopsis('''sflum < in.rsf > out.rsf nfw= smnclip=(nfw+1)/2 shnclip=(nfw+1)/2 boundary=n''','''''')
rsf.doc.progs['sflum']=sflum

sflum2 = rsf.doc.rsfprog('sflum2','user/yliu/Mlum2.c','''2D LUM filter''')
sflum2.par('nfw1',rsf.doc.rsfpar('int','','','''filter-window length in n1 direction (positive and odd integer)'''))
sflum2.par('nfw2',rsf.doc.rsfpar('int','nfw1','','''filter-window length in n2 direction (default=nfw1)'''))
sflum2.par('smnclip',rsf.doc.rsfpar('int','(nfw1*nfw2+1)/2','','''smoother tuning parameter (1 <= smnclip <= (nfw1*nfw2+1)/2, the default is (nfw1*nfw2+1)/2)'''))
sflum2.par('shnclip',rsf.doc.rsfpar('int','(nfw1*nfw2+1)/2','','''sharpener tuning parameter (1 <= shnclip <= (nfw1*nfw2+1)/2, the default is (nfw1*nfw2+1)/2)'''))
sflum2.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflum2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflum2.par('type',rsf.doc.rsfpar('string ',desc='''[rectangular,cross] 2-D window type, the default is rectangular  '''))
sflum2.version('2.1-git')
sflum2.synopsis('''sflum2 < in.rsf > out.rsf nfw1= nfw2=nfw1 smnclip=(nfw1*nfw2+1)/2 shnclip=(nfw1*nfw2+1)/2 boundary=n verb=n type=''','''''')
rsf.doc.progs['sflum2']=sflum2

sflumsmoother = rsf.doc.rsfprog('sflumsmoother','user/yliu/Mlumsmoother.c','''1D LUM smoother filter''')
sflumsmoother.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sflumsmoother.par('nclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''tuning parameter (1 <= nclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflumsmoother.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflumsmoother.version('2.1-git')
sflumsmoother.synopsis('''sflumsmoother < in.rsf > out.rsf nfw= nclip=(nfw+1)/2 boundary=n''','''''')
rsf.doc.progs['sflumsmoother']=sflumsmoother

sflumsharpener = rsf.doc.rsfprog('sflumsharpener','user/yliu/Mlumsharpener.c','''1D LUM sharpener filter''')
sflumsharpener.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sflumsharpener.par('nclip',rsf.doc.rsfpar('int','(nfw+1)/2','','''tuning parameter (1 <= nclip <= (nfw+1)/2, the default is (nfw+1)/2)'''))
sflumsharpener.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sflumsharpener.version('2.1-git')
sflumsharpener.synopsis('''sflumsharpener < in.rsf > out.rsf nfw= nclip=(nfw+1)/2 boundary=n''','''''')
rsf.doc.progs['sflumsharpener']=sflumsharpener

sfmatchoper = rsf.doc.rsfprog('sfmatchoper','user/yliu/Mmatchoper.c','''Local matching-radon operator. ''')
sfmatchoper.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmatchoper.par('np',rsf.doc.rsfpar('int','','','''number of p values '''))
sfmatchoper.par('dp',rsf.doc.rsfpar('float','','','''p sampling '''))
sfmatchoper.par('p0',rsf.doc.rsfpar('float','','','''p origin '''))
sfmatchoper.par('shift',rsf.doc.rsfpar('int','','',''''''))
sfmatchoper.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmatchoper.par('freq',rsf.doc.rsfpar('bool','y','','''if y, parabolic Radon transform '''))
sfmatchoper.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform, only when freq=y '''))
sfmatchoper.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfmatchoper.par('rho',rsf.doc.rsfpar('bool','y','','''rho filtering, only when freq=n '''))
sfmatchoper.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing, only when freq=n '''))
sfmatchoper.par('p1',rsf.doc.rsfpar('float','0.','','''reference slope, only when freq=n '''))
sfmatchoper.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmatchoper.par('pclip',rsf.doc.rsfpar('float','100.','',''''''))
sfmatchoper.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmatchoper.version('2.1-git')
sfmatchoper.synopsis('''sfmatchoper < in.rsf > out.rsf weight=weight.rsf np= dp= p0= shift= verb=n freq=y parab=n x0=1. rho=y anti=1. p1=0. niter=100 pclip=100.''','''''')
rsf.doc.progs['sfmatchoper']=sfmatchoper

sfmean = rsf.doc.rsfprog('sfmean','user/yliu/Mmean.c','''1-D sliding-window mean filtering ''')
sfmean.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive integer)'''))
sfmean.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmean.version('2.1-git')
sfmean.synopsis('''sfmean < in.rsf > out.rsf nfw= boundary=n''','''''')
rsf.doc.progs['sfmean']=sfmean

sfmf = rsf.doc.rsfprog('sfmf','user/yliu/Mmf.c','''1D median filtering. ''')
sfmf.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmf.version('2.1-git')
sfmf.synopsis('''sfmf < in.rsf > out.rsf nfw= boundary=n''','''
January 2015 program of the month:
http://ahay.org/blog/2015/01/30/program-of-the-month-sfmf/
''')
rsf.doc.progs['sfmf']=sfmf

sfmig2 = rsf.doc.rsfprog('sfmig2','user/yliu/Mmig2.c','''2-D prestack Kirchhoff time migration with antialiasing. ''')
sfmig2.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('gather',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig2.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag (y for migration, n for modeling) '''))
sfmig2.par('normalize',rsf.doc.rsfpar('bool','y','','''normalize for the fold '''))
sfmig2.par('nh',rsf.doc.rsfpar('int','','','''number of offsets (for modeling) '''))
sfmig2.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfmig2.par('apt',rsf.doc.rsfpar('int','nx','','''integral aperture '''))
sfmig2.par('angle',rsf.doc.rsfpar('float','90.0','','''angle aperture '''))
sfmig2.par('half',rsf.doc.rsfpar('bool','y','','''if y, the third axis is half-offset instead of full offset '''))
sfmig2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfmig2.par('rho',rsf.doc.rsfpar('float','1.-1./nt','','''Leaky integration constant '''))
sfmig2.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (for modeling) '''))
sfmig2.par('h0',rsf.doc.rsfpar('float','','','''first offset (for modeling) '''))
sfmig2.par('gather',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfmig2.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmig2.version('2.1-git')
sfmig2.synopsis('''sfmig2 < inp.rsf vel=vel.rsf > out.rsf gather=gather.rsf offset=offset.rsf adj=y normalize=y nh= antialias=1.0 apt=nx angle=90.0 half=y verb=y rho=1.-1./nt dh= h0=''','''The axes in the input are {time,midpoint,offset}
The axes in the offset are {1,midpoint,offset}
The axes in the output are {time,midpoint}
The axes in the "image gather" are {time,midpoint,offset}

February 2016 program of the month:
http://ahay.org/blog/2016/02/18/program-of-the-month-sfmig2/
''')
rsf.doc.progs['sfmig2']=sfmig2

sfmiss4 = rsf.doc.rsfprog('sfmiss4','user/yliu/Mmiss4.c','''Missing data interpolation with adaptive PEFs. ''')
sfmiss4.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss4.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss4.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss4.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss4.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss4.version('2.1-git')
sfmiss4.synopsis('''sfmiss4 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss4']=sfmiss4

sfmiss43 = rsf.doc.rsfprog('sfmiss43','user/yliu/Mmiss43.c','''3-D missing data interpolation with adaptive PEFs. ''')
sfmiss43.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss43.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss43.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfmiss43.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfmiss43.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss43.version('2.1-git')
sfmiss43.synopsis('''sfmiss43 < in.rsf filt=fil.rsf > out.rsf mask=mask.rsf niter=100 exact=y eps=0. verb=n''','''''')
rsf.doc.progs['sfmiss43']=sfmiss43

sfmkcmp = rsf.doc.rsfprog('sfmkcmp','user/yliu/Mmkcmp.c','''Make a synthtic two-layer CMP gather with known t0''')
sfmkcmp.par('n1',rsf.doc.rsfpar('int','1000','','''number of n1'''))
sfmkcmp.par('n2',rsf.doc.rsfpar('int','20','','''number of n2'''))
sfmkcmp.par('dt',rsf.doc.rsfpar('float','0.001','','''sampling on 1-th axis(time)'''))
sfmkcmp.par('dx',rsf.doc.rsfpar('float','50','','''sampling on 2-th axis(offset)'''))
sfmkcmp.par('o1',rsf.doc.rsfpar('float','0','',''''''))
sfmkcmp.par('o2',rsf.doc.rsfpar('float','0','',''''''))
sfmkcmp.par('v01',rsf.doc.rsfpar('float','1000','','''first event rms vel '''))
sfmkcmp.par('v02',rsf.doc.rsfpar('float','1000','','''second event rms vel '''))
sfmkcmp.par('t01',rsf.doc.rsfpar('float','0.4','','''t01 start point '''))
sfmkcmp.par('t02',rsf.doc.rsfpar('float','0.8','','''t02 start point '''))
sfmkcmp.par('verb',rsf.doc.rsfpar('bool','n','','''dimensions '''))
sfmkcmp.version('2.1-git')
sfmkcmp.synopsis('''sfmkcmp < in.rsf > spcmp.rsf n1=1000 n2=20 dt=0.001 dx=50 o1=0 o2=0 v01=1000 v02=1000 t01=0.4 t02=0.8 verb=n''','''''')
rsf.doc.progs['sfmkcmp']=sfmkcmp

sfmlm = rsf.doc.rsfprog('sfmlm','user/yliu/Mmlm.c','''2D Multistage median filtering. ''')
sfmlm.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfmlm.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmlm.version('2.1-git')
sfmlm.synopsis('''sfmlm < in.rsf > out.rsf nfw= boundary=n''','''''')
rsf.doc.progs['sfmlm']=sfmlm

sfmtm = rsf.doc.rsfprog('sfmtm','user/yliu/Mmtm.c','''1-D and 2-D modified-trimmed-mean (MTM) filtering. ''')
sfmtm.par('nfw1',rsf.doc.rsfpar('int','','','''filter-window length in n1 direction (positive and odd integer)'''))
sfmtm.par('nfw2',rsf.doc.rsfpar('int','1','','''filter-window length in n2 direction (default=1, 1D case)'''))
sfmtm.par('pclip',rsf.doc.rsfpar('float','','','''0.0 <= pclip <= 100.0: median filter (pclip=0.); mean filter (pclip=100.) '''))
sfmtm.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmtm.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmtm.par('type',rsf.doc.rsfpar('string ',desc='''[rectangular,cross] 2-D window type, the default is rectangular  '''))
sfmtm.version('2.1-git')
sfmtm.synopsis('''sfmtm < in.rsf > out.rsf nfw1= nfw2=1 pclip= boundary=n verb=n type=''','''Also called range-trimmed-mean filter
1D filter (nfw2=1); 2D filter (otherwise)
median filter (pclip=0.); mean filter (pclip=100.)
''')
rsf.doc.progs['sfmtm']=sfmtm

sfmtres = rsf.doc.rsfprog('sfmtres','user/yliu/Mmtres.c','''Calculate apparent resistivity and phase of MT data. ''')
sfmtres.par('Ey',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmtres.par('Hx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmtres.par('Hy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmtres.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfmtres.par('comp',rsf.doc.rsfpar('bool','y','','''component selection '''))
sfmtres.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmtres.par('phase',rsf.doc.rsfpar('bool','n','','''if y, calculate apparent resistivity, otherwise calculate phase '''))
sfmtres.version('2.1-git')
sfmtres.synopsis('''sfmtres < in.rsf Ey=Ey.rsf Hx=Hx.rsf Hy=Hy.rsf > out.rsf opt=y comp=y verb=n phase=n''','''''')
rsf.doc.progs['sfmtres']=sfmtres

sfmlwm = rsf.doc.rsfprog('sfmlwm','user/yliu/Mmlwm.c','''2D Multistage weighted median filtering. ''')
sfmlwm.par('weights',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmlwm.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfmlwm.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfmlwm.version('2.1-git')
sfmlwm.synopsis('''sfmlwm < in.rsf > out.rsf weights=weights.rsf nfw= boundary=n''','''''')
rsf.doc.progs['sfmlwm']=sfmlwm

sfmultiple = rsf.doc.rsfprog('sfmultiple','user/yliu/Mmultiple.c','''2-D shot gather multiple prediction (SRMP)''')
sfmultiple.par('dif',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmultiple.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfmultiple.par('stack',rsf.doc.rsfpar('bool','n','','''stack flag, if y, no common multiple gather '''))
sfmultiple.par('both',rsf.doc.rsfpar('bool','n','','''receiver flag, if y, receiver with both sides '''))
sfmultiple.par('jumpo',rsf.doc.rsfpar('int','1','','''jump in offset dimension, only for stack=n '''))
sfmultiple.par('jumps',rsf.doc.rsfpar('int','1','','''jump in shot dimension, only for stack=n  '''))
sfmultiple.par('dif',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmultiple.version('2.1-git')
sfmultiple.synopsis('''sfmultiple < in.rsf > out.rsf dif=dif.rsf verb=n stack=n both=n jumpo=1 jumps=1''','''The axes in the input are {offset,shot,frequency}
The axes in the output are {prediction(if stack=n),offset,shot,frequency}
Requirement: offset interval = shot interval
''')
rsf.doc.progs['sfmultiple']=sfmultiple

sfmvo = rsf.doc.rsfprog('sfmvo','user/yliu/Mmvo.c','''Calculate MVO and PVO curve of CSEM data. ''')
sfmvo.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfmvo.par('log',rsf.doc.rsfpar('bool','y','','''if y, calculate logarithm of MVO '''))
sfmvo.par('mvo',rsf.doc.rsfpar('bool','y','','''if y, MVO curve; otherwise, PVO curve '''))
sfmvo.par('f',rsf.doc.rsfpar('float','0.08','','''calculate frequency '''))
sfmvo.par('nnw',rsf.doc.rsfpar('int','1600','','''sample window '''))
sfmvo.par('n',rsf.doc.rsfpar('int','1','','''number of window period '''))
sfmvo.version('2.1-git')
sfmvo.synopsis('''sfmvo < in.rsf > out.rsf opt=y log=y mvo=y f=0.08 nnw=1600 n=1''','''''')
rsf.doc.progs['sfmvo']=sfmvo

sfmvo1 = rsf.doc.rsfprog('sfmvo1','user/yliu/Mmvo1.c','''Calculate MVO and PVO curve of CSEM data (another version). ''')
sfmvo1.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfmvo1.par('log',rsf.doc.rsfpar('bool','y','','''if y, calculate logarithm of MVO '''))
sfmvo1.par('mvo',rsf.doc.rsfpar('bool','y','','''if y, MVO curve; otherwise, PVO curve '''))
sfmvo1.par('f',rsf.doc.rsfpar('float','0.08','','''calculate frequency '''))
sfmvo1.par('nnw',rsf.doc.rsfpar('int','1600','','''sample window '''))
sfmvo1.par('n',rsf.doc.rsfpar('int','1','','''number of window period '''))
sfmvo1.version('2.1-git')
sfmvo1.synopsis('''sfmvo1 < in.rsf > out.rsf opt=y log=y mvo=y f=0.08 nnw=1600 n=1''','''''')
rsf.doc.progs['sfmvo1']=sfmvo1

sfnmradon = rsf.doc.rsfprog('sfnmradon','user/yliu/Mnmradon.c','''Nonstationary-matching Radon transform. ''')
sfnmradon.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmradon.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmradon.par('adj',rsf.doc.rsfpar('bool','n','','''if y, perform adjoint operation '''))
sfnmradon.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse operation '''))
sfnmradon.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfnmradon.par('np',rsf.doc.rsfpar('int','','','''number of p values '''))
sfnmradon.par('dp',rsf.doc.rsfpar('float','','','''p sampling '''))
sfnmradon.par('p0',rsf.doc.rsfpar('float','','','''p origin '''))
sfnmradon.par('nx',rsf.doc.rsfpar('int','','','''number of x values '''))
sfnmradon.par('dx',rsf.doc.rsfpar('float','','','''x sampling '''))
sfnmradon.par('ox',rsf.doc.rsfpar('float','','','''x origin '''))
sfnmradon.par('freq',rsf.doc.rsfpar('bool','y','','''if y, parabolic Radon transform '''))
sfnmradon.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform, only when freq=y '''))
sfnmradon.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfnmradon.par('rho',rsf.doc.rsfpar('bool','y','','''rho filtering, only when freq=n '''))
sfnmradon.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing, only when freq=n '''))
sfnmradon.par('p1',rsf.doc.rsfpar('float','0.','','''reference slope, only when freq=n '''))
sfnmradon.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmradon.version('2.1-git')
sfnmradon.synopsis('''sfnmradon < in.rsf > out.rsf filt=fil.rsf weight=weight.rsf adj=n inv=n verb=n np= dp= p0= nx= dx= ox= freq=y parab=n x0=1. rho=y anti=1. p1=0.''','''''')
rsf.doc.progs['sfnmradon']=sfnmradon

sfnmult = rsf.doc.rsfprog('sfnmult','user/yliu/Mnmult.c','''Multiplication with nonstationary filter ''')
sfnmult.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmult.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfnmult.version('2.1-git')
sfnmult.synopsis('''sfnmult < inp.rsf > out.rsf filt=fil.rsf adj=n''','''''')
rsf.doc.progs['sfnmult']=sfnmult

sfnonloc = rsf.doc.rsfprog('sfnonloc','user/yliu/Mnonloc.c','''Non-local (Bilateral) smoothing. ''')
sfnonloc.par('ns',rsf.doc.rsfpar('int','','','''spray radius '''))
sfnonloc.par('bx',rsf.doc.rsfpar('float','','','''exponential weight for the domain distance (different if gaussian)'''))
sfnonloc.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, Gaussian weight, whereas Triangle weight '''))
sfnonloc.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfnonloc.par('ax',rsf.doc.rsfpar('float','','','''Gaussian weight for the range distance '''))
sfnonloc.version('2.1-git')
sfnonloc.synopsis('''sfnonloc < inp.rsf > out.rsf ns= bx= gauss=n repeat=1 ax=''','''Tomasi, C., and R. Manduchi, 1998, Bilateral filtering 
for gray and color images: Proceedings of the 1998 
IEEE International Conference on Computer Vision, 
IEEE, 836-846''')
rsf.doc.progs['sfnonloc']=sfnonloc

sfoclet = rsf.doc.rsfprog('sfoclet','user/yliu/Moclet.c','''Seislet transform in log-stretched frequency-offset-midpoint domain ''')
sfoclet.par('inv',rsf.doc.rsfpar('bool','y','','''if y, do inverse transform '''))
sfoclet.par('adj',rsf.doc.rsfpar('bool','y','','''if y, do adjoint transform '''))
sfoclet.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfoclet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfoclet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfoclet.version('2.1-git')
sfoclet.synopsis('''sfoclet < in.rsf > out.rsf inv=y adj=y unit=n verb=n type=''','''Forward transform (adj=y inv=y)   m=T[d]
Adjoint transform (adj=y inv=n)   m=T^(-1)'[d]
Inverse transform (adj=n inv=y/n) d=T^(-1)[m]
''')
rsf.doc.progs['sfoclet']=sfoclet

sfoshift1 = rsf.doc.rsfprog('sfoshift1','user/yliu/Moshift1.c','''Generate shifts with offset for 1-D regularized autoregression. ''')
sfoshift1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfoshift1.par('nf',rsf.doc.rsfpar('int','1','','''offset of first shift '''))
sfoshift1.version('2.1-git')
sfoshift1.synopsis('''sfoshift1 < in.rsf > shift.rsf ns= nf=1''','''''')
rsf.doc.progs['sfoshift1']=sfoshift1

sfpick31 = rsf.doc.rsfprog('sfpick31','user/yliu/Mpick31.c','''Automatic picking from 3D semblance-like panels plus additional axis. ''')
sfpick31.par('vel1',rsf.doc.rsfpar('float','o2','',''''''))
sfpick31.par('vel2',rsf.doc.rsfpar('float','o3','','''surface velocity '''))
sfpick31.par('rect1',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sfpick31.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick31.par('an1',rsf.doc.rsfpar('float','1.','',''''''))
sfpick31.par('an2',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick31.par('gate1',rsf.doc.rsfpar('int','3','',''''''))
sfpick31.par('gate2',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick31.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick31.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfpick31.version('2.1-git')
sfpick31.synopsis('''sfpick31 < scn.rsf > pik.rsf vel1=o2 vel2=o3 rect1=1 niter=100 an1=1. an2=1. gate1=3 gate2=3 smooth=y verb=y''','''''')
rsf.doc.progs['sfpick31']=sfpick31

sfpseudoprim = rsf.doc.rsfprog('sfpseudoprim','user/yliu/Mpseudoprim.c','''Generate pseudoprimaries using multiples''')
sfpseudoprim.par('mul',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpseudoprim.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpseudoprim.par('stack',rsf.doc.rsfpar('bool','y','','''stack flag, if y, no common pseudoprimary gather '''))
sfpseudoprim.par('both',rsf.doc.rsfpar('bool','n','','''receiver flag, if y, receiver with both sides '''))
sfpseudoprim.par('jumpo',rsf.doc.rsfpar('int','1','','''jump in offset dimension, only for stack=n '''))
sfpseudoprim.par('jumps',rsf.doc.rsfpar('int','1','','''jump in shot dimension, only for stack=n  '''))
sfpseudoprim.par('mul',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpseudoprim.version('2.1-git')
sfpseudoprim.synopsis('''sfpseudoprim < in.rsf > out.rsf mul=mul.rsf verb=n stack=y both=n jumpo=1 jumps=1''','''The axes in the input are {offset,shot,frequency}
The axes in the output are {offset,shot,frequency}
Requirement: offset interval = shot interval
''')
rsf.doc.progs['sfpseudoprim']=sfpseudoprim

sfpwcsemb = rsf.doc.rsfprog('sfpwcsemb','user/yliu/Mpwcsemb.c','''Semblance from plane-wave construction datacube. ''')
sfpwcsemb.par('nfw',rsf.doc.rsfpar('int','','','''calculation window in n1 direction (positive integer)'''))
sfpwcsemb.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfpwcsemb.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpwcsemb.version('2.1-git')
sfpwcsemb.synopsis('''sfpwcsemb < in.rsf > out.rsf nfw= boundary=n verb=n''','''''')
rsf.doc.progs['sfpwcsemb']=sfpwcsemb

sfpwd2 = rsf.doc.rsfprog('sfpwd2','user/yliu/Mpwd2.c','''2-D plane wave destruction. ''')
sfpwd2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwd2.par('order',rsf.doc.rsfpar('int','1','','''accuracy '''))
sfpwd2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpwd2.par('nj1',rsf.doc.rsfpar('int','1','','''aliasing '''))
sfpwd2.version('2.1-git')
sfpwd2.synopsis('''sfpwd2 < in.rsf dip=dip.rsf > out.rsf order=1 verb=n nj1=1''','''''')
rsf.doc.progs['sfpwd2']=sfpwd2

sfpwsfault = rsf.doc.rsfprog('sfpwsfault','user/yliu/Mpwsfault.c','''Fault detection from plane-wave spray. ''')
sfpwsfault.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwsfault.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwsfault.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwsfault.par('ns',rsf.doc.rsfpar('int','','','''spray radius '''))
sfpwsfault.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfpwsfault.par('perc',rsf.doc.rsfpar('float','98.','','''percentage for sharpen, default is 98'''))
sfpwsfault.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwsfault.par('type',rsf.doc.rsfpar('string ',desc='''[difference,sharpen_similarity] calculation type, the default is difference  '''))
sfpwsfault.version('2.1-git')
sfpwsfault.synopsis('''sfpwsfault < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 ns= niter=20 perc=98. order=1 type=''','''''')
rsf.doc.progs['sfpwsfault']=sfpwsfault

sfpwsfault3 = rsf.doc.rsfprog('sfpwsfault3','user/yliu/Mpwsfault3.c','''3-D fault detection from plane-wave spray. ''')
sfpwsfault3.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwsfault3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwsfault3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwsfault3.par('ns2',rsf.doc.rsfpar('int','','',''''''))
sfpwsfault3.par('ns3',rsf.doc.rsfpar('int','','','''spray radius '''))
sfpwsfault3.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfpwsfault3.par('perc',rsf.doc.rsfpar('float','98.','','''percentage for sharpen, default is 98'''))
sfpwsfault3.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwsfault3.par('type',rsf.doc.rsfpar('string ',desc='''[difference,sharpen_similarity] calculation type, the default is difference  '''))
sfpwsfault3.version('2.1-git')
sfpwsfault3.synopsis('''sfpwsfault3 < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 ns2= ns3= niter=20 perc=98. order=1 type=''','''''')
rsf.doc.progs['sfpwsfault3']=sfpwsfault3

sfpwsmooth3 = rsf.doc.rsfprog('sfpwsmooth3','user/yliu/Mpwsmooth3.c','''3-D structural-oriented smoothing using plane-wave spray and weighted stacking. ''')
sfpwsmooth3.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwsmooth3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpwsmooth3.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwsmooth3.par('ns2',rsf.doc.rsfpar('int','','','''spray radius (inline) '''))
sfpwsmooth3.par('ns3',rsf.doc.rsfpar('int','','','''spray radius (crossline) '''))
sfpwsmooth3.par('bilat',rsf.doc.rsfpar('bool','n','','''if y, bilateral smoothing '''))
sfpwsmooth3.par('gauss',rsf.doc.rsfpar('bool','n','','''if y, gaussian weight; otherwise, triangle weight '''))
sfpwsmooth3.par('ax',rsf.doc.rsfpar('float','','','''Gaussian weight for the range distance '''))
sfpwsmooth3.par('bx',rsf.doc.rsfpar('float','','','''exponential weight for the domain distance '''))
sfpwsmooth3.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwsmooth3.version('2.1-git')
sfpwsmooth3.synopsis('''sfpwsmooth3 < inp.rsf dip=dip.rsf > out.rsf verb=n eps=0.01 ns2= ns3= bilat=n gauss=n ax= bx= order=1''','''''')
rsf.doc.progs['sfpwsmooth3']=sfpwsmooth3

sfradonoper = rsf.doc.rsfprog('sfradonoper','user/yliu/Mradonoper.c','''Linear Radon operator. ''')
sfradonoper.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sfradonoper.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfradonoper.par('np',rsf.doc.rsfpar('int','','','''number of p values (if adj=y) '''))
sfradonoper.par('dp',rsf.doc.rsfpar('float','','','''p sampling (if adj=y) '''))
sfradonoper.par('p0',rsf.doc.rsfpar('float','','','''p origin (if adj=y) '''))
sfradonoper.par('nx',rsf.doc.rsfpar('int','','','''number of offsets (if adj=n) '''))
sfradonoper.par('ox',rsf.doc.rsfpar('float','','',''''''))
sfradonoper.par('dx',rsf.doc.rsfpar('float','','',''''''))
sfradonoper.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform '''))
sfradonoper.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfradonoper.version('2.1-git')
sfradonoper.synopsis('''sfradonoper < in.rsf > out.rsf adj=y verb=n np= dp= p0= nx= ox= dx= parab=n x0=1.''','''''')
rsf.doc.progs['sfradonoper']=sfradonoper

sfreversval = rsf.doc.rsfprog('sfreversval','user/yliu/Mreversval.c','''Reverse data value ''')
sfreversval.version('2.1-git')
sfreversval.synopsis('''sfreversval < in.rsf > out.rsf''','''Data' = Max(Data) - Data
''')
rsf.doc.progs['sfreversval']=sfreversval

sfrtft = rsf.doc.rsfprog('sfrtft','user/yliu/Mrtft.c','''Ricker time-frequency transform. ''')
sfrtft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtft.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfrtft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfrtft.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sfrtft.par('dw',rsf.doc.rsfpar('float','','','''frequency step '''))
sfrtft.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sfrtft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius '''))
sfrtft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfrtft.par('alpha',rsf.doc.rsfpar('float','0.','','''frequency adaptivity '''))
sfrtft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfrtft.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfrtft.version('2.1-git')
sfrtft.synopsis('''sfrtft < in.rsf > out.rsf basis=basis.rsf mask=mask.rsf inv=n verb=n nw= dw= w0=0. rect=10 niter=100 alpha=0.''','''''')
rsf.doc.progs['sfrtft']=sfrtft

sfsaltpepper = rsf.doc.rsfprog('sfsaltpepper','user/yliu/Msaltpepper.c','''Add salt and pepper noise to the data.''')
sfsaltpepper.par('den',rsf.doc.rsfpar('float','10.','','''noise density (percent, default=10, Min=0, Max=100) '''))
sfsaltpepper.par('inten',rsf.doc.rsfpar('float','0.1','','''noise intensity (multiple peak value of data, default=0.1) '''))
sfsaltpepper.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfsaltpepper.par('allpos',rsf.doc.rsfpar('bool','n','','''if y, assume positive noise '''))
sfsaltpepper.par('noise',rsf.doc.rsfpar('bool','n','','''if y, output noise only '''))
sfsaltpepper.par('seed',rsf.doc.rsfpar('int','time(NULL)','','''random seed '''))
sfsaltpepper.version('2.1-git')
sfsaltpepper.synopsis('''sfsaltpepper < in.rsf > out.rsf den=10. inten=0.1 rep=n allpos=n noise=n seed=time(NULL)''','''''')
rsf.doc.progs['sfsaltpepper']=sfsaltpepper

sfsclet = rsf.doc.rsfprog('sfsclet','user/yliu/Msclet.c','''2-D SC-seislet: Seislet transform with differential shot continuation''')
sfsclet.par('inv',rsf.doc.rsfpar('bool','y','','''if y, do inverse transform '''))
sfsclet.par('adj',rsf.doc.rsfpar('bool','y','','''if y, do adjoint transform '''))
sfsclet.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfsclet.par('eps',rsf.doc.rsfpar('float','0.1','','''regularization parameter '''))
sfsclet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfsclet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfsclet.version('2.1-git')
sfsclet.synopsis('''sfsclet < in.rsf > out.rsf inv=y adj=y unit=n eps=0.1 verb=n type=''','''Forward transform (adj=y inv=y)   m=T[d]
Adjoint transform (adj=y inv=n)   m=T^(-1)'[d]
Inverse transform (adj=n inv=y/n) d=T^(-1)[m]
''')
rsf.doc.progs['sfsclet']=sfsclet

sfseisavf = rsf.doc.rsfprog('sfseisavf','user/yliu/Mseisavf.c','''1-D amplitude versus frequency (AVF) analysis with 1-D seislet frames ''')
sfseisavf.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisavf.par('thr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisavf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfseisavf.par('ncycle',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfseisavf.par('niter',rsf.doc.rsfpar('int','1','','''number of Bregman iterations '''))
sfseisavf.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseisavf.version('2.1-git')
sfseisavf.synopsis('''sfseisavf < in.rsf > out.rsf freq=w.rsf thr=t.rsf verb=y ncycle=0 niter=1 type=''','''''')
rsf.doc.progs['sfseisavf']=sfseisavf

sfseisbreg2 = rsf.doc.rsfprog('sfseisbreg2','user/yliu/Mseisbreg2.c','''Missing data interpolation in 2D using seislet and Bregman shaping iteration. ''')
sfseisbreg2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisbreg2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisbreg2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfseisbreg2.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfseisbreg2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseisbreg2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfseisbreg2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft thresholding '''))
sfseisbreg2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseisbreg2.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sfseisbreg2.par('oper',rsf.doc.rsfpar('string ',desc='''[bregman,thresholding] method, the default is bregman  '''))
sfseisbreg2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfseisbreg2.version('2.1-git')
sfseisbreg2.synopsis('''sfseisbreg2 < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf niter=20 order=1 verb=n eps=0.01 perc=99. order=1 type= oper=''','''''')
rsf.doc.progs['sfseisbreg2']=sfseisbreg2

sfseishrink = rsf.doc.rsfprog('sfseishrink','user/yliu/Mseishrink.c','''2-D Seislet shrinkage denoising. ''')
sfseishrink.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseishrink.par('lcurve',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseishrink.par('hcurve',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseishrink.par('norm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseishrink.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfseishrink.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseishrink.par('dwt',rsf.doc.rsfpar('bool','n','','''if y, dwt in vertical axis '''))
sfseishrink.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfseishrink.par('perc',rsf.doc.rsfpar('float','90.','','''percentage for shrinkage '''))
sfseishrink.par('nperc',rsf.doc.rsfpar('int','1','','''number of percentage dimension '''))
sfseishrink.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sfseishrink.par('lcurve',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.par('hcurve',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.par('norm',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.par('norm',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.par('lcurve',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.par('hcurve',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseishrink.version('2.1-git')
sfseishrink.synopsis('''sfseishrink < in.rsf > out.rsf dip=dip.rsf lcurve=lcurve.rsf hcurve=hcurve.rsf norm=norm.rsf order=1 verb=n dwt=n eps=0.01 perc=90. nperc=1 type=''','''''')
rsf.doc.progs['sfseishrink']=sfseishrink

sfseismis2 = rsf.doc.rsfprog('sfseismis2','user/yliu/Mseismis2.c','''Missing data interpolation in 2-D using seislet transform. ''')
sfseismis2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseismis2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseismis2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfseismis2.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfseismis2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseismis2.par('cut',rsf.doc.rsfpar('bool','n','','''cutting flag, the default is shaping '''))
sfseismis2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfseismis2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseismis2.par('cnum',rsf.doc.rsfpar('int','n2','','''Max cutting in cutting operator, default is n2 '''))
sfseismis2.par('orderc',rsf.doc.rsfpar('float','1.','','''Curve order for cutting operator, default is linear '''))
sfseismis2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft-thresholding '''))
sfseismis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding operator, default is linear '''))
sfseismis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding operator, default is linear '''))
sfseismis2.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sfseismis2.par('oper',rsf.doc.rsfpar('string ',desc='''[destruction,construction,shaping,pocs,bregman] method, the default is shaping  '''))
sfseismis2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfseismis2.version('2.1-git')
sfseismis2.synopsis('''sfseismis2 < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf niter=20 order=1 verb=n cut=n eps=0.01 order=1 cnum=n2 orderc=1. perc=99. ordert=1. ordert=1. type= oper=''','''''')
rsf.doc.progs['sfseismis2']=sfseismis2

sfseispocs = rsf.doc.rsfprog('sfseispocs','user/yliu/Mseispocs.c','''Missing data interpolation using POCS added 2-D seislet transform. ''')
sfseispocs.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseispocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseispocs.par('convex',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseispocs.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfseispocs.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfseispocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseispocs.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfseispocs.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseispocs.par('perc',rsf.doc.rsfpar('float','90.','','''percentage for smooth '''))
sfseispocs.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sfseispocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfseispocs.par('convex',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfseispocs.version('2.1-git')
sfseispocs.synopsis('''sfseispocs < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf convex=convex.rsf niter=20 order=1 verb=n eps=0.01 order=1 perc=90. type=''','''''')
rsf.doc.progs['sfseispocs']=sfseispocs

sfseisreg2 = rsf.doc.rsfprog('sfseisreg2','user/yliu/Mseisreg2.c','''Data regularization in 2-D using seislet transform. ''')
sfseisreg2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisreg2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfseisreg2.par('interp',rsf.doc.rsfpar('int','2','','''interpolation length '''))
sfseisreg2.par('niter',rsf.doc.rsfpar('int','50','','''number of iterations '''))
sfseisreg2.par('order',rsf.doc.rsfpar('int','1','[1,2,3]','''accuracy order '''))
sfseisreg2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseisreg2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseisreg2.par('head',rsf.doc.rsfpar('string ',desc=''''''))
sfseisreg2.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseisreg2.version('2.1-git')
sfseisreg2.synopsis('''sfseisreg2 < in.rsf > out.rsf dip=dip.rsf eps=0.01 interp=2 niter=50 order=1 order=1 verb=n head= type=''','''''')
rsf.doc.progs['sfseisreg2']=sfseisreg2

sfseisxwell = rsf.doc.rsfprog('sfseisxwell','user/yliu/Mseisxwell.c','''Select seismic data cross well position. ''')
sfseisxwell.par('path',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfseisxwell.par('well',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisxwell.par('wx',rsf.doc.rsfpar('floats','','','''well x coordinates  [nw]'''))
sfseisxwell.par('wy',rsf.doc.rsfpar('floats','','','''well y coordinates  [nw]'''))
sfseisxwell.par('nw',rsf.doc.rsfpar('int','0','','''number of well points '''))
sfseisxwell.par('path',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfseisxwell.par('well',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfseisxwell.version('2.1-git')
sfseisxwell.synopsis('''sfseisxwell < in.rsf > out.rsf path=spath.rsf well=well.rsf wx= wy= nw=0''','''''')
rsf.doc.progs['sfseisxwell']=sfseisxwell

sfsharpsimi = rsf.doc.rsfprog('sfsharpsimi','user/yliu/Msharpsimi.c','''Sharpen similarity measure between two datasets. ''')
sfsharpsimi.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsharpsimi.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfsharpsimi.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfsharpsimi.par('perc',rsf.doc.rsfpar('float','98.','','''percentage for sharpen, default is 98'''))
sfsharpsimi.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfsharpsimi.version('2.1-git')
sfsharpsimi.synopsis('''sfsharpsimi < in.rsf > out.rsf other=other.rsf eps=0.01 niter=20 perc=98. verb=n''','''''')
rsf.doc.progs['sfsharpsimi']=sfsharpsimi

sfsnr = rsf.doc.rsfprog('sfsnr','user/yliu/Msnr.c','''Display dataset signal-noise-ratio.''')
sfsnr.par('ntw1',rsf.doc.rsfpar('int','1','','''trace-window beginning position (default=1)'''))
sfsnr.par('ntw2',rsf.doc.rsfpar('int','n2','','''trace-window end position (default=n2)'''))
sfsnr.par('nsw1',rsf.doc.rsfpar('int','1','','''sample-window beginning position (default=1)'''))
sfsnr.par('nsw2',rsf.doc.rsfpar('int','n1','','''sample-window end position (default=n1)'''))
sfsnr.par('type',rsf.doc.rsfpar('string ',desc='''[stack] method type, the default is stack '''))
sfsnr.version('2.1-git')
sfsnr.synopsis('''sfsnr < in.rsf ntw1=1 ntw2=n2 nsw1=1 nsw2=n1 type=''','''''')
rsf.doc.progs['sfsnr']=sfsnr

sfsphase = rsf.doc.rsfprog('sfsphase','user/yliu/Msphase.c','''Smooth estimate of instantaneous phase. ''')
sfsphase.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfsphase.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfsphase.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfsphase.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsphase.version('2.1-git')
sfsphase.synopsis('''sfsphase < in.rsf > out.rsf niter=100 order=10 ref=1. rect#=(1,1,...)''','''''')
rsf.doc.progs['sfsphase']=sfsphase

sfst = rsf.doc.rsfprog('sfst','user/yliu/Mst.c','''S transform ''')
sfst.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfst.par('flo',rsf.doc.rsfpar('float','','','''Low frequency in band, default is 0 '''))
sfst.par('fhi',rsf.doc.rsfpar('float','','','''High frequency in band, default is Nyquist '''))
sfst.version('2.1-git')
sfst.synopsis('''sfst < in.rsf > out.rsf inv=n flo= fhi=''','''''')
rsf.doc.progs['sfst']=sfst

sfstft = rsf.doc.rsfprog('sfstft','user/yliu/Mstft.c','''Short-time Fourier transform (STFT). ''')
sfstft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sfstft.par('sym',rsf.doc.rsfpar('bool','n','','''if y, apply symmetric scaling to make the FFT operator Hermitian '''))
sfstft.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfstft.par('ntw',rsf.doc.rsfpar('int','7','','''time-window length '''))
sfstft.version('2.1-git')
sfstft.synopsis('''sfstft < in.rsf > out.rsf inv=n sym=n opt=y ntw=7''','''''')
rsf.doc.progs['sfstft']=sfstft

sfsv2d = rsf.doc.rsfprog('sfsv2d','user/yliu/Msv2d.c','''Velocity and heterogeneity parameter convert to dip. ''')
sfsv2d.par('anisotropy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsv2d.par('n',rsf.doc.rsfpar('int','32','','''offset number '''))
sfsv2d.par('d',rsf.doc.rsfpar('float','12.5','','''offset interval '''))
sfsv2d.par('o',rsf.doc.rsfpar('float','0.','','''offset origin '''))
sfsv2d.par('mute',rsf.doc.rsfpar('bool','n','','''if y, use mutter '''))
sfsv2d.par('half',rsf.doc.rsfpar('bool','n','','''if y, half-offset instead of full offset '''))
sfsv2d.par('tp',rsf.doc.rsfpar('float','0.150','','''end time (available when mute=y) '''))
sfsv2d.par('t0',rsf.doc.rsfpar('float','0.','','''starting time (available when mute=y) '''))
sfsv2d.par('v0',rsf.doc.rsfpar('float','10000','','''velocity (available when mute=y) '''))
sfsv2d.par('x0',rsf.doc.rsfpar('float','0.','','''starting space (available when mute=y) '''))
sfsv2d.par('abs',rsf.doc.rsfpar('bool','y','','''if y, use absolute value |x-x0| (available when mute=y) '''))
sfsv2d.par('inner',rsf.doc.rsfpar('bool','n','','''if y, do inner muter (available when mute=y) '''))
sfsv2d.par('hyper',rsf.doc.rsfpar('bool','n','','''if y, do hyperbolic mute (available when mute=y) '''))
sfsv2d.version('2.1-git')
sfsv2d.synopsis('''sfsv2d < in.rsf > out.rsf anisotropy=anisotropy.rsf n=32 d=12.5 o=0. mute=n half=n tp=0.150 t0=0. v0=10000 x0=0. abs=y inner=n hyper=n''','''''')
rsf.doc.progs['sfsv2d']=sfsv2d

sfsvd = rsf.doc.rsfprog('sfsvd','user/yliu/Msvd.c','''Singular value decomposition (SVD)''')
sfsvd.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsvd.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsvd.par('left',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfsvd.par('right',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfsvd.version('2.1-git')
sfsvd.synopsis('''sfsvd < in.rsf > out.rsf left=outu.rsf right=outv.rsf''','''Compute [U,O,V]=SVD(A), A=UOV, a little bit different from A=UoV' ''')
rsf.doc.progs['sfsvd']=sfsvd

sfsvddenoise = rsf.doc.rsfprog('sfsvddenoise','user/yliu/Msvddenoise.c','''SVD denoising ''')
sfsvddenoise.par('pclip',rsf.doc.rsfpar('float','99.','','''data clip percentile (default is 99)'''))
sfsvddenoise.version('2.1-git')
sfsvddenoise.synopsis('''sfsvddenoise < in.rsf > out.rsf pclip=99.''','''''')
rsf.doc.progs['sfsvddenoise']=sfsvddenoise

sfswell = rsf.doc.rsfprog('sfswell','user/yliu/Mswell.c','''Add swell noise to the data.''')
sfswell.par('den',rsf.doc.rsfpar('float','10.','','''noise density (percent, default=10, Min=0, Max=100) '''))
sfswell.par('inten',rsf.doc.rsfpar('float','0.1','','''noise intensity (multiple peak value of data, default=0.1) '''))
sfswell.par('slope',rsf.doc.rsfpar('float','0.1','','''noise slope (default=0.1) '''))
sfswell.par('width',rsf.doc.rsfpar('int','4','','''max noise width (default=4) '''))
sfswell.par('length',rsf.doc.rsfpar('int','30','','''max noise length (default=30) '''))
sfswell.par('num',rsf.doc.rsfpar('int','5','','''noise number (default=5) '''))
sfswell.par('rep',rsf.doc.rsfpar('bool','n','','''if y, replace data with noise '''))
sfswell.par('noise',rsf.doc.rsfpar('bool','n','','''if y, output noise only '''))
sfswell.version('2.1-git')
sfswell.synopsis('''sfswell < in.rsf > out.rsf den=10. inten=0.1 slope=0.1 width=4 length=30 num=5 rep=n noise=n''','''''')
rsf.doc.progs['sfswell']=sfswell

sftestapef = rsf.doc.rsfprog('sftestapef','user/yliu/Mtestapef.c','''Test linear adaptive PEF operator. ''')
sftestapef.par('sfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftestapef.par('nfilt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftestapef.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sftestapef.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftestapef.par('sign',rsf.doc.rsfpar('bool','y','','''if y, test signal PEF; otherwise, test noise PEF '''))
sftestapef.version('2.1-git')
sftestapef.synopsis('''sftestapef < in.rsf > out.rsf sfilt=sfilt.rsf nfilt=nfilt.rsf adj=y verb=n sign=y''','''''')
rsf.doc.progs['sftestapef']=sftestapef

sftestcasoper = rsf.doc.rsfprog('sftestcasoper','user/yliu/Mtestcasoper.c','''Test linear cascading matching-Radon operator. ''')
sftestcasoper.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftestcasoper.par('adj',rsf.doc.rsfpar('bool','n','','''if y, perform adjoint operation '''))
sftestcasoper.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse operation '''))
sftestcasoper.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftestcasoper.par('np',rsf.doc.rsfpar('int','','','''number of p values '''))
sftestcasoper.par('dp',rsf.doc.rsfpar('float','','','''p sampling '''))
sftestcasoper.par('p0',rsf.doc.rsfpar('float','','','''p origin '''))
sftestcasoper.par('niter',rsf.doc.rsfpar('int','100','',''''''))
sftestcasoper.par('freq',rsf.doc.rsfpar('bool','y','','''if y, parabolic Radon transform '''))
sftestcasoper.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform, only when freq=y '''))
sftestcasoper.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sftestcasoper.par('rho',rsf.doc.rsfpar('bool','y','','''rho filtering, only when freq=n '''))
sftestcasoper.par('anti',rsf.doc.rsfpar('float','1.','','''antialiasing, only when freq=n '''))
sftestcasoper.par('p1',rsf.doc.rsfpar('float','0.','','''reference slope, only when freq=n '''))
sftestcasoper.version('2.1-git Mtestcasoper.c 5959 2010-05-14 04:11:09Z yang_liu')
sftestcasoper.synopsis('''sftestcasoper < in.rsf > out.rsf filt=fil.rsf adj=n inv=n verb=n np= dp= p0= niter=100 freq=y parab=n x0=1. rho=y anti=1. p1=0.''','''''')
rsf.doc.progs['sftestcasoper']=sftestcasoper

sftestmatch = rsf.doc.rsfprog('sftestmatch','user/yliu/Mtestmatch.c','''Test linear matching operator. ''')
sftestmatch.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftestmatch.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sftestmatch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftestmatch.version('2.1-git')
sftestmatch.synopsis('''sftestmatch < in.rsf > out.rsf filt=fil.rsf adj=y verb=n''','''''')
rsf.doc.progs['sftestmatch']=sftestmatch

sfthreshold2 = rsf.doc.rsfprog('sfthreshold2','user/yliu/Mthreshold2.c','''2-D Soft thresholding. ''')
sfthreshold2.par('thr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthreshold2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfthreshold2.par('pclip',rsf.doc.rsfpar('float','99.','',''''''))
sfthreshold2.par('thr',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfthreshold2.version('2.1-git')
sfthreshold2.synopsis('''sfthreshold2 < in.rsf > out.rsf thr=thr.rsf verb=n pclip=99.''','''''')
rsf.doc.progs['sfthreshold2']=sfthreshold2

sfthreshold3 = rsf.doc.rsfprog('sfthreshold3','user/yliu/Mthreshold3.c','''Automatic soft or hard thresholding. ''')
sfthreshold3.par('type',rsf.doc.rsfpar('string ',desc='''[soft,hard] thresholding type, the default is soft  '''))
sfthreshold3.par('dist',rsf.doc.rsfpar('string ',desc='''[gaussian,rayleigh] distribution type, the default is gaussian '''))
sfthreshold3.version('2.1-git')
sfthreshold3.synopsis('''sfthreshold3 < in.rsf > out.rsf type= dist=''','''''')
rsf.doc.progs['sfthreshold3']=sfthreshold3

sftslread = rsf.doc.rsfprog('sftslread','user/yliu/Mtslread.c','''Convert a TSL (MT, V5-2000 of Phoenix Geophysics) dataset to RSF. ''')
sftslread.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftslread.par('format',rsf.doc.rsfpar('bool','n','','''data format: [false] (TSL,TSH: 16) or [true] (TSn: 32) '''))
sftslread.par('data',rsf.doc.rsfpar('string ',desc='''input data '''))
sftslread.par('tfile',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftslread.version('2.1-git')
sftslread.synopsis('''sftslread > out.rsf tfile=tfile.rsf format=n data=''','''''')
rsf.doc.progs['sftslread']=sftslread

sftvmf = rsf.doc.rsfprog('sftvmf','user/yliu/Mtvmf.c','''1D Time-varying median filtering. ''')
sftvmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sftvmf.par('nfw',rsf.doc.rsfpar('int','','','''reference filter-window length (>delta, positive and odd integer)'''))
sftvmf.par('alpha',rsf.doc.rsfpar('int','2','','''time-varying window parameter "alpha" (default=2)'''))
sftvmf.par('beta',rsf.doc.rsfpar('int','0','','''time-varying window parameter "beta" (default=0)'''))
sftvmf.par('gamma',rsf.doc.rsfpar('int','2','','''time-varying window parameter "gamma" (default=2)'''))
sftvmf.par('delta',rsf.doc.rsfpar('int','4','','''time-varying window parameter "delta" (default=4)'''))
sftvmf.version('2.1-git')
sftvmf.synopsis('''sftvmf < in.rsf > out.rsf boundary=n nfw= alpha=2 beta=0 gamma=2 delta=4''','''''')
rsf.doc.progs['sftvmf']=sftvmf

sftxrna = rsf.doc.rsfprog('sftxrna','user/yliu/Mtxrna.c','''Causal t-x or t-x-y nonstationary regularized autoregression. ''')
sftxrna.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftxrna.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sftxrna.version('2.1-git')
sftxrna.synopsis('''sftxrna < mat.rsf > flt.rsf pred=pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna']=sftxrna

sftxrna2 = rsf.doc.rsfprog('sftxrna2','user/yliu/Mtxrna2.c','''2D space-noncausal t-x nonstationary regularized autoregression. ''')
sftxrna2.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna2.version('2.1-git')
sftxrna2.synopsis('''sftxrna2 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna2']=sftxrna2

sftxrna3 = rsf.doc.rsfprog('sftxrna3','user/yliu/Mtxrna3.c','''3D space-noncausal t-x-y nonstationary regularized autoregression. ''')
sftxrna3.par('a',rsf.doc.rsfpar('ints','','',''' [mdim]'''))
sftxrna3.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sftxrna3.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftxrna3.version('2.1-git')
sftxrna3.synopsis('''sftxrna3 < mat.rsf > pre.rsf a= niter=20 verb=n''','''''')
rsf.doc.progs['sftxrna3']=sftxrna3

sftxspf = rsf.doc.rsfprog('sftxspf','user/yliu/Mtxspf.c','''Streaming prediction filter in t-x domain. ''')
sftxspf.par('a',rsf.doc.rsfpar('ints','','','''Get filter size from input, a0 is 2M+1, a1 is N in equation 3  [dim]'''))
sftxspf.par('lambda1',rsf.doc.rsfpar('float','','','''Regularization in t direction, lambda_t in equations 1 and 5 '''))
sftxspf.par('lambda2',rsf.doc.rsfpar('float','','','''Regularization in x direction, lambda_x in equations 1 and 5 '''))
sftxspf.version('2.1-git')
sftxspf.synopsis('''sftxspf < in.rsf > out.rsf a= lambda1= lambda2=''','''''')
rsf.doc.progs['sftxspf']=sftxspf

sftxsorth = rsf.doc.rsfprog('sftxsorth','user/yliu/Mtxsorth.c','''Streaming orthogonalize signal and noise in t-x domain. ''')
sftxsorth.par('noise',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftxsorth.par('sig2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftxsorth.par('gamma1',rsf.doc.rsfpar('float','','','''Regularization in t direction, gamma_t in equations 18 and 20 '''))
sftxsorth.par('gamma2',rsf.doc.rsfpar('float','','','''Regularization in x direction, gamma_x in equations 18 and 20 '''))
sftxsorth.version('2.1-git')
sftxsorth.synopsis('''sftxsorth < in.rsf noise=noise.rsf > fnoi2.rsf sig2=fsig2.rsf gamma1= gamma2=''','''''')
rsf.doc.progs['sftxsorth']=sftxsorth

sfv2d = rsf.doc.rsfprog('sfv2d','user/yliu/Mv2d.c','''Velocity convert to dip. ''')
sfv2d.par('n',rsf.doc.rsfpar('int','32','','''offset number '''))
sfv2d.par('d',rsf.doc.rsfpar('float','12.5','','''offset interval '''))
sfv2d.par('o',rsf.doc.rsfpar('float','0.','','''offset origin '''))
sfv2d.par('mute',rsf.doc.rsfpar('bool','n','','''if y, use mutter '''))
sfv2d.par('half',rsf.doc.rsfpar('bool','n','','''if y, half-offset instead of full offset '''))
sfv2d.par('tp',rsf.doc.rsfpar('float','0.150','','''end time (available when mute=y) '''))
sfv2d.par('t0',rsf.doc.rsfpar('float','0.','','''starting time (available when mute=y) '''))
sfv2d.par('v0',rsf.doc.rsfpar('float','10000','','''velocity (available when mute=y) '''))
sfv2d.par('x0',rsf.doc.rsfpar('float','0.','','''starting space (available when mute=y) '''))
sfv2d.par('abs',rsf.doc.rsfpar('bool','y','','''if y, use absolute value |x-x0| (available when mute=y) '''))
sfv2d.par('inner',rsf.doc.rsfpar('bool','n','','''if y, do inner muter (available when mute=y) '''))
sfv2d.par('hyper',rsf.doc.rsfpar('bool','n','','''if y, do hyperbolic mute (available when mute=y) '''))
sfv2d.version('2.1-git')
sfv2d.synopsis('''sfv2d < in.rsf > out.rsf n=32 d=12.5 o=0. mute=n half=n tp=0.150 t0=0. v0=10000 x0=0. abs=y inner=n hyper=n''','''''')
rsf.doc.progs['sfv2d']=sfv2d

sfvariogram = rsf.doc.rsfprog('sfvariogram','user/yliu/Mvariogram.c','''Compute a variogram of data values. ''')
sfvariogram.par('dh',rsf.doc.rsfpar('int','1','','''interval (number) of variogram lag '''))
sfvariogram.par('oh',rsf.doc.rsfpar('int','0','','''origin (number) of variogram lag '''))
sfvariogram.par('nh',rsf.doc.rsfpar('int','n1/dh-oh','','''number of variogram lag '''))
sfvariogram.par('semi',rsf.doc.rsfpar('bool','y','','''if y, output semivariogram '''))
sfvariogram.version('2.1-git')
sfvariogram.synopsis('''sfvariogram < in.rsf > out.rsf dh=1 oh=0 nh=n1/dh-oh semi=y''','''''')
rsf.doc.progs['sfvariogram']=sfvariogram

sfvariogram2 = rsf.doc.rsfprog('sfvariogram2','user/yliu/Mvariogram2.c','''Compute a horizontal variogram of data slice. ''')
sfvariogram2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfvariogram2.par('dh1',rsf.doc.rsfpar('int','1','','''interval (jump) of variogram lag in first axis '''))
sfvariogram2.par('nh1',rsf.doc.rsfpar('int','n1/dh1','','''number of variogram lag in first axis '''))
sfvariogram2.par('dh2',rsf.doc.rsfpar('int','1','','''interval (jump) of variogram lag in second axis '''))
sfvariogram2.par('nh2',rsf.doc.rsfpar('int','n2/dh2','','''number of variogram lag in second axis '''))
sfvariogram2.par('semi',rsf.doc.rsfpar('bool','y','','''if y, output semivariogram '''))
sfvariogram2.version('2.1-git')
sfvariogram2.synopsis('''sfvariogram2 < in.rsf > out.rsf verb=n dh1=1 nh1=n1/dh1 dh2=1 nh2=n2/dh2 semi=y''','''''')
rsf.doc.progs['sfvariogram2']=sfvariogram2

sfvconvert = rsf.doc.rsfprog('sfvconvert','user/yliu/Mvconvert.c','''2-D velocity mapping from manual picking to rsf RMS format. ''')
sfvconvert.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvconvert.par('shift',rsf.doc.rsfpar('int','0','','''Lateral shift '''))
sfvconvert.par('pattern',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvconvert.version('2.1-git')
sfvconvert.synopsis('''sfvconvert < in.rsf > out.rsf pattern=pattern.rsf shift=0''','''Covert from
--------------------------------------
Time_i(ms) RMS_i(m/s) Lateral_j(trace)
...        ...        ...
-1         0          Lateral_j
...        ...        ...
--------------------------------------
to
regular RSF_RMS velocity grid

Specify either n1= o1= d1= n2= o2= d2= or pattern=
''')
rsf.doc.progs['sfvconvert']=sfvconvert

sfvirtualdata = rsf.doc.rsfprog('sfvirtualdata','user/yliu/Mvirtualdata.c','''Construction of virtual seismic data. ''')
sfvirtualdata.par('dif',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvirtualdata.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfvirtualdata.par('stack',rsf.doc.rsfpar('bool','n','','''stack flag, if y, no common multiple gather '''))
sfvirtualdata.par('both',rsf.doc.rsfpar('bool','n','','''receiver flag, if y, receiver with both sides '''))
sfvirtualdata.par('jumpo',rsf.doc.rsfpar('int','1','','''jump in offset dimension, only for stack=n '''))
sfvirtualdata.par('jumps',rsf.doc.rsfpar('int','1','','''jump in shot dimension, only for stack=n  '''))
sfvirtualdata.par('dif',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfvirtualdata.version('2.1-git')
sfvirtualdata.synopsis('''sfvirtualdata < in.rsf > out.rsf dif=dif.rsf verb=n stack=n both=n jumpo=1 jumps=1''','''''')
rsf.doc.progs['sfvirtualdata']=sfvirtualdata

sfwavemis2 = rsf.doc.rsfprog('sfwavemis2','user/yliu/Mwavemis2.c','''Missing data interpolation in 2-D using wavelet transform and compressive sensing. ''')
sfwavemis2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwavemis2.par('niter',rsf.doc.rsfpar('int','20','','''number of iterations '''))
sfwavemis2.par('perc',rsf.doc.rsfpar('float','99.','','''percentage for soft-thresholding '''))
sfwavemis2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwavemis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sfwavemis2.par('ordert',rsf.doc.rsfpar('float','1.','','''Curve order for thresholding parameter, default is linear '''))
sfwavemis2.par('nbreg',rsf.doc.rsfpar('int','1','','''number of iterations for Bregman iteration '''))
sfwavemis2.par('oper',rsf.doc.rsfpar('string ',desc='''[shaping,pocs,bregman] method, the default is shaping  '''))
sfwavemis2.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfwavemis2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfwavemis2.version('2.1-git')
sfwavemis2.synopsis('''sfwavemis2 < in.rsf > out.rsf mask=mask.rsf niter=20 perc=99. verb=n ordert=1. ordert=1. nbreg=1 oper= type=''','''''')
rsf.doc.progs['sfwavemis2']=sfwavemis2

sfwinscan = rsf.doc.rsfprog('sfwinscan','user/yliu/Mwinscan.c','''Picking scanned data window trace by trace with fixed t0''')
sfwinscan.par('winsz',rsf.doc.rsfpar('int','200','','''for each trace,the width of window. unit:sample point '''))
sfwinscan.par('v0',rsf.doc.rsfpar('float','1000','','''init Vel for velocity scan '''))
sfwinscan.par('deltav',rsf.doc.rsfpar('float','20','','''step lenth for velocity scan '''))
sfwinscan.par('t0',rsf.doc.rsfpar('float','0.5','','''t0 fixed '''))
sfwinscan.par('n',rsf.doc.rsfpar('int','100','','''numbers of velscan'''))
sfwinscan.version('2.1-git')
sfwinscan.synopsis('''sfwinscan < cmp.rsf > outf.rsf winsz=200 v0=1000 deltav=20 t0=0.5 n=100''','''''')
rsf.doc.progs['sfwinscan']=sfwinscan

sfwmf = rsf.doc.rsfprog('sfwmf','user/yliu/Mwmf.c','''1D weighted median filtering. ''')
sfwmf.par('weights',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwmf.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwmf.par('nfw',rsf.doc.rsfpar('int','','','''filter-window length (positive and odd integer)'''))
sfwmf.par('boundary',rsf.doc.rsfpar('bool','n','','''if y, boundary is data, whereas zero'''))
sfwmf.par('weights',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfwmf.version('2.1-git')
sfwmf.synopsis('''sfwmf < in.rsf > out.rsf weights=weights.rsf verb=n nfw= boundary=n''','''''')
rsf.doc.progs['sfwmf']=sfwmf

sfzcwt = rsf.doc.rsfprog('sfzcwt','user/yliu/Mzcwt.c','''Improve signal resolution using zero-crossing of wavelet transform. ''')
sfzcwt.par('maxscale',rsf.doc.rsfpar('int','5','','''The maximum decomposition scale (default=5)'''))
sfzcwt.par('outscale',rsf.doc.rsfpar('int','1','','''The output scale (default=1)'''))
sfzcwt.version('2.1-git')
sfzcwt.synopsis('''sfzcwt < in.rsf > out.rsf maxscale=5 outscale=1''','''''')
rsf.doc.progs['sfzcwt']=sfzcwt

