import rsf.doc

sfabalance = rsf.doc.rsfprog('sfabalance','user/fomels/Mabalance.c','''Amplitude balancing. ''')
sfabalance.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfabalance.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfabalance.par('reverse',rsf.doc.rsfpar('bool','y','','''reverse weight '''))
sfabalance.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfabalance.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfabalance.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfabalance.par('weight',rsf.doc.rsfpar('string ',desc='''optional weight output (auxiliary output file name)'''))
sfabalance.version('2.1-git')
sfabalance.synopsis('''sfabalance < in.rsf other=ref.rsf > out.rsf weight=weight.rsf reverse=y niter=100 order=100 ref=1.''','''''')
rsf.doc.progs['sfabalance']=sfabalance

sfanalytical = rsf.doc.rsfprog('sfanalytical','user/fomels/Manalytical.c','''First-arrival traveltime table using analytical traveltimes ''')
sfanalytical.par('vel',rsf.doc.rsfpar('bool','y','','''y, input is velocity; n, slowness '''))
sfanalytical.par('order',rsf.doc.rsfpar('int','3','','''interpolation accuracy for velocity '''))
sfanalytical.par('yshot',rsf.doc.rsfpar('float','x0 + 0.5*(nx-1)*dx','',''''''))
sfanalytical.par('zshot',rsf.doc.rsfpar('float','z0','','''read velocity or slowness '''))
sfanalytical.version('2.1-git')
sfanalytical.synopsis('''sfanalytical < in.rsf > out.rsf vel=y order=3 yshot=x0 + 0.5*(nx-1)*dx zshot=z0''','''''')
rsf.doc.progs['sfanalytical']=sfanalytical

sfangle = rsf.doc.rsfprog('sfangle','user/fomels/Mangle.c','''Illustration of angle gathers.''')
sfangle.par('nw',rsf.doc.rsfpar('int','513','',''''''))
sfangle.par('nm',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('nh',rsf.doc.rsfpar('int','257','',''''''))
sfangle.par('dw',rsf.doc.rsfpar('float','1./(2*(nw-1)*0.004)','',''''''))
sfangle.par('dm',rsf.doc.rsfpar('float','1./(2*(nm-1)*0.01)','',''''''))
sfangle.par('dh',rsf.doc.rsfpar('float','1./(2*(nh-1)*0.01)','',''''''))
sfangle.par('w0',rsf.doc.rsfpar('float','dw','',''''''))
sfangle.par('vel',rsf.doc.rsfpar('float','2.','',''''''))
sfangle.version('2.1-git')
sfangle.synopsis('''sfangle > angle.rsf nw=513 nm=257 nh=257 dw=1./(2*(nw-1)*0.004) dm=1./(2*(nm-1)*0.01) dh=1./(2*(nh-1)*0.01) w0=dw vel=2.''','''''')
rsf.doc.progs['sfangle']=sfangle

sfangle2 = rsf.doc.rsfprog('sfangle2','user/fomels/Mangle2.c','''Another illustration of angle gathers.''')
sfangle2.par('nx',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('ny',rsf.doc.rsfpar('int','451','',''''''))
sfangle2.par('dx',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('dy',rsf.doc.rsfpar('float','0.1','',''''''))
sfangle2.par('zx',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.par('zy',rsf.doc.rsfpar('float','0.','',''''''))
sfangle2.version('2.1-git')
sfangle2.synopsis('''sfangle2 > angle.rsf nx=451 ny=451 dx=0.1 dy=0.1 zx=0. zy=0.''','''''')
rsf.doc.progs['sfangle2']=sfangle2

sfapprox = rsf.doc.rsfprog('sfapprox','user/fomels/Mapprox.c','''Illustrating non-hyperbolic approximations ''')
sfapprox.par('np',rsf.doc.rsfpar('int','300','',''''''))
sfapprox.par('nq',rsf.doc.rsfpar('int','300','',''''''))
sfapprox.par('dp',rsf.doc.rsfpar('float','1./(np-1)','',''''''))
sfapprox.par('dq',rsf.doc.rsfpar('float','4./(nq-1)','',''''''))
sfapprox.par('dist',rsf.doc.rsfpar('string ',desc='''distribution type '''))
sfapprox.par('appr',rsf.doc.rsfpar('string ',desc='''approximation type '''))
sfapprox.version('2.1-git')
sfapprox.synopsis('''sfapprox > out.rsf np=300 nq=300 dp=1./(np-1) dq=4./(nq-1) dist= appr=''','''''')
rsf.doc.progs['sfapprox']=sfapprox

sfarrival = rsf.doc.rsfprog('sfarrival','user/fomels/Marrival.c','''Multiple-arrival interpolation from down-marching. ''')
sfarrival.par('place',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfarrival.par('depth',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfarrival.par('sx',rsf.doc.rsfpar('float','0.','','''source x position '''))
sfarrival.par('nw',rsf.doc.rsfpar('int','3','','''interpolation accuracy '''))
sfarrival.par('depth',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfarrival.version('2.1-git')
sfarrival.synopsis('''sfarrival < in.rsf place=place.rsf > out.rsf depth=depth.rsf sx=0. nw=3''','''''')
rsf.doc.progs['sfarrival']=sfarrival

sfbdix = rsf.doc.rsfprog('sfbdix','user/fomels/Mbdix.c','''Convert RMS to interval velocity using LS and shaping regularization.''')
sfbdix.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbdix.par('block',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbdix.par('vrmsout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbdix.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfbdix.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfbdix.par('vrmsout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted vrms (auxiliary output file name)'''))
sfbdix.version('2.1-git Mdix.c 1131 2005-04-20 18:19:10Z fomels')
sfbdix.synopsis('''sfbdix < vrms.rsf > vint.rsf weight=weight.rsf block=block.rsf vrmsout=vout.rsf perc=50.0 niter=100 rect1= rect2= ...''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfbdix']=sfbdix

sfbil1 = rsf.doc.rsfprog('sfbil1','user/fomels/Mbil1.c','''Bi-variate L1 regression ''')
sfbil1.par('reg',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbil1.par('niter',rsf.doc.rsfpar('int','10','','''number of POCS iterations '''))
sfbil1.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening '''))
sfbil1.version('2.1-git')
sfbil1.synopsis('''sfbil1 < inp.rsf reg=reg.rsf > out.rsf niter=10 perc=90.0''','''''')
rsf.doc.progs['sfbil1']=sfbil1

sfbilat2 = rsf.doc.rsfprog('sfbilat2','user/fomels/Mbilat2.c','''2-D bilateral filtering ''')
sfbilat2.par('r1',rsf.doc.rsfpar('int','1','','''vertical smoothing radius '''))
sfbilat2.par('r2',rsf.doc.rsfpar('int','1','','''horizontal smoothing radius '''))
sfbilat2.par('a1',rsf.doc.rsfpar('float','0.0f','','''vertical attenuation factor '''))
sfbilat2.par('a2',rsf.doc.rsfpar('float','a1','','''horizontal attenuation factor '''))
sfbilat2.par('a3',rsf.doc.rsfpar('float','0.0f','','''data attenuation factor '''))
sfbilat2.par('repeat',rsf.doc.rsfpar('int','1','','''repeat the operation '''))
sfbilat2.version('2.1-git')
sfbilat2.synopsis('''sfbilat2 < inp.rsf > out.rsf r1=1 r2=1 a1=0.0f a2=a1 a3=0.0f repeat=1''','''''')
rsf.doc.progs['sfbilat2']=sfbilat2

sfblur = rsf.doc.rsfprog('sfblur','user/fomels/Mblur.c','''2-D blurring and deblurring ''')
sfblur.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfblur.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfblur.par('spk',rsf.doc.rsfpar('bool','y','','''spiky inversion '''))
sfblur.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfblur.par('eps',rsf.doc.rsfpar('float','1.','','''scaling '''))
sfblur.par('rect',rsf.doc.rsfpar('int','','','''blurring radius '''))
sfblur.par('rect2',rsf.doc.rsfpar('float','1.0','','''smoothing radius '''))
sfblur.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfblur.par('ncycle',rsf.doc.rsfpar('int','1','','''number of nonlinear cycles '''))
sfblur.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfblur.version('2.1-git')
sfblur.synopsis('''sfblur < in.rsf > out.rsf adj=n inv=n spk=y niter=100 eps=1. rect= rect2=1.0 repeat=1 ncycle=1 perc=50.0''','''''')
rsf.doc.progs['sfblur']=sfblur

sfboxcascade = rsf.doc.rsfprog('sfboxcascade','user/fomels/Mboxcascade.c','''Box filter cascade ''')
sfboxcascade.par('rect',rsf.doc.rsfpar('int','0','','''smoothing radius '''))
sfboxcascade.par('inter',rsf.doc.rsfpar('int','n','','''interrupt '''))
sfboxcascade.version('2.1-git')
sfboxcascade.synopsis('''sfboxcascade < inp.rsf > out.rsf rect=0 inter=n''','''''')
rsf.doc.progs['sfboxcascade']=sfboxcascade

sfcfftwave1 = rsf.doc.rsfprog('sfcfftwave1','user/fomels/Mcfftwave1.c','''1-D complex lowrank FFT wave extrapolation ''')
sfcfftwave1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcfftwave1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcfftwave1.par('prop',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcfftwave1.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfcfftwave1.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfcfftwave1.par('right',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfcfftwave1.version('2.1-git')
sfcfftwave1.synopsis('''sfcfftwave1 < inp.rsf > out.rsf left=left.rsf right=right.rsf prop=prop.rsf nt= dt=''','''''')
rsf.doc.progs['sfcfftwave1']=sfcfftwave1

sfcdivn = rsf.doc.rsfprog('sfcdivn','user/fomels/Mcdivn.c','''Smooth division for complex data. ''')
sfcdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfcdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfcdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfcdivn.version('2.1-git')
sfcdivn.synopsis('''sfcdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sfcdivn']=sfcdivn

sfcflow = rsf.doc.rsfprog('sfcflow','user/fomels/Mcflow.c','''Fast mean-curvature flow. ''')
sfcflow.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfcflow.par('order',rsf.doc.rsfpar('int','3','','''interpolation order '''))
sfcflow.par('tol',rsf.doc.rsfpar('float','0.1','','''error tolerance '''))
sfcflow.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfcflow.par('band',rsf.doc.rsfpar('float','1.','','''narrow band '''))
sfcflow.version('2.1-git')
sfcflow.synopsis('''sfcflow < in.rsf > out.rsf rect=3 order=3 tol=0.1 niter=100 band=1.''','''''')
rsf.doc.progs['sfcflow']=sfcflow

sfchebvc = rsf.doc.rsfprog('sfchebvc','user/fomels/Mchebvc.c','''Post-stack 2-D velocity continuation by Chebyshev-tau method. ''')
sfchebvc.par('nv',rsf.doc.rsfpar('int','','',''''''))
sfchebvc.par('vel',rsf.doc.rsfpar('float','','',''''''))
sfchebvc.version('2.1-git')
sfchebvc.synopsis('''sfchebvc < in.rsf > out.rsf nv= vel=''','''''')
rsf.doc.progs['sfchebvc']=sfchebvc

sfclpf = rsf.doc.rsfprog('sfclpf','user/fomels/Mclpf.c','''Local prediction filter for complex numbers (n-dimensional). ''')
sfclpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfclpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfclpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfclpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfclpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfclpf.version('2.1-git')
sfclpf.synopsis('''sfclpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y''','''''')
rsf.doc.progs['sfclpf']=sfclpf

sfcltft = rsf.doc.rsfprog('sfcltft','user/fomels/Mcltft.c','''Complex local time-frequency transform. ''')
sfcltft.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcltft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfcltft.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfcltft.par('dip',rsf.doc.rsfpar('bool','n','','''if y, do dip decomposition '''))
sfcltft.par('time',rsf.doc.rsfpar('bool','n','','''if y, decompose in time '''))
sfcltft.par('decompose',rsf.doc.rsfpar('bool','n','','''if y, output decomposition '''))
sfcltft.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius (in time, samples) '''))
sfcltft.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sfcltft.par('np',rsf.doc.rsfpar('int','','','''number of slopes '''))
sfcltft.par('dp',rsf.doc.rsfpar('float','','','''slope step '''))
sfcltft.par('p0',rsf.doc.rsfpar('float','','','''first slope '''))
sfcltft.par('nw',rsf.doc.rsfpar('int','kiss_fft_next_fast_size(n1)','','''number of frequencies '''))
sfcltft.par('dw',rsf.doc.rsfpar('float','1./(nw*d1)','','''frequency step '''))
sfcltft.par('w0',rsf.doc.rsfpar('float','-0.5/d1','','''first frequency '''))
sfcltft.par('basis',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfcltft.version('2.1-git')
sfcltft.synopsis('''sfcltft < in.rsf > out.rsf basis=basis.rsf inv=n verb=n dip=n time=n decompose=n rect=10 niter=100 np= dp= p0= nw=kiss_fft_next_fast_size(n1) dw=1./(nw*d1) w0=-0.5/d1''','''''')
rsf.doc.progs['sfcltft']=sfcltft

sfconstperm = rsf.doc.rsfprog('sfconstperm','user/fomels/Mconstperm.c','''Constant-velocity prestack exploding reflector. ''')
sfconstperm.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfconstperm.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sfconstperm.par('nz',rsf.doc.rsfpar('int','','','''depth samples (if migration) '''))
sfconstperm.par('dz',rsf.doc.rsfpar('float','','','''depth sampling (if migration) '''))
sfconstperm.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sfconstperm.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sfconstperm.par('nh',rsf.doc.rsfpar('int','','','''offset samples (if modeling) '''))
sfconstperm.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (if modeling) '''))
sfconstperm.par('v',rsf.doc.rsfpar('float','','','''velocity '''))
sfconstperm.version('2.1-git')
sfconstperm.synopsis('''sfconstperm < data.rsf > image.rsf mig=n snap=0 nz= dz= nt= dt= nh= dh= v=''','''''')
rsf.doc.progs['sfconstperm']=sfconstperm

sfconstpermh = rsf.doc.rsfprog('sfconstpermh','user/fomels/Mconstpermh.c','''Constant-velocity prestack exploding reflector in offset. ''')
sfconstpermh.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfconstpermh.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sfconstpermh.par('nz',rsf.doc.rsfpar('int','','','''depth samples (if migration) '''))
sfconstpermh.par('dz',rsf.doc.rsfpar('float','','','''depth sampling (if migration) '''))
sfconstpermh.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sfconstpermh.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sfconstpermh.par('nh',rsf.doc.rsfpar('int','','','''offset samples (if modeling) '''))
sfconstpermh.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (if modeling) '''))
sfconstpermh.par('v',rsf.doc.rsfpar('float','','','''velocity '''))
sfconstpermh.version('2.1-git')
sfconstpermh.synopsis('''sfconstpermh < data.rsf > image.rsf mig=n snap=0 nz= dz= nt= dt= nh= dh= v=''','''''')
rsf.doc.progs['sfconstpermh']=sfconstpermh

sfconstpermh1 = rsf.doc.rsfprog('sfconstpermh1','user/fomels/Mconstpermh1.c','''Constant-velocity prestack exploding reflector in offset. ''')
sfconstpermh1.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfconstpermh1.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sfconstpermh1.par('nz',rsf.doc.rsfpar('int','','','''depth samples (if migration) '''))
sfconstpermh1.par('dz',rsf.doc.rsfpar('float','','','''depth sampling (if migration) '''))
sfconstpermh1.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sfconstpermh1.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sfconstpermh1.par('nh',rsf.doc.rsfpar('int','','','''offset samples (if modeling) '''))
sfconstpermh1.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (if modeling) '''))
sfconstpermh1.par('v',rsf.doc.rsfpar('float','','','''velocity '''))
sfconstpermh1.version('2.1-git')
sfconstpermh1.synopsis('''sfconstpermh1 < data.rsf > image.rsf mig=n snap=0 nz= dz= nt= dt= nh= dh= v=''','''''')
rsf.doc.progs['sfconstpermh1']=sfconstpermh1

sfcosftwave1 = rsf.doc.rsfprog('sfcosftwave1','user/fomels/Mcosftwave1.c','''1-D FFT wave extrapolation using Cosine FT ''')
sfcosftwave1.par('prop',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcosftwave1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcosftwave1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcosftwave1.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfcosftwave1.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfcosftwave1.version('2.1-git')
sfcosftwave1.synopsis('''sfcosftwave1 < inp.rsf > out.rsf prop=prop.rsf left=left.rsf right=right.rsf nt= dt=''','''''')
rsf.doc.progs['sfcosftwave1']=sfcosftwave1

sfcpef = rsf.doc.rsfprog('sfcpef','user/fomels/Mcpef.c','''1-D prediction-error filter estimation from complex data ''')
sfcpef.par('single',rsf.doc.rsfpar('bool','y','','''single channel or multichannel '''))
sfcpef.par('nf',rsf.doc.rsfpar('int','','','''filter length '''))
sfcpef.version('2.1-git')
sfcpef.synopsis('''sfcpef < in.rsf > out.rsf single=y nf=''','''''')
rsf.doc.progs['sfcpef']=sfcpef

sfcr = rsf.doc.rsfprog('sfcr','user/fomels/Mcr.c','''Column-row matrix decomposition ''')
sfcr.par('col_in',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcr.par('col_out',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcr.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfcr.par('tol',rsf.doc.rsfpar('float','0.0f','','''CG tolerance '''))
sfcr.par('prec',rsf.doc.rsfpar('bool','y','','''If apply preconditioning '''))
sfcr.version('2.1-git')
sfcr.synopsis('''sfcr < row_in.rsf col_in=col_in.rsf > row_out.rsf col_out=col_out.rsf niter=10 tol=0.0f prec=y''','''''')
rsf.doc.progs['sfcr']=sfcr

sfdeblur = rsf.doc.rsfprog('sfdeblur','user/fomels/Mdeblur.c','''Non-stationary debluring by inversion ''')
sfdeblur.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdeblur.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdeblur.par('nliter',rsf.doc.rsfpar('int','1','','''number of nonlinear iterations '''))
sfdeblur.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdeblur.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfdeblur.version('2.1-git')
sfdeblur.synopsis('''sfdeblur < in.rsf > out.rsf rect=rect.rsf niter=100 nliter=1 verb=n eps=0.''','''''')
rsf.doc.progs['sfdeblur']=sfdeblur

sfdistance = rsf.doc.rsfprog('sfdistance','user/fomels/Mdistance.c','''Computing distance function by fast marching eikonal solver (3-D). ''')
sfdistance.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdistance.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfdistance.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfdistance.par('n3',rsf.doc.rsfpar('int','1','','''dimensions '''))
sfdistance.par('d1',rsf.doc.rsfpar('float','','',''''''))
sfdistance.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfdistance.par('d3',rsf.doc.rsfpar('float','d2','','''sampling '''))
sfdistance.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfdistance.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfdistance.par('o3',rsf.doc.rsfpar('float','0.','','''origin '''))
sfdistance.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfdistance.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfdistance.par('velocity',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdistance.version('2.1-git Meikonal.c 825 2004-10-07 08:11:17Z fomels')
sfdistance.synopsis('''sfdistance < points.rsf > dist.rsf velocity=vel.rsf n1= n2= n3=1 d1= d2= d3=d2 o1=0. o2=0. o3=0. order=2 vel=y''','''''')
rsf.doc.progs['sfdistance']=sfdistance

sfdivn = rsf.doc.rsfprog('sfdivn','user/fomels/Mdivn.c','''Smooth division. ''')
sfdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfdivn.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdivn.version('2.1-git')
sfdivn.synopsis('''sfdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''
December 2015 program of the month:
http://ahay.org/blog/2015/12/22/program-of-the-month-sfdivn/
''')
rsf.doc.progs['sfdivn']=sfdivn

sfdix = rsf.doc.rsfprog('sfdix','user/fomels/Mdix.c','''Convert RMS to interval velocity using LS and shaping regularization. ''')
sfdix.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdix.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfdix.par('rect#',rsf.doc.rsfpar('string','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdix.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdix.par('vrmsout',rsf.doc.rsfpar('string ',desc='''optionally, output predicted vrms (auxiliary output file name)'''))
sfdix.version('2.1-git')
sfdix.synopsis('''sfdix < vrms.rsf > vint.rsf weight=weight.rsf vrmsout=vout.rsf niter=100 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfdix']=sfdix

sfdpeiko = rsf.doc.rsfprog('sfdpeiko','user/fomels/Mdpeiko.c','''2-D eikonal solver based on dynamic programming. ''')
sfdpeiko.par('ishot',rsf.doc.rsfpar('int','(n1-1)/2','','''shot location '''))
sfdpeiko.version('2.1-git')
sfdpeiko.synopsis('''sfdpeiko < vel.rsf > ttime.rsf ishot=(n1-1)/2''','''''')
rsf.doc.progs['sfdpeiko']=sfdpeiko

sfeikonal = rsf.doc.rsfprog('sfeikonal','user/fomels/Meikonal.c','''Fast marching eikonal solver (3-D). ''')
sfeikonal.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikonal.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikonal.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikonal.par('sweep',rsf.doc.rsfpar('bool','n','','''if y, use fast sweeping instead of fast marching '''))
sfeikonal.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikonal.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikonal.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikonal.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonal.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikonal.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikonal.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikonal.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikonal.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikonal.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikonal.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikonal.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikonal.version('2.1-git')
sfeikonal.synopsis('''sfeikonal < vel.rsf > time.rsf shotfile=shots.rsf vel=y order=2 sweep=n br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3''','''
June 2014 program of the month:
http://ahay.org/blog/2014/06/11/program-of-the-month-sfeikonal/
''')
rsf.doc.progs['sfeikonal']=sfeikonal

sfeikonalvti = rsf.doc.rsfprog('sfeikonalvti','user/fomels/Meikonalvti.c','''Fast marching eikonal solver in VTI media. ''')
sfeikonalvti.par('shotfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeikonalvti.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfeikonalvti.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sfeikonalvti.par('br1',rsf.doc.rsfpar('float','d1','',''''''))
sfeikonalvti.par('br2',rsf.doc.rsfpar('float','d2','',''''''))
sfeikonalvti.par('br3',rsf.doc.rsfpar('float','d3','','''Constant-velocity box around the source (in physical dimensions) '''))
sfeikonalvti.par('plane1',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonalvti.par('plane2',rsf.doc.rsfpar('bool','n','',''''''))
sfeikonalvti.par('plane3',rsf.doc.rsfpar('bool','n','','''plane-wave source '''))
sfeikonalvti.par('b1',rsf.doc.rsfpar('int','plane[2]? n1: (int) (br1/d1+0.5)','',''''''))
sfeikonalvti.par('b2',rsf.doc.rsfpar('int','plane[1]? n2: (int) (br2/d2+0.5)','',''''''))
sfeikonalvti.par('b3',rsf.doc.rsfpar('int','plane[0]? n3: (int) (br3/d3+0.5)','','''Constant-velocity box around the source (in samples) '''))
sfeikonalvti.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikonalvti.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikonalvti.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikonalvti.par('vx',rsf.doc.rsfpar('string ',desc=''''''))
sfeikonalvti.par('eta',rsf.doc.rsfpar('string ',desc=''''''))
sfeikonalvti.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) (auxiliary input file name)'''))
sfeikonalvti.version('2.1-git Meikonal.c 1507 2005-10-22 04:01:28Z savap')
sfeikonalvti.synopsis('''sfeikonalvti < vzf.rsf > time.rsf shotfile=shots.rsf vel=y order=2 br1=d1 br2=d2 br3=d3 plane1=n plane2=n plane3=n b1=plane[2]? n1: (int) (br1/d1+0.5) b2=plane[1]? n2: (int) (br2/d2+0.5) b3=plane[0]? n3: (int) (br3/d3+0.5) zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3 vx= eta=''','''''')
rsf.doc.progs['sfeikonalvti']=sfeikonalvti

sfeno2 = rsf.doc.rsfprog('sfeno2','user/fomels/Meno2.c','''Convert velocity to slowness and compute gradient using ENO interpolation ''')
sfeno2.par('order',rsf.doc.rsfpar('int','3','','''interpolation order '''))
sfeno2.par('is_inverse',rsf.doc.rsfpar('bool','1','','''make vel to slowness '''))
sfeno2.version('2.1-git')
sfeno2.synopsis('''sfeno2 < vel.rsf > out.rsf order=3 is_inverse=1''','''''')
rsf.doc.progs['sfeno2']=sfeno2

sferf = rsf.doc.rsfprog('sferf','user/fomels/Merf.c','''Bandpass filtering using erf function. ''')
sferf.par('flo',rsf.doc.rsfpar('float','-1.','','''low frequency in band '''))
sferf.par('fhi',rsf.doc.rsfpar('float','-1.','','''high frequency in band '''))
sferf.par('rect',rsf.doc.rsfpar('float','1','','''filter sharpness '''))
sferf.par('spline',rsf.doc.rsfpar('bool','n','','''if use B-spline erf '''))
sferf.par('der',rsf.doc.rsfpar('bool','n','','''compute derivative '''))
sferf.version('2.1-git')
sferf.synopsis('''sferf < in.rsf > out.rsf flo=-1. fhi=-1. rect=1 spline=n der=n''','''''')
rsf.doc.progs['sferf']=sferf

sfexgr = rsf.doc.rsfprog('sfexgr','user/fomels/Mexgr.c','''Exact group velocity in VTI media ''')
sfexgr.par('aq',rsf.doc.rsfpar('float','14.47','',''''''))
sfexgr.par('bq',rsf.doc.rsfpar('float','2.28','',''''''))
sfexgr.par('cq',rsf.doc.rsfpar('float','9.57','',''''''))
sfexgr.par('dq',rsf.doc.rsfpar('float','4.51','',''''''))
sfexgr.version('2.1-git')
sfexgr.synopsis('''sfexgr > out.rsf aq=14.47 bq=2.28 cq=9.57 dq=4.51''','''''')
rsf.doc.progs['sfexgr']=sfexgr

sffft2 = rsf.doc.rsfprog('sffft2','user/fomels/Mfft2.c','''Test 2-D Fourier transform. ''')
sffft2.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag '''))
sffft2.par('n1',rsf.doc.rsfpar('int','','',''''''))
sffft2.par('n2',rsf.doc.rsfpar('int','','',''''''))
sffft2.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffft2.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffft2.version('2.1-git')
sffft2.synopsis('''sffft2 < freq.rsf > space.rsf inv=n n1= n2= cmplx=n pad1=1''','''''')
rsf.doc.progs['sffft2']=sffft2

sffftexp0 = rsf.doc.rsfprog('sffftexp0','user/fomels/Mfftexp0.c','''2-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sffftexp0.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftexp0.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp0.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp0.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp0.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftexp0.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftexp0.par('trm',rsf.doc.rsfpar('bool','n','','''time-reversal imaging '''))
sffftexp0.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp0.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp0.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp0.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp0.par('t0',rsf.doc.rsfpar('float','0.0f','','''time origin (if modeling) '''))
sffftexp0.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftexp0.version('2.1-git')
sffftexp0.synopsis('''sffftexp0 < data.rsf > image.rsf snaps=snaps.rsf left=left.rsf right=right.rsf mig=n cmplx=n pad1=1 trm=n nz= dz= nt= dt= t0=0.0f snap=0''','''''')
rsf.doc.progs['sffftexp0']=sffftexp0

sffftexp1 = rsf.doc.rsfprog('sffftexp1','user/fomels/Mfftexp1.c','''2-D FFT-based prestack exploding reflector modeling/migration  ''')
sffftexp1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp1.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp1.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftexp1.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp1.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp1.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp1.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp1.par('nh',rsf.doc.rsfpar('int','','','''offset samples (if modeling) '''))
sffftexp1.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (if modeling) '''))
sffftexp1.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftexp1.par('sub',rsf.doc.rsfpar('bool','y','','''if -1 is included in the matrix '''))
sffftexp1.version('2.1-git')
sffftexp1.synopsis('''sffftexp1 < data.rsf > image.rsf left=left.rsf right=right.rsf mig=n snap=0 nz= dz= nt= dt= nh= dh= cmplx=n sub=y''','''''')
rsf.doc.progs['sffftexp1']=sffftexp1

sffftexp3 = rsf.doc.rsfprog('sffftexp3','user/fomels/Mfftexp3.c','''3-D FFT-based zero-offset exploding reflector modeling/migration  ''')
sffftexp3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftexp3.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sffftexp3.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sffftexp3.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sffftexp3.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sffftexp3.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sffftexp3.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sffftexp3.version('2.1-git')
sffftexp3.synopsis('''sffftexp3 < data.rsf > image.rsf left=left.rsf right=right.rsf mig=n ompchunk=1 nz= dz= nt= dt=''','''''')
rsf.doc.progs['sffftexp3']=sffftexp3

sffftone = rsf.doc.rsfprog('sffftone','user/fomels/Mfftone.c','''Test 1-D Fourier transform. ''')
sffftone.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag '''))
sffftone.par('n1',rsf.doc.rsfpar('int','','','''dimension (for inv=y) '''))
sffftone.version('2.1-git')
sffftone.synopsis('''sffftone < freq.rsf > space.rsf inv=n n1=''','''''')
rsf.doc.progs['sffftone']=sffftone

sfffttest = rsf.doc.rsfprog('sfffttest','user/fomels/Mffttest.c','''Test 3-D Fourier transform. ''')
sfffttest.par('inv',rsf.doc.rsfpar('bool','n','','''inverse flag '''))
sfffttest.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfffttest.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfffttest.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfffttest.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sfffttest.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sfffttest.version('2.1-git')
sfffttest.synopsis('''sfffttest < freq.rsf > space.rsf inv=n n1= n2= n3= cmplx=n pad1=1''','''''')
rsf.doc.progs['sfffttest']=sfffttest

sffftwave1 = rsf.doc.rsfprog('sffftwave1','user/fomels/Mfftwave1.c','''1-D FFT wave extrapolation ''')
sffftwave1.par('prop',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave1.par('nt',rsf.doc.rsfpar('int','','',''''''))
sffftwave1.par('dt',rsf.doc.rsfpar('float','','',''''''))
sffftwave1.par('sub',rsf.doc.rsfpar('bool','y','','''if -1 is included in the matrix '''))
sffftwave1.par('step',rsf.doc.rsfpar('bool','y','','''if two-step propagation '''))
sffftwave1.par('nsps',rsf.doc.rsfpar('bool','n','','''if using NSPS '''))
sffftwave1.par('right',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffftwave1.version('2.1-git')
sffftwave1.synopsis('''sffftwave1 < inp.rsf > out.rsf prop=prop.rsf right=right.rsf nt= dt= sub=y step=y nsps=n''','''''')
rsf.doc.progs['sffftwave1']=sffftwave1

sffftwave2 = rsf.doc.rsfprog('sffftwave2','user/fomels/Mfftwave2.c','''Simple 2-D wave propagation ''')
sffftwave2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffftwave2.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave2.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave2.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave2.version('2.1-git')
sffftwave2.synopsis('''sffftwave2 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=n snap=0 cmplx=n pad1=1''','''''')
rsf.doc.progs['sffftwave2']=sffftwave2

sffftwave3 = rsf.doc.rsfprog('sffftwave3','user/fomels/Mfftwave3.c','''Simple 3-D wave propagation ''')
sffftwave3.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sffftwave3.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave3.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave3.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave3.version('2.1-git')
sffftwave3.synopsis('''sffftwave3 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=y cmplx=n pad1=1 snap=0''','''''')
rsf.doc.progs['sffftwave3']=sffftwave3

sffindmin2 = rsf.doc.rsfprog('sffindmin2','user/fomels/Mfindmin2.c','''Find minimum in 2-D ''')
sffindmin2.par('gate1',rsf.doc.rsfpar('int','3','',''''''))
sffindmin2.par('gate2',rsf.doc.rsfpar('int','3','','''picking gate '''))
sffindmin2.version('2.1-git')
sffindmin2.synopsis('''sffindmin2 < inp.rsf > out.rsf gate1=3 gate2=3''','''''')
rsf.doc.progs['sffindmin2']=sffindmin2

sffocus = rsf.doc.rsfprog('sffocus','user/fomels/Mfocus.c','''Focusing indicator. ''')
sffocus.par('dim',rsf.doc.rsfpar('int','','','''dimensionality '''))
sffocus.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffocus.par('verb',rsf.doc.rsfpar('bool','y','',''''''))
sffocus.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sffocus.version('2.1-git')
sffocus.synopsis('''sffocus < in.rsf > out.rsf dim= niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sffocus']=sffocus

sffpow = rsf.doc.rsfprog('sffpow','user/fomels/Mfpow.c','''Time/frequency power estimation ''')
sffpow.par('beta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffpow.par('niter',rsf.doc.rsfpar('int','10','','''number of Newton iterations '''))
sffpow.par('fmin',rsf.doc.rsfpar('float','o1','','''minimum frequency '''))
sffpow.par('fmax',rsf.doc.rsfpar('float','o1+(n1-1)*d1','','''maximum frequency '''))
sffpow.par('bmin',rsf.doc.rsfpar('float','-1.0','','''minimum value of beta '''))
sffpow.par('bmax',rsf.doc.rsfpar('float','1.0','','''maximum value of beta '''))
sffpow.par('nb',rsf.doc.rsfpar('int','10','',''''''))
sffpow.par('tol',rsf.doc.rsfpar('float','SF_EPS','','''accuracy tolerance for beta '''))
sffpow.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffpow.par('time',rsf.doc.rsfpar('bool','n','','''time axis '''))
sffpow.version('2.1-git')
sffpow.synopsis('''sffpow < inp.rsf > out.rsf beta=beta.rsf niter=10 fmin=o1 fmax=o1+(n1-1)*d1 bmin=-1.0 bmax=1.0 nb=10 tol=SF_EPS verb=y time=n''','''''')
rsf.doc.progs['sffpow']=sffpow

sffreqest = rsf.doc.rsfprog('sffreqest','user/fomels/Mfreqest.c','''Local frequency estimation ''')
sffreqest.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffreqest.par('hertz',rsf.doc.rsfpar('bool','n','','''if y, convert output to Hertz '''))
sffreqest.version('2.1-git Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sffreqest.synopsis('''sffreqest < in.rsf > out.rsf niter=100 hertz=n rect1=1 rect2=1 ... ''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sffreqest']=sffreqest

sfgaussmooth = rsf.doc.rsfprog('sfgaussmooth','user/fomels/Mgaussmooth.c','''Recursive Gaussian smoothing on the fast axis. ''')
sfgaussmooth.par('der',rsf.doc.rsfpar('bool','n','','''compute derivative '''))
sfgaussmooth.par('rect',rsf.doc.rsfpar('float','1','','''smoothing radius '''))
sfgaussmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfgaussmooth.version('2.1-git')
sfgaussmooth.synopsis('''sfgaussmooth < in.rsf > out.rsf der=n rect=1 repeat=1''','''''')
rsf.doc.progs['sfgaussmooth']=sfgaussmooth

sfgbeamform = rsf.doc.rsfprog('sfgbeamform','user/fomels/Mgbeamform.c','''2-D lateral smoothing. ''')
sfgbeamform.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfgbeamform.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag '''))
sfgbeamform.par('repeat',rsf.doc.rsfpar('int','2','','''triangle convolutions '''))
sfgbeamform.version('2.1-git')
sfgbeamform.synopsis('''sfgbeamform < in.rsf > out.rsf rect=3 adj=y repeat=2''','''''')
rsf.doc.progs['sfgbeamform']=sfgbeamform

sfimray = rsf.doc.rsfprog('sfimray','user/fomels/Mimray.c','''2-D image ray tracing using HWT ''')
sfimray.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfimray.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfimray.par('order',rsf.doc.rsfpar('int','3','','''interpolation order '''))
sfimray.version('2.1-git')
sfimray.synopsis('''sfimray < vel.rsf > dix.rsf nt= dt= order=3''','''''')
rsf.doc.progs['sfimray']=sfimray

sfinterf = rsf.doc.rsfprog('sfinterf','user/fomels/Minterf.c','''Create an interferometric matrix ''')
sfinterf.version('2.1-git')
sfinterf.synopsis('''sfinterf < inp.rsf > out.rsf''','''''')
rsf.doc.progs['sfinterf']=sfinterf

sfinterp2 = rsf.doc.rsfprog('sfinterp2','user/fomels/Minterp2.c','''Multiple-arrival interpolation. ''')
sfinterp2.par('size',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinterp2.par('grid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinterp2.par('sx',rsf.doc.rsfpar('float','0.','',''''''))
sfinterp2.par('sz',rsf.doc.rsfpar('float','0.','','''Shot coordinates '''))
sfinterp2.par('nw',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sfinterp2.par('plane',rsf.doc.rsfpar('int','0','','''0: point-source, 4: plane-wave '''))
sfinterp2.version('2.1-git Minterp2.c 4084 2009-01-22 21:39:08Z sfomel')
sfinterp2.synopsis('''sfinterp2 < in.rsf size=size.rsf > out.rsf grid=grid.rsf sx=0. sz=0. nw=4 plane=0''','''''')
rsf.doc.progs['sfinterp2']=sfinterp2

sfinterpt = rsf.doc.rsfprog('sfinterpt','user/fomels/Minterpt.c','''Multiple-arrival interpolation (yet another).''')
sfinterpt.par('sx',rsf.doc.rsfpar('float','0.','',''''''))
sfinterpt.par('sz',rsf.doc.rsfpar('float','0.','','''Shot coordinate '''))
sfinterpt.par('nw',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sfinterpt.version('2.1-git')
sfinterpt.synopsis('''sfinterpt < in.rsf > out.rsf sx=0. sz=0. nw=4''','''''')
rsf.doc.progs['sfinterpt']=sfinterpt

sfiphase = rsf.doc.rsfprog('sfiphase','user/fomels/Miphase.c','''Smooth estimate of instantaneous frequency. ''')
sfiphase.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfiphase.par('complex',rsf.doc.rsfpar('bool','n','','''if y, use complex-valued computations '''))
sfiphase.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfiphase.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfiphase.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfiphase.par('hertz',rsf.doc.rsfpar('bool','n','','''if y, convert output to Hertz '''))
sfiphase.par('band',rsf.doc.rsfpar('bool','n','','''if y, compute instantaneous bandwidth '''))
sfiphase.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfiphase.version('2.1-git')
sfiphase.synopsis('''sfiphase < in.rsf > out.rsf verb=n complex=n niter=100 order=100 ref=1. hertz=n band=n rect#=(1,1,...)''','''''')
rsf.doc.progs['sfiphase']=sfiphase

sfkdsort = rsf.doc.rsfprog('sfkdsort','user/fomels/Mkdsort.c','''Sort entries based on k-D tree. ''')
sfkdsort.version('2.1-git')
sfkdsort.synopsis('''sfkdsort < inp.rsf > out.rsf''','''''')
rsf.doc.progs['sfkdsort']=sfkdsort

sfkdtree = rsf.doc.rsfprog('sfkdtree','user/fomels/Mkdtree.c','''Test k-D tree algorithm. ''')
sfkdtree.par('point',rsf.doc.rsfpar('floats','','',''' [nd]'''))
sfkdtree.version('2.1-git')
sfkdtree.synopsis('''sfkdtree < inp.rsf > out.rsf point=''','''''')
rsf.doc.progs['sfkdtree']=sfkdtree

sfkron = rsf.doc.rsfprog('sfkron','user/fomels/Mkron.c','''Kroneker product with square matrices ''')
sfkron.par('mat1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkron.par('mat2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkron.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfkron.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfkron.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfkron.par('eps',rsf.doc.rsfpar('float','0.','','''regularization '''))
sfkron.par('nliter',rsf.doc.rsfpar('int','1','','''number of nonlinear iterations '''))
sfkron.version('2.1-git')
sfkron.synopsis('''sfkron < in.rsf > out.rsf mat1=mat1.rsf mat2=mat2.rsf adj=n inv=n niter=100 eps=0. nliter=1''','''''')
rsf.doc.progs['sfkron']=sfkron

sflabel = rsf.doc.rsfprog('sflabel','user/fomels/Mlabel.c','''Connected-component labeling ''')
sflabel.version('2.1-git')
sflabel.synopsis('''sflabel < inp.rsf > out.rsf''','''''')
rsf.doc.progs['sflabel']=sflabel

sflegacy = rsf.doc.rsfprog('sflegacy','user/fomels/Mlegacy.c','''Merging legacy and hires datasets ''')
sflegacy.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflegacy.par('hweight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflegacy.par('lweight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflegacy.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sflegacy.version('2.1-git')
sflegacy.synopsis('''sflegacy < in.rsf > out.rsf rect=rect.rsf hweight=hweight.rsf lweight=lweight.rsf adj=n''','''''')
rsf.doc.progs['sflegacy']=sflegacy

sflfftexp0 = rsf.doc.rsfprog('sflfftexp0','user/fomels/Mlfftexp0.c','''2-D FFT-based zero-offset exploding reflector modeling/migration as linear operator  ''')
sflfftexp0.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflfftexp0.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflfftexp0.par('adj',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sflfftexp0.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sflfftexp0.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sflfftexp0.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sflfftexp0.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sflfftexp0.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sflfftexp0.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sflfftexp0.version('2.1-git')
sflfftexp0.synopsis('''sflfftexp0 < data.rsf > image.rsf left=left.rsf right=right.rsf adj=n cmplx=n pad1=1 nz= dz= nt= dt=''','''''')
rsf.doc.progs['sflfftexp0']=sflfftexp0

sfllpf = rsf.doc.rsfprog('sfllpf','user/fomels/Mllpf.c','''Local prediction filter (n-dimensional) with an adjoint flag. ''')
sfllpf.par('basis',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfllpf.par('adj',rsf.doc.rsfpar('bool','n','',''''''))
sfllpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfllpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfllpf.version('2.1-git')
sfllpf.synopsis('''sfllpf basis=dat.rsf < mat.rsf > flt.rsf adj=n niter=100 verb=y''','''''')
rsf.doc.progs['sfllpf']=sfllpf

sflocalskew = rsf.doc.rsfprog('sflocalskew','user/fomels/Mlocalskew.c','''Rotate phase and compute local skewness. ''')
sflocalskew.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sflocalskew.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sflocalskew.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sflocalskew.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sflocalskew.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sflocalskew.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflocalskew.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sflocalskew.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sflocalskew.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sflocalskew.par('const',rsf.doc.rsfpar('bool','n','','''if y, compute inverse varimax '''))
sflocalskew.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflocalskew.version('2.1-git')
sflocalskew.synopsis('''sflocalskew < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3 const=n eps=0.0f''','''''')
rsf.doc.progs['sflocalskew']=sflocalskew

sflocov = rsf.doc.rsfprog('sflocov','user/fomels/Mlocov.c','''Local covariance filter ''')
sflocov.par('na',rsf.doc.rsfpar('int','1','',''''''))
sflocov.par('nb',rsf.doc.rsfpar('int','1','',''''''))
sflocov.par('a0',rsf.doc.rsfpar('float','','',''''''))
sflocov.par('b0',rsf.doc.rsfpar('float','','',''''''))
sflocov.par('a1',rsf.doc.rsfpar('float','a0','',''''''))
sflocov.par('b1',rsf.doc.rsfpar('float','b0','',''''''))
sflocov.version('2.1-git')
sflocov.synopsis('''sflocov < inp.rsf > out.rsf na=1 nb=1 a0= b0= a1=a0 b1=b0''','''''')
rsf.doc.progs['sflocov']=sflocov

sflpf = rsf.doc.rsfprog('sflpf','user/fomels/Mlpf.c','''Local prediction filter (n-dimensional). ''')
sflpf.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflpf.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpf.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflpf.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sflpf.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflpf.par('pef',rsf.doc.rsfpar('string ',desc='''signal PEF file (optional) '''))
sflpf.par('lag',rsf.doc.rsfpar('string ',desc='''file with PEF lags (optional) '''))
sflpf.version('2.1-git')
sflpf.synopsis('''sflpf < dat.rsf match=mat.rsf > flt.rsf pred=pre.rsf niter=100 verb=y pef= lag=''','''''')
rsf.doc.progs['sflpf']=sflpf

sflrmig0 = rsf.doc.rsfprog('sflrmig0','user/fomels/Mlrmig0.c','''Fast zero-offset time migration ''')
sflrmig0.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflrmig0.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflrmig0.version('2.1-git')
sflrmig0.synopsis('''sflrmig0 < inp.rsf > mig.rsf left=left.rsf right=right.rsf''','''''')
rsf.doc.progs['sflrmig0']=sflrmig0

sflsfit = rsf.doc.rsfprog('sflsfit','user/fomels/Mlsfit.c','''Simple least-squares regression. ''')
sflsfit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsfit.par('linear',rsf.doc.rsfpar('bool','y','','''if linear LS '''))
sflsfit.par('dim',rsf.doc.rsfpar('int','dim','','''number of dimensions '''))
sflsfit.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization parameter '''))
sflsfit.par('coef',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sflsfit.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsfit.version('2.1-git')
sflsfit.synopsis('''sflsfit < inp.rsf fit=fit.rsf > out.rsf coef=coef.rsf weight=wht.rsf linear=y dim=dim eps=0.0f''','''''')
rsf.doc.progs['sflsfit']=sflsfit

sfmax2 = rsf.doc.rsfprog('sfmax2','user/fomels/Mmax2.c','''Picking local maxima in 2-D ''')
sfmax2.par('np',rsf.doc.rsfpar('int','n12','','''maximum number of picks '''))
sfmax2.version('2.1-git')
sfmax2.synopsis('''sfmax2 < in.rsf > out.rsf np=n12''','''''')
rsf.doc.progs['sfmax2']=sfmax2

sfmedian = rsf.doc.rsfprog('sfmedian','user/fomels/Mmedian.c','''Compute median on the first axis. ''')
sfmedian.version('2.1-git')
sfmedian.synopsis('''sfmedian < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfmedian']=sfmedian

sfmffit = rsf.doc.rsfprog('sfmffit','user/fomels/Mmffit.c','''Fitting multi-focusing approximations ''')
sfmffit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmffit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmffit.par('x0',rsf.doc.rsfpar('float','m0','','''central midpoint '''))
sfmffit.par('type',rsf.doc.rsfpar('string ',desc='''Type of approximation (crs,mf,nonhyperbolic) '''))
sfmffit.version('2.1-git')
sfmffit.synopsis('''sfmffit < in.rsf coef=coef.rsf > out.rsf fit=fit.rsf x0=m0 type=''','''''')
rsf.doc.progs['sfmffit']=sfmffit

sfmig3 = rsf.doc.rsfprog('sfmig3','user/fomels/Mmig3.c','''3-D Kirchhoff time migration with antialiasing. ''')
sfmig3.par('hdr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmig3.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o2',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('d3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('o3',rsf.doc.rsfpar('float','','',''''''))
sfmig3.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfmig3.par('vel',rsf.doc.rsfpar('float','','','''migration velocity '''))
sfmig3.par('antialias',rsf.doc.rsfpar('string ',desc='''antialiasing type [triangle,flat,steep,none] '''))
sfmig3.version('2.1-git')
sfmig3.synopsis('''sfmig3 < in.rsf hdr=head.rsf > mig.rsf n2= d2= o2= n3= d3= o3= n1= vel= antialias=''','''''')
rsf.doc.progs['sfmig3']=sfmig3

sfmiss3 = rsf.doc.rsfprog('sfmiss3','user/fomels/Mmiss3.c','''Missing data interpolation (N-dimensional) using shaping regularization. ''')
sfmiss3.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmiss3.par('niter',rsf.doc.rsfpar('int','100','','''Number of iterations '''))
sfmiss3.par('force',rsf.doc.rsfpar('bool','y','','''if y, keep known values '''))
sfmiss3.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfmiss3.version('2.1-git')
sfmiss3.synopsis('''sfmiss3 < in.rsf > out.rsf mask=mask.rsf niter=100 force=y''','''''')
rsf.doc.progs['sfmiss3']=sfmiss3

sfmorph = rsf.doc.rsfprog('sfmorph','user/fomels/Mmorph.c','''Morphological operations on binary images ''')
sfmorph.par('what',rsf.doc.rsfpar('string ',desc=''''''))
sfmorph.version('2.1-git')
sfmorph.synopsis('''sfmorph < inp.rsf > out.rsf what=''','''''')
rsf.doc.progs['sfmorph']=sfmorph

sfnconv = rsf.doc.rsfprog('sfnconv','user/fomels/Mnconv.c','''Non-stationary convolution ''')
sfnconv.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnconv.par('lag',rsf.doc.rsfpar('int','(ntau+1)/2','','''filter lag '''))
sfnconv.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfnconv.version('2.1-git')
sfnconv.synopsis('''sfnconv < inp.rsf filt=flt.rsf > out.rsf lag=(ntau+1)/2 adj=n''','''''')
rsf.doc.progs['sfnconv']=sfnconv

sfnnint = rsf.doc.rsfprog('sfnnint','user/fomels/Mnnint.c','''Natural neighbor interpolation (2-D) ''')
sfnnint.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnint.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnint.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfnnint.par('n2',rsf.doc.rsfpar('int','','','''dimensions '''))
sfnnint.par('d1',rsf.doc.rsfpar('float','','',''''''))
sfnnint.par('d2',rsf.doc.rsfpar('float','','','''sampling '''))
sfnnint.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfnnint.par('o2',rsf.doc.rsfpar('float','0.','','''origin '''))
sfnnint.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order for distance calculation '''))
sfnnint.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfnnint.par('dist',rsf.doc.rsfpar('bool','n','','''if output distance '''))
sfnnint.par('voro',rsf.doc.rsfpar('bool','n','','''if output Voronoi diagram '''))
sfnnint.par('repeat',rsf.doc.rsfpar('int','1','',''''''))
sfnnint.par('velocity',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnnint.version('2.1-git')
sfnnint.synopsis('''sfnnint < ord.rsf coord=coord.rsf > grid.rsf velocity=vel.rsf n1= n2= d1= d2= o1=0. o2=0. order=2 vel=y dist=n voro=n repeat=1''','''''')
rsf.doc.progs['sfnnint']=sfnnint

sfnnshape = rsf.doc.rsfprog('sfnnshape','user/fomels/Mnnshape.c','''2-D irregular data interpolation using natural neighbors and shaping regularization. ''')
sfnnshape.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnshape.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnshape.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfnnshape.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfnnshape.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sfnnshape.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sfnnshape.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfnnshape.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfnnshape.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfnnshape.par('niter',rsf.doc.rsfpar('int','niter','','''GMRES memory '''))
sfnnshape.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sfnnshape.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing regularization '''))
sfnnshape.par('nw',rsf.doc.rsfpar('int','2','','''interpolator size '''))
sfnnshape.par('sym',rsf.doc.rsfpar('bool','n','','''if y, use symmetric shaping '''))
sfnnshape.par('tol',rsf.doc.rsfpar('float','1e-3','','''tolerance for stopping iteration '''))
sfnnshape.par('pattern',rsf.doc.rsfpar('string ',desc='''pattern file for output dimensions (auxiliary input file name)'''))
sfnnshape.version('2.1-git')
sfnnshape.synopsis('''sfnnshape < in.rsf > out.rsf coord=coord.rsf pattern=pattern.rsf n1= n2= d1=1. d2=1. o1=0. o2=0. niter=10 niter=niter rect1=1 rect2=1 nw=2 sym=n tol=1e-3''','''''')
rsf.doc.progs['sfnnshape']=sfnnshape

sfnnshapet = rsf.doc.rsfprog('sfnnshapet','user/fomels/Mnnshapet.c','''2-D irregular data interpolation of traces using natural neighbors and shaping regularization. ''')
sfnnshapet.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnshapet.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnshapet.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnnshapet.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfnnshapet.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfnnshapet.par('d1',rsf.doc.rsfpar('float','1.','',''''''))
sfnnshapet.par('d2',rsf.doc.rsfpar('float','1.','',''''''))
sfnnshapet.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfnnshapet.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfnnshapet.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfnnshapet.par('niter',rsf.doc.rsfpar('int','niter','','''GMRES memory '''))
sfnnshapet.par('eps',rsf.doc.rsfpar('float','1.0e-6','','''division parameter '''))
sfnnshapet.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sfnnshapet.par('rect2',rsf.doc.rsfpar('int','1','',''''''))
sfnnshapet.par('rect3',rsf.doc.rsfpar('int','1','','''smoothing regularization '''))
sfnnshapet.par('nw',rsf.doc.rsfpar('int','2','','''interpolator size '''))
sfnnshapet.par('sym',rsf.doc.rsfpar('bool','n','','''if y, use symmetric shaping '''))
sfnnshapet.par('tol',rsf.doc.rsfpar('float','1e-3','','''tolerance for stopping iteration '''))
sfnnshapet.par('pattern',rsf.doc.rsfpar('string ',desc='''pattern file for output dimensions (auxiliary input file name)'''))
sfnnshapet.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnnshapet.version('2.1-git')
sfnnshapet.synopsis('''sfnnshapet < in.rsf > out.rsf coord=coord.rsf pattern=pattern.rsf weight=weight.rsf n1= n2= d1=1. d2=1. o1=0. o2=0. niter=10 niter=niter eps=1.0e-6 rect1=1 rect2=1 rect3=1 nw=2 sym=n tol=1e-3''','''''')
rsf.doc.progs['sfnnshapet']=sfnnshapet

sfnsmooth = rsf.doc.rsfprog('sfnsmooth','user/fomels/Mnsmooth.c','''N-D non-stationary smoothing. ''')
sfnsmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfnsmooth.par('rect#',rsf.doc.rsfpar('string','','','''size of the smoothing stencil in #-th dimension /auxiliary input file/ '''))
sfnsmooth.par('shift#',rsf.doc.rsfpar('string','','','''shifting of the smoothing stencil in #-th dimension /auxiliary input file/ '''))
sfnsmooth.version('2.1-git Msmooth.c 691 2004-07-04 19:28:08Z fomels')
sfnsmooth.synopsis('''sfnsmooth < in.rsf > out.rsf repeat=1 rect#= shift#=''','''''')
rsf.doc.progs['sfnsmooth']=sfnsmooth

sfnsmooth1 = rsf.doc.rsfprog('sfnsmooth1','user/fomels/Mnsmooth1.c','''1-D non-stationary smoothing. ''')
sfnsmooth1.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnsmooth1.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfnsmooth1.version('2.1-git Msmooth.c 691 2004-07-04 19:28:08Z fomels')
sfnsmooth1.synopsis('''sfnsmooth1 < in.rsf > out.rsf rect=rect.rsf repeat=1''','''''')
rsf.doc.progs['sfnsmooth1']=sfnsmooth1

sfocparcel = rsf.doc.rsfprog('sfocparcel','user/fomels/Mocparcel.c','''Patching test for out-of-core patching. ''')
sfocparcel.par('w',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.par('k',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfocparcel.version('2.1-git Mparcel.c 691 2004-07-04 19:28:08Z fomels')
sfocparcel.synopsis('''sfocparcel < in.rsf > out.rsf w= k=''','''''')
rsf.doc.progs['sfocparcel']=sfocparcel

sfoctentwt = rsf.doc.rsfprog('sfoctentwt','user/fomels/Moctentwt.c','''Tent-like weight for out-of-core patching. ''')
sfoctentwt.par('windwt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfoctentwt.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfoctentwt.par('k',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfoctentwt.par('a',rsf.doc.rsfpar('ints','','','''filter size  [dim]'''))
sfoctentwt.par('center',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfoctentwt.par('dim',rsf.doc.rsfpar('int','2','','''number of dimensions '''))
sfoctentwt.version('2.1-git Mtentwt.c 691 2004-07-04 19:28:08Z fomels')
sfoctentwt.synopsis('''sfoctentwt > wallwt.rsf windwt=windwt.rsf w= k= a= center= dim=2''','''''')
rsf.doc.progs['sfoctentwt']=sfoctentwt

sfofilp = rsf.doc.rsfprog('sfofilp','user/fomels/Mofilp.c','''2-D missing data interpolation by differential offset continuation. ''')
sfofilp.par('known',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfofilp.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfofilp.par('simple',rsf.doc.rsfpar('bool','n','','''if y, use simple h derivative for regularization '''))
sfofilp.version('2.1-git')
sfofilp.synopsis('''sfofilp < in.rsf > out.rsf known=known.rsf niter=10 simple=n''','''''')
rsf.doc.progs['sfofilp']=sfofilp

sfofsemb = rsf.doc.rsfprog('sfofsemb','user/fomels/Mofsemb.c','''Objective function of dip estimation with semblance. ''')
sfofsemb.par('np',rsf.doc.rsfpar('int','100','','''number of dips '''))
sfofsemb.par('p0',rsf.doc.rsfpar('float','','','''dip origin '''))
sfofsemb.par('dp',rsf.doc.rsfpar('float','2*p0/(1.-np)','','''dip sampling '''))
sfofsemb.version('2.1-git')
sfofsemb.synopsis('''sfofsemb < in.rsf > of.rsf np=100 p0= dp=2*p0/(1.-np)''','''''')
rsf.doc.progs['sfofsemb']=sfofsemb

sfortho = rsf.doc.rsfprog('sfortho','user/fomels/Mortho.c','''Orthogonolize signal and noise. ''')
sfortho.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortho.par('sig2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortho.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfortho.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfortho.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfortho.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfortho.version('2.1-git')
sfortho.synopsis('''sfortho < fnoi.rsf sig=fsig.rsf > fnoi2.rsf sig2=fsig2.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfortho']=sfortho

sfpatch = rsf.doc.rsfprog('sfpatch','user/fomels/Mpatch.c','''Patching (N-dimensional). ''')
sfpatch.par('n0',rsf.doc.rsfpar('ints','','','''data dimensions (for inv=y)  [dim]'''))
sfpatch.par('w',rsf.doc.rsfpar('ints','','','''window size  [dim]'''))
sfpatch.par('p',rsf.doc.rsfpar('ints','','','''number of windows  [dim]'''))
sfpatch.par('inv',rsf.doc.rsfpar('bool','n','','''inverse or forward operation '''))
sfpatch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpatch.par('weight',rsf.doc.rsfpar('bool','n','','''if y, apply weighting to each patch '''))
sfpatch.par('dim',rsf.doc.rsfpar('int','dim0','',''''''))
sfpatch.version('2.1-git')
sfpatch.synopsis('''sfpatch < in.rsf > out.rsf n0= w= p= inv=n verb=n weight=n dim=dim0''','''
w is window size (defaults to n1,n2,...)
p is number of patches in different dimensions (defaults to 1,1,...)

If inv=n, the number of output dimensions is twice the number of input dimensions.
If inv=y, the number of output dimensions is half the number of input dimensions.

September 2013 program of the month:
http://ahay.org/blog/2013/09/14/program-of-the-month-sfpatch/
''')
rsf.doc.progs['sfpatch']=sfpatch

sfpchain = rsf.doc.rsfprog('sfpchain','user/fomels/Mpchain.c','''Nonstationary Prony by chain of PEFs ''')
sfpchain.par('pef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpchain.par('nc',rsf.doc.rsfpar('int','1','','''number of components '''))
sfpchain.par('verb',rsf.doc.rsfpar('bool','(bool) (1 == nt)','','''verbosity flag '''))
sfpchain.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfpchain.par('liter',rsf.doc.rsfpar('int','50','','''number of linear iterations '''))
sfpchain.par('rect',rsf.doc.rsfpar('int','1','','''smoothing in time '''))
sfpchain.version('2.1-git')
sfpchain.synopsis('''sfpchain < inp.rsf pef=pef.rsf > out.rsf nc=1 verb=(bool) (1 == nt) niter=0 liter=50 rect=1''','''''')
rsf.doc.progs['sfpchain']=sfpchain

sfpchain1 = rsf.doc.rsfprog('sfpchain1','user/fomels/Mpchain1.c','''Nonstationary Prony by chain of PEFs - linear operator ''')
sfpchain1.par('pef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpchain1.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpchain1.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfpchain1.version('2.1-git')
sfpchain1.synopsis('''sfpchain1 < inp.rsf pef=pef.rsf sig=sig.rsf > out.rsf adj=n''','''''')
rsf.doc.progs['sfpchain1']=sfpchain1

sfphaserot = rsf.doc.rsfprog('sfphaserot','user/fomels/Mphaserot.c','''Non-stationary phase rotation. ''')
sfphaserot.par('phase',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfphaserot.par('na',rsf.doc.rsfpar('int','721','','''number of angles '''))
sfphaserot.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfphaserot.par('a0',rsf.doc.rsfpar('float','-360.','','''first angle '''))
sfphaserot.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfphaserot.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfphaserot.version('2.1-git')
sfphaserot.synopsis('''sfphaserot < inp.rsf phase=pha.rsf > out.rsf na=721 da=1.0 a0=-360. order=100 ref=1.''','''''')
rsf.doc.progs['sfphaserot']=sfphaserot

sfpick = rsf.doc.rsfprog('sfpick','user/fomels/Mpick.c','''Automatic picking from semblance-like panels.''')
sfpick.par('vel0',rsf.doc.rsfpar('float','o2','','''surface velocity '''))
sfpick.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick.par('an',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick.par('gate',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick.par('norm',rsf.doc.rsfpar('bool','n','','''if apply normalization (0.~1.) '''))
sfpick.par('back',rsf.doc.rsfpar('bool','n','','''if run backward '''))
sfpick.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfpick.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfpick')
sfpick.version('2.1-git')
sfpick.synopsis('''sfpick < scn.rsf > pik.rsf vel0=o2 niter=100 an=1. gate=3 smooth=y norm=n back=n rect#=(1,1,...) rect1=1 rect2=1 ...''','''rectN defines the size of the smoothing stencil in N-th dimension.

Theory in Appendix B of:
S. Fomel, 2009,
Velocity analysis using AB semblance: Geophysical Prospecting, v. 57, 311-321.
Reproducible version in RSFSRC/book/tccs/avo
http://ahay.org/RSF/book/tccs/avo/paper_html/

August 2012 program of the month:
http://ahay.org/blog/2012/08/01/program-of-the-month-sfpick/
''')
rsf.doc.progs['sfpick']=sfpick

sfpick2 = rsf.doc.rsfprog('sfpick2','user/fomels/Mpick2.c','''Automatic picking from semblance-like panels (3-D input). ''')
sfpick2.par('slice',rsf.doc.rsfpar('int','0','','''if only one kind of slicing (1: inline, 2: time) '''))
sfpick2.par('vel0',rsf.doc.rsfpar('float','o2','','''surface velocity '''))
sfpick2.par('rect1',rsf.doc.rsfpar('int','1','','''smoothing radius on the first axis '''))
sfpick2.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing radius on the second axis '''))
sfpick2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick2.par('an',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick2.par('gate',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick2.version('2.1-git')
sfpick2.synopsis('''sfpick2 < scn.rsf > pik.rsf slice=0 vel0=o2 rect1=1 rect2=1 niter=100 an=1. gate=3''','''''')
rsf.doc.progs['sfpick2']=sfpick2

sfpick3 = rsf.doc.rsfprog('sfpick3','user/fomels/Mpick3.c','''Automatic picking  from 3-D semblance-like panels. ''')
sfpick3.par('vel1',rsf.doc.rsfpar('float','o2','',''''''))
sfpick3.par('vel2',rsf.doc.rsfpar('float','o3','','''surface velocity '''))
sfpick3.par('rect1',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sfpick3.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpick3.par('an1',rsf.doc.rsfpar('float','1.','',''''''))
sfpick3.par('an2',rsf.doc.rsfpar('float','1.','','''axes anisotropy '''))
sfpick3.par('gate1',rsf.doc.rsfpar('int','3','',''''''))
sfpick3.par('gate2',rsf.doc.rsfpar('int','3','','''picking gate '''))
sfpick3.par('smooth',rsf.doc.rsfpar('bool','y','','''if apply smoothing '''))
sfpick3.version('2.1-git')
sfpick3.synopsis('''sfpick3 < scn.rsf > pik.rsf vel1=o2 vel2=o3 rect1=1 niter=100 an1=1. an2=1. gate1=3 gate2=3 smooth=y''','''''')
rsf.doc.progs['sfpick3']=sfpick3

sfplane = rsf.doc.rsfprog('sfplane','user/fomels/Mplane.c','''Generating plane waves with steering filters. ''')
sfplane.par('p',rsf.doc.rsfpar('float','0.7','','''plane wave slope '''))
sfplane.par('a1',rsf.doc.rsfpar('int','2','','''filter length '''))
sfplane.par('b1',rsf.doc.rsfpar('int','1','','''denominator length '''))
sfplane.par('hyp',rsf.doc.rsfpar('bool','n','','''generate hyperbolas '''))
sfplane.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfplane.version('2.1-git')
sfplane.synopsis('''sfplane < inp.rsf > out.rsf p=0.7 a1=2 b1=1 hyp=n lag=''','''''')
rsf.doc.progs['sfplane']=sfplane

sfpoly = rsf.doc.rsfprog('sfpoly','user/fomels/Mpoly.c','''From roots to polynomials ''')
sfpoly.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpoly.par('n1',rsf.doc.rsfpar('int','','','''number of samples '''))
sfpoly.par('d1',rsf.doc.rsfpar('float','','','''sampling '''))
sfpoly.par('o1',rsf.doc.rsfpar('float','','','''origin '''))
sfpoly.par('coef',rsf.doc.rsfpar('string ',desc='''(optional) coefficients (auxiliary output file name)'''))
sfpoly.version('2.1-git')
sfpoly.synopsis('''sfpoly < inp.rsf > out.rsf coef=coef.rsf n1= d1= o1=''','''''')
rsf.doc.progs['sfpoly']=sfpoly

sfpolyfit = rsf.doc.rsfprog('sfpolyfit','user/fomels/Mpolyfit.c','''Fitting a polynomial by least-squares. ''')
sfpolyfit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpolyfit.par('coord',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpolyfit.par('reg',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpolyfit.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization parameter '''))
sfpolyfit.par('np',rsf.doc.rsfpar('int','1','','''polynomial order '''))
sfpolyfit.par('n1',rsf.doc.rsfpar('int','','','''number of samples for regularly sampled '''))
sfpolyfit.par('d1',rsf.doc.rsfpar('float','','','''sampling for regularly sampled '''))
sfpolyfit.par('o1',rsf.doc.rsfpar('float','','','''origin for regularly sampled '''))
sfpolyfit.par('coef',rsf.doc.rsfpar('string ',desc='''(optional) coefficients (auxiliary output file name)'''))
sfpolyfit.par('coord',rsf.doc.rsfpar('string ',desc='''coordinates (auxiliary input file name)'''))
sfpolyfit.par('reg',rsf.doc.rsfpar('string ',desc='''(optional) regularly sampled (auxiliary output file name)'''))
sfpolyfit.version('2.1-git')
sfpolyfit.synopsis('''sfpolyfit < inp.rsf > out.rsf coef=coef.rsf coord=coord.rsf reg=reg.rsf eps=0.0f np=1 n1= d1= o1=''','''''')
rsf.doc.progs['sfpolyfit']=sfpolyfit

sfregr = rsf.doc.rsfprog('sfregr','user/fomels/Mregr.c','''Linear regression ''')
sfregr.par('reg',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfregr.par('niter',rsf.doc.rsfpar('int','10','','''number of CG iterations '''))
sfregr.par('method',rsf.doc.rsfpar('int','2','','''method (L1-like or L2) '''))
sfregr.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfregr.par('n1iter',rsf.doc.rsfpar('int','10','','''number of POCS iterations '''))
sfregr.par('perc',rsf.doc.rsfpar('float','90.0','','''percentage for sharpening '''))
sfregr.version('2.1-git')
sfregr.synopsis('''sfregr < inp.rsf reg=reg.rsf > out.rsf niter=10 method=2 verb=n n1iter=10 perc=90.0''','''''')
rsf.doc.progs['sfregr']=sfregr

sfrdiv = rsf.doc.rsfprog('sfrdiv','user/fomels/Mrdiv.c','''Rough division. ''')
sfrdiv.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrdiv.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfrdiv.par('niter2',rsf.doc.rsfpar('int','1','','''number of outer iterations '''))
sfrdiv.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfrdiv.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfrdiv.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfrdiv.version('2.1-git')
sfrdiv.synopsis('''sfrdiv < fnum.rsf den=fden.rsf > frat.rsf niter=100 niter2=1 verb=y eps=0.01 perc=50.0''','''''')
rsf.doc.progs['sfrdiv']=sfrdiv

sfrect1 = rsf.doc.rsfprog('sfrect1','user/fomels/Mrect1.c','''1-D covariance estimator. ''')
sfrect1.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfrect1.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfrect1.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfrect1.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfrect1.version('2.1-git')
sfrect1.synopsis('''sfrect1 < inp.rsf > rct.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfrect1']=sfrect1

sfreshape = rsf.doc.rsfprog('sfreshape','user/fomels/Mreshape.c','''Non-stationary spectral balancing. ''')
sfreshape.par('in2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfreshape.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfreshape.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfreshape.par('out2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreshape.par('dim',rsf.doc.rsfpar('int','1','','''data dimensionality '''))
sfreshape.par('in2',rsf.doc.rsfpar('string ',desc='''optional second input file (auxiliary input file name)'''))
sfreshape.version('2.1-git')
sfreshape.synopsis('''sfreshape < in.rsf in2=in2.rsf ma=ma.rsf ma2=ma2.rsf > out.rsf out2=out2.rsf dim=1''','''''')
rsf.doc.progs['sfreshape']=sfreshape

sfriesz = rsf.doc.rsfprog('sfriesz','user/fomels/Mriesz.c','''Compute 2-D Riesz transform. ''')
sfriesz.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfriesz.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfriesz.version('2.1-git')
sfriesz.synopsis('''sfriesz < in.rsf > out.rsf order=10 ref=1.''','''''')
rsf.doc.progs['sfriesz']=sfriesz

sfrsin = rsf.doc.rsfprog('sfrsin','user/fomels/Mrsin.c','''Simple operations with real sinusoids ''')
sfrsin.par('root',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrsin.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfrsin.par('oper',rsf.doc.rsfpar('string ',desc='''operation to perform '''))
sfrsin.version('2.1-git')
sfrsin.synopsis('''sfrsin < in.rsf > out.rsf root=root.rsf adj=n oper=''','''''')
rsf.doc.progs['sfrsin']=sfrsin

sfsc = rsf.doc.rsfprog('sfsc','user/fomels/Msc.c','''Surface-consistent decomposition ''')
sfsc.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsc.par('error',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsc.par('index',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsc.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfsc.par('prec',rsf.doc.rsfpar('bool','y','','''if apply preconditioning '''))
sfsc.par('pred',rsf.doc.rsfpar('string ',desc='''prediction (auxiliary output file name)'''))
sfsc.par('error',rsf.doc.rsfpar('string ',desc='''prediction (auxiliary output file name)'''))
sfsc.version('2.1-git')
sfsc.synopsis('''sfsc < inp.rsf pred=pred.rsf error=error.rsf index=index.rsf > out.rsf niter=0 prec=y''','''''')
rsf.doc.progs['sfsc']=sfsc

sfseislet1 = rsf.doc.rsfprog('sfseislet1','user/fomels/Mseislet1.c','''1-D seislet transform ''')
sfseislet1.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseislet1.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfseislet1.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfseislet1.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfseislet1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseislet1.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseislet1.version('2.1-git')
sfseislet1.synopsis('''sfseislet1 < in.rsf > out.rsf freq=dip.rsf inv=n adj=n unit=n verb=n type=''','''''')
rsf.doc.progs['sfseislet1']=sfseislet1

sfsemblance = rsf.doc.rsfprog('sfsemblance','user/fomels/Msemblance.c','''Semblance over the specified axis. ''')
sfsemblance.par('weighted',rsf.doc.rsfpar('bool','n','','''if use weighted semblance '''))
sfsemblance.par('axis',rsf.doc.rsfpar('int','2','','''which axis to stack '''))
sfsemblance.version('2.1-git')
sfsemblance.synopsis('''sfsemblance < in.rsf > out.rsf weighted=n axis=2''','''''')
rsf.doc.progs['sfsemblance']=sfsemblance

sfsemblancew = rsf.doc.rsfprog('sfsemblancew','user/fomels/Msemblancew.c','''Semblance over the specified axis. ''')
sfsemblancew.par('weighted',rsf.doc.rsfpar('bool','n','','''if use weighted semblance '''))
sfsemblancew.par('axis',rsf.doc.rsfpar('int','2','','''which axis to stack '''))
sfsemblancew.par('nb',rsf.doc.rsfpar('int','2','','''smoothing along the first axis '''))
sfsemblancew.version('2.1-git')
sfsemblancew.synopsis('''sfsemblancew < in.rsf > out.rsf weighted=n axis=2 nb=2''','''''')
rsf.doc.progs['sfsemblancew']=sfsemblancew

sfshape = rsf.doc.rsfprog('sfshape','user/fomels/Mshape.c','''Non-stationary smoothing by shaping regularization. ''')
sfshape.par('limit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshape.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshape.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfshape.version('2.1-git')
sfshape.synopsis('''sfshape < inp.rsf > out.rsf limit=lim.rsf niter=100 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfshape']=sfshape

sfshapeagc = rsf.doc.rsfprog('sfshapeagc','user/fomels/Mshapeagc.c','''Automatic gain control by shaping regularization. ''')
sfshapeagc.par('gain',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshapeagc.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshapeagc.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfshapeagc.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfshapeagc.par('rect#',rsf.doc.rsfpar('int','(125,1,1,...)','','''smoothing radius on #-th axis '''))
sfshapeagc.par('gain',rsf.doc.rsfpar('string ',desc='''output gain file (optional) (auxiliary output file name)'''))
sfshapeagc.version('2.1-git')
sfshapeagc.synopsis('''sfshapeagc < in.rsf > out.rsf gain=fgain.rsf niter=100 eps=0.0f verb=n rect#=(125,1,1,...)''','''''')
rsf.doc.progs['sfshapeagc']=sfshapeagc

sfshapefill = rsf.doc.rsfprog('sfshapefill','user/fomels/Mshapefill.c','''Missing data interpolation in 2-D by Laplacian regularization. ''')
sfshapefill.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshapefill.par('niter',rsf.doc.rsfpar('int','200','','''number of iterations '''))
sfshapefill.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfshapefill.par('dim',rsf.doc.rsfpar('int','dim','','''dimensionality '''))
sfshapefill.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfshapefill.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file with zeroes for missing data locations (auxiliary input file name)'''))
sfshapefill.version('2.1-git')
sfshapefill.synopsis('''sfshapefill < in.rsf > out.rsf mask=mask.rsf niter=200 verb=n dim=dim rect#=(1,1,...)''','''''')
rsf.doc.progs['sfshapefill']=sfshapefill

sfshearer = rsf.doc.rsfprog('sfshearer','user/fomels/Mshearer.c','''Preconditioning for traveltime picking. ''')
sfshearer.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshearer.par('order',rsf.doc.rsfpar('int','10','','''Hilbert transformer order '''))
sfshearer.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfshearer.par('short',rsf.doc.rsfpar('int','1','','''short smoothing radius '''))
sfshearer.par('long',rsf.doc.rsfpar('int','10','','''long smoothing radius '''))
sfshearer.version('2.1-git Menvelope.c 696 2004-07-06 23:17:31Z fomels')
sfshearer.synopsis('''sfshearer < in.rsf > out.rsf niter=100 order=10 ref=1. short=1 long=10 rect1=1 rect2=1 ... ''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfshearer']=sfshearer

sfshift1 = rsf.doc.rsfprog('sfshift1','user/fomels/Mshift1.c','''Generate shifts for 1-D regularized autoregression. ''')
sfshift1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshift1.version('2.1-git')
sfshift1.synopsis('''sfshift1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshift1']=sfshift1

sfsimilarity = rsf.doc.rsfprog('sfsimilarity','user/fomels/Msimilarity.c','''Local similarity measure between two datasets. ''')
sfsimilarity.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimilarity.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimilarity.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimilarity.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfsimilarity.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsimilarity.version('2.1-git')
sfsimilarity.synopsis('''sfsimilarity < in.rsf > out.rsf other=other.rsf verb=y niter=20 eps=0.0f rect#=(1,1,...)''','''
September 2015 program of the month:
http://ahay.org/blog/2015/09/14/program-of-the-month-sfsimilarity/
''')
rsf.doc.progs['sfsimilarity']=sfsimilarity

sfsimilarity2 = rsf.doc.rsfprog('sfsimilarity2','user/fomels/Msimilarity2.c','''Local similarity measure between two datasets (alternative form). ''')
sfsimilarity2.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimilarity2.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimilarity2.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimilarity2.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsimilarity2.version('2.1-git')
sfsimilarity2.synopsis('''sfsimilarity2 < in.rsf > out.rsf other=other.rsf verb=y niter=20 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfsimilarity2']=sfsimilarity2

sfsimenv = rsf.doc.rsfprog('sfsimenv','user/fomels/Msimenv.c','''Rotate phase and compute similarity with enevelope. ''')
sfsimenv.par('na',rsf.doc.rsfpar('int','360','','''number of angles '''))
sfsimenv.par('da',rsf.doc.rsfpar('float','1.0','','''angle increment '''))
sfsimenv.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle '''))
sfsimenv.par('order',rsf.doc.rsfpar('int','100','','''Hilbert transformer order '''))
sfsimenv.par('ref',rsf.doc.rsfpar('float','1.','','''Hilbert transformer reference (0.5 < ref <= 1) '''))
sfsimenv.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimenv.par('inv',rsf.doc.rsfpar('bool','y','','''inverse similarity '''))
sfsimenv.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimenv.par('rect',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfsimenv.version('2.1-git')
sfsimenv.synopsis('''sfsimenv < inp.rsf > sim.rsf na=360 da=1.0 a0=-180. order=100 ref=1. verb=y inv=y niter=20 rect=3''','''''')
rsf.doc.progs['sfsimenv']=sfsimenv

sfsmoothderw = rsf.doc.rsfprog('sfsmoothderw','user/fomels/Msmoothderw.c','''Convert input to its derivative using LS and shaping regularization''')
sfsmoothderw.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsmoothderw.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfsmoothderw.par('rect#',rsf.doc.rsfpar('string','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsmoothderw.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsmoothderw.version('2.1-git')
sfsmoothderw.synopsis('''sfsmoothderw < data.rsf > modl.rsf weight=weight.rsf niter=100 rect#=(1,1,...)''','''* applied to causint_lop ''')
rsf.doc.progs['sfsmoothderw']=sfsmoothderw

sfsmoothreg = rsf.doc.rsfprog('sfsmoothreg','user/fomels/Msmoothreg.c','''Smoothing in 1-D by simple regularization.''')
sfsmoothreg.par('eps',rsf.doc.rsfpar('float','1.','','''smoothness parameter '''))
sfsmoothreg.par('repeat',rsf.doc.rsfpar('int','1','','''repeat smoothing '''))
sfsmoothreg.version('2.1-git')
sfsmoothreg.synopsis('''sfsmoothreg < in.rsf > smooth.rsf eps=1. repeat=1''','''''')
rsf.doc.progs['sfsmoothreg']=sfsmoothreg

sfsmspray = rsf.doc.rsfprog('sfsmspray','user/fomels/Msmspray.c','''Smoothing by spraying ''')
sfsmspray.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfsmspray.par('ns',rsf.doc.rsfpar('int','0','','''smoothing radius '''))
sfsmspray.par('type',rsf.doc.rsfpar('string ',desc='''weight type (triangle, gauss) '''))
sfsmspray.version('2.1-git')
sfsmspray.synopsis('''sfsmspray < inp.rsf > out.rsf adj=n ns=0 type=''','''''')
rsf.doc.progs['sfsmspray']=sfsmspray

sfstfchain = rsf.doc.rsfprog('sfstfchain','user/fomels/Mstfchain.c','''Find a symmetric chain of Fourier weighting and scaling ''')
sfstfchain.par('target',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstfchain.par('fweight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstfchain.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstfchain.par('rect',rsf.doc.rsfpar('int','1','','''smoothing in time '''))
sfstfchain.par('frect',rsf.doc.rsfpar('int','1','','''smoothing in frequency '''))
sfstfchain.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfstfchain.par('liter',rsf.doc.rsfpar('int','50','','''number of linear iterations '''))
sfstfchain.version('2.1-git')
sfstfchain.synopsis('''sfstfchain < src.rsf > wht.rsf target=tgt.rsf fweight=fwht.rsf match=mch.rsf rect=1 frect=1 niter=0 liter=50''','''''')
rsf.doc.progs['sfstfchain']=sfstfchain

sfstfchain2 = rsf.doc.rsfprog('sfstfchain2','user/fomels/Mstfchain2.c','''Find a symmetric chain of Fourier weighting and scaling ''')
sfstfchain2.par('target',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstfchain2.par('fweight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstfchain2.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstfchain2.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sfstfchain2.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing in time '''))
sfstfchain2.par('frect1',rsf.doc.rsfpar('int','1','',''''''))
sfstfchain2.par('frect2',rsf.doc.rsfpar('int','1','','''smoothing in frequency '''))
sfstfchain2.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sfstfchain2.par('liter',rsf.doc.rsfpar('int','50','','''number of linear iterations '''))
sfstfchain2.version('2.1-git')
sfstfchain2.synopsis('''sfstfchain2 < src.rsf > wht.rsf target=tgt.rsf fweight=fwht.rsf match=mch.rsf rect1=1 rect2=1 frect1=1 frect2=1 niter=0 liter=50''','''''')
rsf.doc.progs['sfstfchain2']=sfstfchain2

sfstream = rsf.doc.rsfprog('sfstream','user/fomels/Mstream.c','''Streaming PEF ''')
sfstream.par('pattern',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstream.par('pef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstream.par('known',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstream.par('inv',rsf.doc.rsfpar('bool','n','','''inversion flag '''))
sfstream.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag (for linear operator) '''))
sfstream.par('na',rsf.doc.rsfpar('int','','','''PEF filter size (not including leading one) '''))
sfstream.par('eps',rsf.doc.rsfpar('float','','','''regularization '''))
sfstream.par('pattern',rsf.doc.rsfpar('string ',desc='''pattern data (for linear operator) (auxiliary input file name)'''))
sfstream.par('pef',rsf.doc.rsfpar('string ',desc='''output PEF (optional) (auxiliary output file name)'''))
sfstream.par('known',rsf.doc.rsfpar('string ',desc='''known data locations (optional) (auxiliary input file name)'''))
sfstream.version('2.1-git')
sfstream.synopsis('''sfstream < inp.rsf > out.rsf pattern=pat.rsf pef=pef.rsf known=known.rsf inv=n adj=n na= eps=''','''''')
rsf.doc.progs['sfstream']=sfstream

sfstreamiss = rsf.doc.rsfprog('sfstreamiss','user/fomels/Mstreamiss.c','''Missing data interpolation using streaming PEF ''')
sfstreamiss.par('pef',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfstreamiss.par('known',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstreamiss.par('na',rsf.doc.rsfpar('int','','','''PEF filter size (not including leading one) '''))
sfstreamiss.par('eps',rsf.doc.rsfpar('float','','','''regularization '''))
sfstreamiss.par('pef',rsf.doc.rsfpar('string ',desc='''output PEF (optional) (auxiliary output file name)'''))
sfstreamiss.version('2.1-git')
sfstreamiss.synopsis('''sfstreamiss < inp.rsf > out.rsf pef=pef.rsf known=known.rsf na= eps=''','''''')
rsf.doc.progs['sfstreamiss']=sfstreamiss

sftaupfit = rsf.doc.rsfprog('sftaupfit','user/fomels/Mtaupfit.c','''Fitting tau-p approximations ''')
sftaupfit.par('coef',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftaupfit.par('fit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftaupfit.par('type',rsf.doc.rsfpar('string ',desc='''Type of approximation (iso,vti) '''))
sftaupfit.version('2.1-git')
sftaupfit.synopsis('''sftaupfit < in.rsf coef=coef.rsf > out.rsf fit=fit.rsf type=''','''''')
rsf.doc.progs['sftaupfit']=sftaupfit

sftfchain = rsf.doc.rsfprog('sftfchain','user/fomels/Mtfchain.c','''Find a chain of Fourier weighting and scaling ''')
sftfchain.par('target',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftfchain.par('fweight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftfchain.par('match',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftfchain.par('rect',rsf.doc.rsfpar('int','1','','''smoothing in time '''))
sftfchain.par('frect',rsf.doc.rsfpar('int','1','','''smoothing in frequency '''))
sftfchain.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations '''))
sftfchain.par('liter',rsf.doc.rsfpar('int','50','','''number of linear iterations '''))
sftfchain.version('2.1-git')
sftfchain.synopsis('''sftfchain < src.rsf > wht.rsf target=tgt.rsf fweight=fwht.rsf match=mch.rsf rect=1 frect=1 niter=0 liter=50''','''''')
rsf.doc.progs['sftfchain']=sftfchain

sfthin = rsf.doc.rsfprog('sfthin','user/fomels/Mthin.c','''Sparse deconvolution. ''')
sfthin.par('wave',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthin.par('conv',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfthin.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfthin.par('eps',rsf.doc.rsfpar('float','0.0001','','''regularization for Wiener deconvolution '''))
sfthin.par('pclip',rsf.doc.rsfpar('float','4','','''percentage to threshold '''))
sfthin.par('conv',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfthin.version('2.1-git')
sfthin.synopsis('''sfthin < seis.rsf > refl.rsf wave=wave.rsf conv=conv.rsf niter=100 eps=0.0001 pclip=4''','''''')
rsf.doc.progs['sfthin']=sfthin

sftimecont = rsf.doc.rsfprog('sftimecont','user/fomels/Mtimecont.c','''Forward or reverse time continuation using fast marching. ''')
sftimecont.par('surf',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftimecont.par('forwd',rsf.doc.rsfpar('bool','n','','''continue forward or backward '''))
sftimecont.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sftimecont.par('order',rsf.doc.rsfpar('int','2','[1,2]','''Accuracy order '''))
sftimecont.version('2.1-git')
sftimecont.synopsis('''sftimecont < vel.rsf > time.rsf surf=time0.rsf forwd=n vel=y order=2''','''''')
rsf.doc.progs['sftimecont']=sftimecont

sftimefreq = rsf.doc.rsfprog('sftimefreq','user/fomels/Mtimefreq.c','''Time-frequency analysis using local attributes. ''')
sftimefreq.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftimefreq.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sftimefreq.par('dw',rsf.doc.rsfpar('float','','','''f	requency step '''))
sftimefreq.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sftimefreq.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius '''))
sftimefreq.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sftimefreq.par('phase',rsf.doc.rsfpar('bool','n','','''output phase instead of amplitude '''))
sftimefreq.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftimefreq.version('2.1-git')
sftimefreq.synopsis('''sftimefreq < time.rsf > timefreq.rsf mask=mask.rsf nw= dw= w0=0. rect=10 niter=100 phase=n''','''''')
rsf.doc.progs['sftimefreq']=sftimefreq

sftomo = rsf.doc.rsfprog('sftomo','user/fomels/Mtomo.c','''Simple tomography test. ''')
sftomo.par('adj',rsf.doc.rsfpar('bool','n','','''if n, generate traveltime from slowness; 
       if y, invert slowness from traveltime '''))
sftomo.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sftomo.par('eps',rsf.doc.rsfpar('float','1.','','''scaling parameter '''))
sftomo.par('tol',rsf.doc.rsfpar('float','1.e-7','','''tolerance for stopping iterations '''))
sftomo.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sftomo.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing length in z and x '''))
sftomo.par('np',rsf.doc.rsfpar('int','11','',''''''))
sftomo.par('ns',rsf.doc.rsfpar('int','1','','''number of depth steps '''))
sftomo.par('ds',rsf.doc.rsfpar('int','nz','','''step size '''))
sftomo.version('2.1-git')
sftomo.synopsis('''sftomo < time.rsf > slow.rsf adj=n niter=100 eps=1. tol=1.e-7 rect1=1 rect2=1 np=11 ns=1 ds=nz''','''''')
rsf.doc.progs['sftomo']=sftomo

sftree = rsf.doc.rsfprog('sftree','user/fomels/Mtree.c','''Multiple arrivals with a fast algorithm. ''')
sftree.par('na',rsf.doc.rsfpar('int','361','','''number of angles '''))
sftree.par('da',rsf.doc.rsfpar('float','1.','','''angle increment (in degrees) '''))
sftree.par('a0',rsf.doc.rsfpar('float','-180.','','''first angle (in degrees) '''))
sftree.par('vel',rsf.doc.rsfpar('bool','y','','''y: theinput is velocity; n: slowness '''))
sftree.par('order',rsf.doc.rsfpar('int','3','','''accuracy order '''))
sftree.par('debug',rsf.doc.rsfpar('bool','n','','''debugging flag '''))
sftree.version('2.1-git Mtree.c 1575 2005-11-21 14:09:06Z fomels')
sftree.synopsis('''sftree < vel.rsf > out.rsf na=361 da=1. a0=-180. vel=y order=3 debug=n''','''''')
rsf.doc.progs['sftree']=sftree

sftrace2 = rsf.doc.rsfprog('sftrace2','user/fomels/Mtrace2.c','''2-D multiple arrivals by cell ray tracing. ''')
sftrace2.par('size',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftrace2.par('grid',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sftrace2.par('na',rsf.doc.rsfpar('int','60','','''number of angles '''))
sftrace2.par('da',rsf.doc.rsfpar('float','3.1','','''angle increment (in degrees) '''))
sftrace2.par('a0',rsf.doc.rsfpar('float','-90.','','''initial angle (in degrees) '''))
sftrace2.par('maxsplit',rsf.doc.rsfpar('int','10','','''maximum splitting for adaptive grid '''))
sftrace2.par('minx',rsf.doc.rsfpar('float','0.5*dx','','''parameters for adaptive grid '''))
sftrace2.par('maxx',rsf.doc.rsfpar('float','2.*dx','',''''''))
sftrace2.par('mina',rsf.doc.rsfpar('float','0.5*da','',''''''))
sftrace2.par('maxa',rsf.doc.rsfpar('float','2.*da','',''''''))
sftrace2.par('vel',rsf.doc.rsfpar('bool','y','','''y: velocity, n: slowness '''))
sftrace2.par('order',rsf.doc.rsfpar('int','3','','''velocity interpolation order '''))
sftrace2.par('lsint',rsf.doc.rsfpar('bool','n','','''if use least-squares interpolation '''))
sftrace2.version('2.1-git Mtrace2.c 853 2004-11-05 12:54:22Z fomels')
sftrace2.synopsis('''sftrace2 < vel.rsf > outp.rsf size=size.rsf grid=grid.rsf na=60 da=3.1 a0=-90. maxsplit=10 minx=0.5*dx maxx=2.*dx mina=0.5*da maxa=2.*da vel=y order=3 lsint=n''','''''')
rsf.doc.progs['sftrace2']=sftrace2

sftricascade = rsf.doc.rsfprog('sftricascade','user/fomels/Mtricascade.c','''Triangle filter cascade ''')
sftricascade.par('rect',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sftricascade.par('inter',rsf.doc.rsfpar('int','n','','''interrupt '''))
sftricascade.version('2.1-git')
sftricascade.synopsis('''sftricascade < inp.rsf > out.rsf rect=1 inter=n''','''''')
rsf.doc.progs['sftricascade']=sftricascade

sftristack = rsf.doc.rsfprog('sftristack','user/fomels/Mtristack.c','''Resampling with triangle weights. ''')
sftristack.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag '''))
sftristack.par('rect',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sftristack.par('gauss',rsf.doc.rsfpar('bool','n','','''use pseudo-gaussian '''))
sftristack.version('2.1-git')
sftristack.synopsis('''sftristack < in.rsf > out.rsf adj=y rect=1 gauss=n''','''''')
rsf.doc.progs['sftristack']=sftristack

sftristack2 = rsf.doc.rsfprog('sftristack2','user/fomels/Mtristack2.c','''2-D resampling with triangle weights. ''')
sftristack2.par('adj',rsf.doc.rsfpar('bool','y','','''adjoint flag '''))
sftristack2.par('rect1',rsf.doc.rsfpar('int','1','',''''''))
sftristack2.par('rect2',rsf.doc.rsfpar('int','1','','''smoothing radius '''))
sftristack2.par('gauss',rsf.doc.rsfpar('bool','n','','''use pseudo-gaussian '''))
sftristack2.version('2.1-git')
sftristack2.synopsis('''sftristack2 < in.rsf > out.rsf adj=y rect1=1 rect2=1 gauss=n''','''''')
rsf.doc.progs['sftristack2']=sftristack2

sftwofreq2 = rsf.doc.rsfprog('sftwofreq2','user/fomels/Mtwofreq2.c','''2-D two spectral component estimation.''')
sftwofreq2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftwofreq2.par('niter',rsf.doc.rsfpar('int','5','','''number of iterations '''))
sftwofreq2.par('eps',rsf.doc.rsfpar('float','1','','''vertical smoothness '''))
sftwofreq2.par('lam',rsf.doc.rsfpar('float','1','','''horizontal smoothness '''))
sftwofreq2.par('p0',rsf.doc.rsfpar('float','1.','','''initial first component '''))
sftwofreq2.par('q0',rsf.doc.rsfpar('float','1.','','''initial first component '''))
sftwofreq2.par('p1',rsf.doc.rsfpar('float','-1.','','''initial second component '''))
sftwofreq2.par('q1',rsf.doc.rsfpar('float','1.','','''initial second component '''))
sftwofreq2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sftwofreq2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftwofreq2.version('2.1-git Mtwofreq2.c 704 2004-07-13 18:22:06Z fomels')
sftwofreq2.synopsis('''sftwofreq2 < in.rsf > out.rsf mask=mask.rsf niter=5 eps=1 lam=1 p0=1. q0=1. p1=-1. q1=1. verb=n < data.rsf > dip.rsf''','''''')
rsf.doc.progs['sftwofreq2']=sftwofreq2

sfupgrad = rsf.doc.rsfprog('sfupgrad','user/fomels/Mupgrad.c','''Causal gradient operator ''')
sfupgrad.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfupgrad.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfupgrad.par('grad',rsf.doc.rsfpar('bool','y','','''if y, gradient; if n, Laplacian '''))
sfupgrad.par('dim',rsf.doc.rsfpar('int','','',''''''))
sfupgrad.version('2.1-git')
sfupgrad.synopsis('''sfupgrad < inp.rsf ref=ref.rsf > out.rsf adj=n grad=y dim=''','''''')
rsf.doc.progs['sfupgrad']=sfupgrad

sfvar2 = rsf.doc.rsfprog('sfvar2','user/fomels/Mvar2.c','''Variogram from irregular 2-D data. ''')
sfvar2.par('nx',rsf.doc.rsfpar('int','','','''number of distance bins '''))
sfvar2.par('dx',rsf.doc.rsfpar('float','','','''distance sampling '''))
sfvar2.version('2.1-git')
sfvar2.synopsis('''sfvar2 < in.rsf > out.rsf nx= dx=''','''''')
rsf.doc.progs['sfvar2']=sfvar2

sfvelcon = rsf.doc.rsfprog('sfvelcon','user/fomels/Mvelcon.c','''Post-stack velocity continuation by implicit finite differences ''')
sfvelcon.par('vel',rsf.doc.rsfpar('float','0.75','','''final velocity '''))
sfvelcon.par('v0',rsf.doc.rsfpar('float','0.','','''starting velocity '''))
sfvelcon.par('nv',rsf.doc.rsfpar('int','n1','','''number of steps '''))
sfvelcon.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfvelcon.par('add',rsf.doc.rsfpar('bool','n','','''addition flag '''))
sfvelcon.par('inv',rsf.doc.rsfpar('int','0','','''amplitude type '''))
sfvelcon.version('2.1-git')
sfvelcon.synopsis('''sfvelcon < in.rsf > out.rsf vel=0.75 v0=0. nv=n1 adj=n add=n inv=0''','''''')
rsf.doc.progs['sfvelcon']=sfvelcon

sfvelinv = rsf.doc.rsfprog('sfvelinv','user/fomels/Mvelinv.c','''Velocity transform for generating velocity spectra and its corresponding hyperbolic modeling. ''')
sfvelinv.par('adj',rsf.doc.rsfpar('bool','n','','''adj = 0: from velocity-domain(t,s) to cmp-gather(t,x)
       adj = 1: from cmp-gather(t,x) to velocity-domain(t,s) '''))
sfvelinv.par('niter',rsf.doc.rsfpar('int','0','','''number of iterations (invoked if adj=y) '''))
sfvelinv.par('ns',rsf.doc.rsfpar('int','nx','','''number of slowness values '''))
sfvelinv.par('ds',rsf.doc.rsfpar('float','0.001','','''slowness sampling '''))
sfvelinv.par('os',rsf.doc.rsfpar('float','0.00000001','','''slowness origin '''))
sfvelinv.par('nx',rsf.doc.rsfpar('int','ns','','''number of offset values '''))
sfvelinv.par('dx',rsf.doc.rsfpar('float','10.','','''offset sampling '''))
sfvelinv.par('ox',rsf.doc.rsfpar('float','0.','','''offset origin '''))
sfvelinv.par('robust',rsf.doc.rsfpar('bool','n','','''robust inversion '''))
sfvelinv.par('perc',rsf.doc.rsfpar('float','90.','','''threshold percentage for robust inversion '''))
sfvelinv.par('nliter',rsf.doc.rsfpar('int','10','','''number of POCS iterations for robust inversion '''))
sfvelinv.par('eps',rsf.doc.rsfpar('float','1.','','''regularization parameter for robust inversion '''))
sfvelinv.version('2.1-git')
sfvelinv.synopsis('''sfvelinv < cmp.rsf > vtr.rsf adj=n niter=0 ns=nx ds=0.001 os=0.00000001 nx=ns dx=10. ox=0. robust=n perc=90. nliter=10 eps=1.''','''''')
rsf.doc.progs['sfvelinv']=sfvelinv

sfvidattr = rsf.doc.rsfprog('sfvidattr','user/fomels/Mvidattr.c','''Slope-based velocity-independent data attributes. ''')
sfvidattr.par('hdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvidattr.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfvidattr.par('what',rsf.doc.rsfpar('string ',desc='''what attribute to compute '''))
sfvidattr.version('2.1-git')
sfvidattr.synopsis('''sfvidattr < xdip.rsf hdip=hdip.rsf > out.rsf half=y what=''','''
The axis order is time-midpoint-offset.
''')
rsf.doc.progs['sfvidattr']=sfvidattr

sfvipmig0 = rsf.doc.rsfprog('sfvipmig0','user/fomels/Mvipmig0.c','''Velocity-independent phase-space zero-offset migration. ''')
sfvipmig0.par('vmin',rsf.doc.rsfpar('float','','',''''''))
sfvipmig0.par('vmax',rsf.doc.rsfpar('float','','','''convert to slowness '''))
sfvipmig0.version('2.1-git')
sfvipmig0.synopsis('''sfvipmig0 < inp.rsf > mig.rsf vmin= vmax=''','''''')
rsf.doc.progs['sfvipmig0']=sfvipmig0

sfvofzperm = rsf.doc.rsfprog('sfvofzperm','user/fomels/Mvofzperm.c','''V(z) prestack exploditing reflector. ''')
sfvofzperm.par('size',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvofzperm.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvofzperm.par('middle',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvofzperm.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfvofzperm.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfvofzperm.par('nz',rsf.doc.rsfpar('int','','','''time samples (if migration) '''))
sfvofzperm.par('dz',rsf.doc.rsfpar('float','','','''time sampling (if migration) '''))
sfvofzperm.par('nt',rsf.doc.rsfpar('int','','','''time samples (if modeling) '''))
sfvofzperm.par('dt',rsf.doc.rsfpar('float','','','''time sampling (if modeling) '''))
sfvofzperm.par('nh',rsf.doc.rsfpar('int','','','''offset samples (if modeling) '''))
sfvofzperm.par('dh',rsf.doc.rsfpar('float','','','''offset sampling (if modeling) '''))
sfvofzperm.version('2.1-git')
sfvofzperm.synopsis('''sfvofzperm < data.rsf > image.rsf size=size.rsf left=left.rsf middle=middle.rsf right=right.rsf mig=n nz= dz= nt= dt= nh= dh=''','''''')
rsf.doc.progs['sfvofzperm']=sfvofzperm

sfwarp1 = rsf.doc.rsfprog('sfwarp1','user/fomels/Mwarp1.c','''Multicomponent data registration by 1-D warping. ''')
sfwarp1.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarp1.par('warpout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwarp1.par('amplout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwarp1.par('warpin',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarp1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwarp1.par('noamp',rsf.doc.rsfpar('bool','n','','''if y, don't correct amplitudes '''))
sfwarp1.par('accuracy',rsf.doc.rsfpar('int','','[1-4]','''interpolation accuracy '''))
sfwarp1.par('nliter',rsf.doc.rsfpar('int','10','','''number of non-linear iterations '''))
sfwarp1.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of linear iterations '''))
sfwarp1.par('warpin',rsf.doc.rsfpar('string ',desc='''optional initial warp file (auxiliary input file name)'''))
sfwarp1.version('2.1-git')
sfwarp1.synopsis('''sfwarp1 < in.rsf > warped.rsf other=other.rsf warpout=warpout.rsf amplout=amplout.rsf warpin=warpin.rsf verb=n noamp=n accuracy= nliter=10 niter=100''','''''')
rsf.doc.progs['sfwarp1']=sfwarp1

sfwarpadd = rsf.doc.rsfprog('sfwarpadd','user/fomels/Mwarpadd.c','''Add a perturbation to the warping function. ''')
sfwarpadd.par('add',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpadd.par('accuracy',rsf.doc.rsfpar('int','','','''Interpolation accuracy order '''))
sfwarpadd.par('m1',rsf.doc.rsfpar('int','n1*2','','''Trace pading '''))
sfwarpadd.version('2.1-git')
sfwarpadd.synopsis('''sfwarpadd < in.rsf add=add.rsf > sum.rsf accuracy= m1=n1*2''','''''')
rsf.doc.progs['sfwarpadd']=sfwarpadd

sfwarpscan = rsf.doc.rsfprog('sfwarpscan','user/fomels/Mwarpscan.c','''Multicomponent data registration analysis. ''')
sfwarpscan.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwarpscan.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfwarpscan.par('cheb',rsf.doc.rsfpar('bool','n','','''use Chebyshev scan '''))
sfwarpscan.par('sign',rsf.doc.rsfpar('bool','n','','''use signed similarity '''))
sfwarpscan.par('ng',rsf.doc.rsfpar('int','1','','''number of gamma values '''))
sfwarpscan.par('g0',rsf.doc.rsfpar('float','','','''gamma origin '''))
sfwarpscan.par('dg',rsf.doc.rsfpar('float','g0','','''gamma sampling '''))
sfwarpscan.par('rect1',rsf.doc.rsfpar('int','1','','''vertical smoothing '''))
sfwarpscan.par('rect2',rsf.doc.rsfpar('int','1','','''gamma smoothing '''))
sfwarpscan.par('rect3',rsf.doc.rsfpar('int','1','','''in-line smoothing '''))
sfwarpscan.par('rect4',rsf.doc.rsfpar('int','1','','''cross-line smoothing '''))
sfwarpscan.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfwarpscan.par('shift',rsf.doc.rsfpar('bool','n','','''use shift instead of stretch '''))
sfwarpscan.par('accuracy',rsf.doc.rsfpar('int','','[1-4]','''interpolation accuracy '''))
sfwarpscan.version('2.1-git Mwarpscan.c 744 2004-08-17 18:46:07Z fomels')
sfwarpscan.synopsis('''sfwarpscan < in.rsf > warped.rsf other=other.rsf verb=y cheb=n sign=n ng=1 g0= dg=g0 rect1=1 rect2=1 rect3=1 rect4=1 niter=10 shift=n accuracy=''','''''')
rsf.doc.progs['sfwarpscan']=sfwarpscan

sfzero = rsf.doc.rsfprog('sfzero','user/fomels/Mzero.c','''Zero crossings with sub-pixel resolution. ''')
sfzero.par('nzero',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfzero.par('nw',rsf.doc.rsfpar('int','4','','''Interpolation accuracy '''))
sfzero.par('down',rsf.doc.rsfpar('bool','n','','''only zeros on the way down '''))
sfzero.version('2.1-git')
sfzero.synopsis('''sfzero < inp.rsf > out.rsf nzero=nzero.rsf nw=4 down=n''','''''')
rsf.doc.progs['sfzero']=sfzero

sfzmarch = rsf.doc.rsfprog('sfzmarch','user/fomels/Mzmarch.c','''Phase-space traveltime (marching in z) ''')
sfzmarch.par('na',rsf.doc.rsfpar('int','','','''angle samples '''))
sfzmarch.par('da',rsf.doc.rsfpar('float','','','''angle sampling '''))
sfzmarch.par('a0',rsf.doc.rsfpar('float','','','''starting velocity '''))
sfzmarch.par('order',rsf.doc.rsfpar('int','3','','''interpolation order '''))
sfzmarch.par('scheme',rsf.doc.rsfpar('int','2','','''finite-difference order '''))
sfzmarch.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfzmarch.par('what',rsf.doc.rsfpar('string ',desc='''what to compute (t,x,z,a) '''))
sfzmarch.version('2.1-git')
sfzmarch.synopsis('''sfzmarch < vel.rsf > out.rsf na= da= a0= order=3 scheme=2 verb=n what=''','''''')
rsf.doc.progs['sfzmarch']=sfzmarch

sfztrace = rsf.doc.rsfprog('sfztrace','user/fomels/Mztrace.c','''Multiple arrivals by depth marching. ''')
sfztrace.par('nt',rsf.doc.rsfpar('int','nx*nz','','''ray length bound '''))
sfztrace.par('na',rsf.doc.rsfpar('int','362','','''number of angles '''))
sfztrace.par('da',rsf.doc.rsfpar('float','0.5','','''angle increment (in degrees) '''))
sfztrace.par('a0',rsf.doc.rsfpar('float','-90.','','''starting angle (in degrees) '''))
sfztrace.par('vel',rsf.doc.rsfpar('bool','y','','''y, input is velocity; n, slowness '''))
sfztrace.par('order',rsf.doc.rsfpar('int','3','','''interpolation accuracy for velocity '''))
sfztrace.par('iorder',rsf.doc.rsfpar('int','4','','''interpolation accuracy for grid '''))
sfztrace.version('2.1-git')
sfztrace.synopsis('''sfztrace < in.rsf nt=nx*nz na=362 da=0.5 a0=-90. vel=y order=3 iorder=4''','''''')
rsf.doc.progs['sfztrace']=sfztrace

sfanisolr2 = rsf.doc.rsfprog('sfanisolr2','user/fomels/Manisolr2.cc','''Lowrank decomposition for 2-D anisotropic wave propagation (Real number).''')
sfanisolr2.par('vels',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('xtap',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('ktap',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfanisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfanisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfanisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfanisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfanisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfanisolr2.par('fftexp0',rsf.doc.rsfpar('','0','','''model/mig with sffftexp0'''))
sfanisolr2.par('approx',rsf.doc.rsfpar('','2','','''Type of approximation (0=exact 1=zone 2=acoustic)'''))
sfanisolr2.par('relation',rsf.doc.rsfpar('','3','','''Type of q relationship (0=shale, 1=sand, 2=carbonate, default being smallest error)'''))
sfanisolr2.par('xtaper',rsf.doc.rsfpar('','false','','''if taper in x'''))
sfanisolr2.par('ktaper',rsf.doc.rsfpar('','false','','''if taper in k'''))
sfanisolr2.version('2.1-git')
sfanisolr2.synopsis('''sfanisolr2 < velz.rsf vels=vels.rsf fft=fft.rsf xtap=fxtap.rsf ktap=fktap.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt= fftexp0=0 approx=2 relation=3 xtaper=false ktaper=false''','''''')
rsf.doc.progs['sfanisolr2']=sfanisolr2

sfisolr2 = rsf.doc.rsfprog('sfisolr2','user/fomels/Misolr2.cc','''Lowrank decomposition for 2-D isotropic wave propagation.''')
sfisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr2.version('2.1-git')
sfisolr2.synopsis('''sfisolr2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr2']=sfisolr2

sfisolr3 = rsf.doc.rsfprog('sfisolr3','user/fomels/Misolr3.cc','''Lowrank decomposition for 3-D isotropic wave propagation. ''')
sfisolr3.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr3.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr3.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr3.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr3.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr3.version('2.1-git')
sfisolr3.synopsis('''sfisolr3 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr3']=sfisolr3

sflrvc0 = rsf.doc.rsfprog('sflrvc0','user/fomels/Mlrvc0.cc','''Lowrank decomposition for zero-offset time migration''')
sflrvc0.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflrvc0.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflrvc0.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflrvc0.par('tol',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sflrvc0.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sflrvc0.par('v0',rsf.doc.rsfpar('','0.0','','''minimum velocity'''))
sflrvc0.par('fmin',rsf.doc.rsfpar('','dw','','''minimum frequency'''))
sflrvc0.par('tmax',rsf.doc.rsfpar('','t0+(nt-1','',''''''))
sflrvc0.version('2.1-git')
sflrvc0.synopsis('''sflrvc0 vel=vel.rsf < fft.rsf left=left.rsf > right.rsf seed=time(NULL tol=1.e-4 npk=20 v0=0.0 fmin=dw tmax=t0+(nt-1''','''''')
rsf.doc.progs['sflrvc0']=sflrvc0

sfpermlr1 = rsf.doc.rsfprog('sfpermlr1','user/fomels/Mpermlr1.cc','''Lowrank decomposition for prestack exploding reflector in v(z). ''')
sfpermlr1.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermlr1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpermlr1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpermlr1.par('size',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpermlr1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfpermlr1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfpermlr1.par('npk',rsf.doc.rsfpar('','5','','''maximum rank'''))
sfpermlr1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfpermlr1.version('2.1-git')
sfpermlr1.synopsis('''sfpermlr1 < vel.rsf fft=fft.rsf left=left.rsf right=right.rsf size=size.rsf seed=time(NULL eps=1.e-4 npk=5 dt=''','''''')
rsf.doc.progs['sfpermlr1']=sfpermlr1

sfpermlr2 = rsf.doc.rsfprog('sfpermlr2','user/fomels/Mpermlr2.cc','''Lowrank decomposition for 2-D prestack exploding reflector in V(z)''')
sfpermlr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermlr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpermlr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfpermlr2.par('tol',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfpermlr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfpermlr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfpermlr2.par('nh',rsf.doc.rsfpar('','','',''''''))
sfpermlr2.version('2.1-git')
sfpermlr2.synopsis('''sfpermlr2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL tol=1.e-4 npk=20 dt= nh=''','''''')
rsf.doc.progs['sfpermlr2']=sfpermlr2

sfpermlr3 = rsf.doc.rsfprog('sfpermlr3','user/fomels/Mpermlr3.cc','''Lowrank decomposition for 2-D prestack exploding reflector in V(x,z)''')
sfpermlr3.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermlr3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpermlr3.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfpermlr3.par('tol',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfpermlr3.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfpermlr3.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfpermlr3.par('eps',rsf.doc.rsfpar('','0.0','','''regularization'''))
sfpermlr3.par('nh',rsf.doc.rsfpar('','','',''''''))
sfpermlr3.par('equation',rsf.doc.rsfpar('','3','','''equation type'''))
sfpermlr3.par('sub',rsf.doc.rsfpar('','true','','''if subtract one'''))
sfpermlr3.version('2.1-git')
sfpermlr3.synopsis('''sfpermlr3 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL tol=1.e-4 npk=20 dt= eps=0.0 nh= equation=3 sub=true''','''''')
rsf.doc.progs['sfpermlr3']=sfpermlr3

sfbyte2jpg = rsf.doc.rsfprog('sfbyte2jpg','user/fomels/_byte2jpg.c','''Convert byte RSF to a JPEG image. ''')
sfbyte2jpg.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2jpg.version('2.1-git')
sfbyte2jpg.synopsis('''sfbyte2jpg < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2jpg']=sfbyte2jpg

sfjpg2byte = rsf.doc.rsfprog('sfjpg2byte','user/fomels/_jpg2byte.c','''Convert JPEG image to byte RSF. ''')
sfjpg2byte.version('2.1-git')
sfjpg2byte.synopsis('''sfjpg2byte > out.rsf < file.jpeg ''','''''')
rsf.doc.progs['sfjpg2byte']=sfjpg2byte

sfbyte2tif = rsf.doc.rsfprog('sfbyte2tif','user/fomels/_byte2tif.c','''Convert byte RSF to a TIFF image. ''')
sfbyte2tif.par('color',rsf.doc.rsfpar('bool','(bool)(3==n1)','',''''''))
sfbyte2tif.version('2.1-git')
sfbyte2tif.synopsis('''sfbyte2tif < in.rsf color=(bool)(3==n1)''','''''')
rsf.doc.progs['sfbyte2tif']=sfbyte2tif

sftif2byte = rsf.doc.rsfprog('sftif2byte','user/fomels/_tif2byte.c','''Convert TIFF image to byte RSF. ''')
sftif2byte.version('2.1-git')
sftif2byte.synopsis('''sftif2byte > out.rsf < file.tiff ''','''''')
rsf.doc.progs['sftif2byte']=sftif2byte

sfcgi = rsf.doc.rsfprog('sfcgi','user/fomels/Mcgi.py','''A generic CGI script''')
sfcgi.version('2.1-git')
sfcgi.synopsis('''sfcgi''','''''')
rsf.doc.progs['sfcgi']=sfcgi

sffft = rsf.doc.rsfprog('sffft','user/fomels/Mfft.py','''Fourier transform as a linear operator''')
sffft.version('2.1-git')
sffft.synopsis('''sffft''','''''')
rsf.doc.progs['sffft']=sffft

sfipick = rsf.doc.rsfprog('sfipick','user/fomels/Mipick.py','''Simple interactive picking''')
sfipick.version('2.1-git')
sfipick.synopsis('''sfipick''','''''')
rsf.doc.progs['sfipick']=sfipick

sflas2rsf = rsf.doc.rsfprog('sflas2rsf','user/fomels/Mlas2rsf.py','''Convert LAS-2 well logs to RSF''')
sflas2rsf.version('2.1-git')
sflas2rsf.synopsis('''sflas2rsf''','''''')
rsf.doc.progs['sflas2rsf']=sflas2rsf

sfmatplotlib = rsf.doc.rsfprog('sfmatplotlib','user/fomels/Mmatplotlib.py','''Plotting RSF files with matplotlib''')
sfmatplotlib.version('2.1-git')
sfmatplotlib.synopsis('''sfmatplotlib''','''''')
rsf.doc.progs['sfmatplotlib']=sfmatplotlib

sfresults = rsf.doc.rsfprog('sfresults','user/fomels/Mresults.py','''Explore project results''')
sfresults.version('2.1-git')
sfresults.synopsis('''sfresults''','''''')
rsf.doc.progs['sfresults']=sfresults

sfwxipick = rsf.doc.rsfprog('sfwxipick','user/fomels/Mwxipick.py','''Simple interactive picking''')
sfwxipick.version('2.1-git')
sfwxipick.synopsis('''sfwxipick''','''''')
rsf.doc.progs['sfwxipick']=sfwxipick

sfwxresults = rsf.doc.rsfprog('sfwxresults','user/fomels/Mwxresults.py','''Explore project results''')
sfwxresults.version('2.1-git')
sfwxresults.synopsis('''sfwxresults''','''''')
rsf.doc.progs['sfwxresults']=sfwxresults

sfzoom = rsf.doc.rsfprog('sfzoom','user/fomels/Mzoom.py','''Show data with zoom''')
sfzoom.version('2.1-git')
sfzoom.synopsis('''sfzoom''','''''')
rsf.doc.progs['sfzoom']=sfzoom

sfwxzoom = rsf.doc.rsfprog('sfwxzoom','user/fomels/Mwxzoom.py','''Show data with zoom''')
sfwxzoom.version('2.1-git')
sfwxzoom.synopsis('''sfwxzoom''','''''')
rsf.doc.progs['sfwxzoom']=sfwxzoom

