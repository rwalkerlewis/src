import rsf.doc

sfcohn = rsf.doc.rsfprog('sfcohn','user/pyang/Mcohn.c','''Coherence calculations in the presence of structural dip''')
sfcohn.par('idip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcohn.par('xdip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcohn.par('ntw',rsf.doc.rsfpar('int','5','','''half window size for coherence '''))
sfcohn.par('nxw',rsf.doc.rsfpar('int','5','','''half window size for coherence '''))
sfcohn.par('nyw',rsf.doc.rsfpar('int','5','','''half window size for coherence '''))
sfcohn.par('twod',rsf.doc.rsfpar('bool','y','','''y: only twod coherence '''))
sfcohn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfcohn.par('op1',rsf.doc.rsfpar('float','-2.0','',''''''))
sfcohn.par('dp1',rsf.doc.rsfpar('float','0.5','',''''''))
sfcohn.par('np1',rsf.doc.rsfpar('int','9','','''inline slope '''))
sfcohn.par('op2',rsf.doc.rsfpar('float','-2.0','',''''''))
sfcohn.par('dp2',rsf.doc.rsfpar('float','0.5','',''''''))
sfcohn.par('np2',rsf.doc.rsfpar('int','9','','''xline slope '''))
sfcohn.par('idip',rsf.doc.rsfpar('string ',desc='''inline dip (auxiliary output file name)'''))
sfcohn.par('xdip',rsf.doc.rsfpar('string ',desc='''crossline dip (auxiliary output file name)'''))
sfcohn.par('mode',rsf.doc.rsfpar('string ',desc='''coherence mode: c1, c2, c3 '''))
sfcohn.version('2.1-git')
sfcohn.synopsis('''sfcohn < in.rsf > out.rsf idip=idip.rsf xdip=xdip.rsf ntw=5 nxw=5 nyw=5 twod=y verb=y op1=-2.0 dp1=0.5 np1=9 op2=-2.0 dp2=0.5 np2=9 mode=''','''''')
rsf.doc.progs['sfcohn']=sfcohn

sfcheckptdemo = rsf.doc.rsfprog('sfcheckptdemo','user/pyang/Mcheckptdemo.c','''RTM with checkpointing in 2D acoustic media''')
sfcheckptdemo.par('p1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcheckptdemo.par('p2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfcheckptdemo.par('nb',rsf.doc.rsfpar('int','20','','''thickness of PML ABC '''))
sfcheckptdemo.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfcheckptdemo.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfcheckptdemo.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfcheckptdemo.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfcheckptdemo.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfcheckptdemo.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfcheckptdemo.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfcheckptdemo.par('nob',rsf.doc.rsfpar('int','(int)log2f(nt)','','''number of buffers, default=optimal value '''))
sfcheckptdemo.version('2.1-git')
sfcheckptdemo.synopsis('''sfcheckptdemo < Fv.rsf > Fw.rsf p1=Fp1.rsf p2=Fp2.rsf nb=20 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt= nob=(int)log2f(nt)''','''The real value of checkpointing technology resides in the backpropagation with
viscoacoustic and viscoelastic wave equation, where the wavefield 
reconstruction method using saved boundaries fails. Here, we only
demonstrate how to implement it in acoustic media without dissipation.
''')
rsf.doc.progs['sfcheckptdemo']=sfcheckptdemo

sffwi2d = rsf.doc.rsfprog('sffwi2d','user/pyang/Mfwi2d.c','''Time domain full waveform inversion ''')
sffwi2d.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffwi2d.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffwi2d.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffwi2d.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffwi2d.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sffwi2d.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sffwi2d.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffwi2d.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sffwi2d.version('2.1-git')
sffwi2d.synopsis('''sffwi2d < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf illums=illums.rsf objs=objs.rsf verb=y precon=n niter=100 rbell=2''','''Note: This serial FWI is merely designed to help the understanding of 
beginners. Enquist absorbing boundary condition (A2) is applied!
''')
rsf.doc.progs['sffwi2d']=sffwi2d

sffbrec2d = rsf.doc.rsfprog('sffbrec2d','user/pyang/Mfbrec2d.c','''2-D forward modeling to generate shot records ''')
sffbrec2d.par('check1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffbrec2d.par('check2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffbrec2d.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sffbrec2d.par('amp',rsf.doc.rsfpar('float','1.','','''maximum amplitude of ricker '''))
sffbrec2d.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sffbrec2d.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sffbrec2d.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sffbrec2d.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sffbrec2d.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sffbrec2d.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sffbrec2d.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sffbrec2d.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sffbrec2d.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sffbrec2d.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sffbrec2d.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sffbrec2d.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sffbrec2d.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sffbrec2d.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sffbrec2d.version('2.1-git')
sffbrec2d.synopsis('''sffbrec2d < vinit.rsf > shots.rsf check1=check1.rsf check2=check2.rsf kt=100 amp=1. fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''Note: 	Clayton-Enquist absorbing boundary condition is applied!
''')
rsf.doc.progs['sffbrec2d']=sffbrec2d

sfistseislet = rsf.doc.rsfprog('sfistseislet','user/pyang/Mistseislet.c','''Analysis-based IST interpolation using seislet (2d validation)''')
sfistseislet.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistseislet.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfistseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfistseislet.par('pscale',rsf.doc.rsfpar('float','25','','''percentile of small scale to be preserved (default is 25)'''))
sfistseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfistseislet.par('niter',rsf.doc.rsfpar('int','10','','''total number iterations '''))
sfistseislet.par('pclip',rsf.doc.rsfpar('float','99','','''starting data clip percentile (default is 99)'''))
sfistseislet.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sfistseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfistseislet.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfistseislet.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfistseislet.version('2.1-git')
sfistseislet.synopsis('''sfistseislet < Fin.rsf mask=Fmask.rsf > Fout.rsf dip=Fdip.rsf eps=0.01 order=1 pscale=25 verb=n niter=10 pclip=99 p=0.35 type= mode=''','''IST=iterative shrinkage-thresholding
''')
rsf.doc.progs['sfistseislet']=sfistseislet

sflsrtm2d = rsf.doc.rsfprog('sflsrtm2d','user/pyang/Mlsrtm2d.c','''2-D zero-offset least-squares reverse time migration (LSRTM)''')
sflsrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sflsrtm2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsrtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsrtm2d.par('tol',rsf.doc.rsfpar('float','1.e-12','','''tolerance of inversion '''))
sflsrtm2d.version('2.1-git')
sflsrtm2d.synopsis('''sflsrtm2d < data.rsf > imag.rsf vel=modl.rsf n0=0 verb=n niter=10 tol=1.e-12''','''''')
rsf.doc.progs['sflsrtm2d']=sflsrtm2d

sflsprtm2d = rsf.doc.rsfprog('sflsprtm2d','user/pyang/Mlsprtm2d.c','''least-squares prestack RTM in 2-D ''')
sflsprtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsprtm2d.par('imgrtm',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflsprtm2d.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflsprtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsprtm2d.par('nb',rsf.doc.rsfpar('int','20','','''number (thickness) of ABC on each side '''))
sflsprtm2d.par('fromBoundary',rsf.doc.rsfpar('bool','y','','''if fromBoundary=true, reconstruct source wavefield from stored boundary '''))
sflsprtm2d.par('testadj',rsf.doc.rsfpar('int','0','','''if testadj = 1 then program only testadj without calculating '''))
sflsprtm2d.version('2.1-git')
sflsprtm2d.synopsis('''sflsprtm2d < shots.rsf vel=velo.rsf > imglsm.rsf imgrtm=imgrtm.rsf verb=y niter=10 nb=20 fromBoundary=y testadj=0''','''''')
rsf.doc.progs['sflsprtm2d']=sflsprtm2d

sfmythresh = rsf.doc.rsfprog('sfmythresh','user/pyang/Mmythresh.c','''Generalized thresholding operator''')
sfmythresh.par('pclip',rsf.doc.rsfpar('float','99.','','''percentage to clip '''))
sfmythresh.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sfmythresh.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode='hard', 'soft','pthresh' or 'exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfmythresh.version('2.1-git')
sfmythresh.synopsis('''sfmythresh < in.rsf > out.rsf pclip=99. p=0.35 mode=''','''''')
rsf.doc.progs['sfmythresh']=sfmythresh

sfmshots = rsf.doc.rsfprog('sfmshots','user/pyang/Mmshots.c','''2-D prestack forward modeling using sponge ABC using 4-th order FD''')
sfmshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfmshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfmshots.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC  '''))
sfmshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfmshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfmshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfmshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfmshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfmshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfmshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfmshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfmshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfmshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfmshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfmshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfmshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point '''))
sfmshots.par('mute',rsf.doc.rsfpar('bool','n','','''if yes, muting the direct arrivals '''))
sfmshots.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq artifacts, unit=m/s'''))
sfmshots.par('tdmute',rsf.doc.rsfpar('int','2.0/(fm*dt)','','''number of deleyed time samples to mute '''))
sfmshots.version('2.1-git')
sfmshots.synopsis('''sfmshots < vinit.rsf > shots.rsf amp=1000 fm=10 nb=30 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n mute=n vmute=1500 tdmute=2.0/(fm*dt)''','''NB: prepare high quality prestack seismic data for LSRTM and FWI
Top boundary is free surface (no ABC applied)!
''')
rsf.doc.progs['sfmshots']=sfmshots

sfmcaseislet = rsf.doc.rsfprog('sfmcaseislet','user/pyang/Mmcaseislet.c','''Morphological component analysis using 2-D Seislet transform ''')
sfmcaseislet.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmcaseislet.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmcaseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfmcaseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfmcaseislet.par('pscale',rsf.doc.rsfpar('float','25','','''percentile of small scale to be preserved (default is 100)'''))
sfmcaseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity or not '''))
sfmcaseislet.par('decr',rsf.doc.rsfpar('bool','y','','''decrease threshold in iterations or not '''))
sfmcaseislet.par('niter',rsf.doc.rsfpar('int','10','','''total number iterations '''))
sfmcaseislet.par('pclip',rsf.doc.rsfpar('float','10','','''starting data clip percentile (default is 10)'''))
sfmcaseislet.par('p',rsf.doc.rsfpar('float','0.5','','''norm=p, where 0<p<=1 '''))
sfmcaseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfmcaseislet.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfmcaseislet.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmcaseislet.version('2.1-git')
sfmcaseislet.synopsis('''sfmcaseislet < Fin.rsf > Fout.rsf dips=Fdips.rsf mask=Fmask.rsf eps=0.01 order=1 pscale=25 verb=n decr=y niter=10 pclip=10 p=0.5 type= mode=''','''Note:  Here, nc components with nc seislet transforms build a seislet 
frame to do the simultineous multicomponent separation and interpolation.	
''')
rsf.doc.progs['sfmcaseislet']=sfmcaseislet

sfmodeling2d = rsf.doc.rsfprog('sfmodeling2d','user/pyang/Mmodeling2d.c','''2-D forward modeling to generate shot records ''')
sfmodeling2d.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmodeling2d.par('check',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmodeling2d.par('chk',rsf.doc.rsfpar('bool','','',''''''))
sfmodeling2d.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sfmodeling2d.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfmodeling2d.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfmodeling2d.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfmodeling2d.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfmodeling2d.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfmodeling2d.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfmodeling2d.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfmodeling2d.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfmodeling2d.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfmodeling2d.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfmodeling2d.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfmodeling2d.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfmodeling2d.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfmodeling2d.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfmodeling2d.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfmodeling2d.version('2.1-git')
sfmodeling2d.synopsis('''sfmodeling2d < vinit.rsf > shots.rsf time=time.rsf check=check.rsf chk= kt=100 amp=1000 fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''Note: Clayton-Enquist absorbing boundary condition (A2) is applied!
''')
rsf.doc.progs['sfmodeling2d']=sfmodeling2d

sfmysnr = rsf.doc.rsfprog('sfmysnr','user/pyang/Mmysnr.c','''print out signal-to-noise ratio in decibel (dB)''')
sfmysnr.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmysnr.version('2.1-git')
sfmysnr.synopsis('''sfmysnr < in.rsf ref=ref.rsf > out.rsf''','''''')
rsf.doc.progs['sfmysnr']=sfmysnr

sfpocsseislet = rsf.doc.rsfprog('sfpocsseislet','user/pyang/Mpocsseislet.c','''Seislet-based POCS interpolation (2d validation)''')
sfpocsseislet.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocsseislet.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocsseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpocsseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order for seislet transform'''))
sfpocsseislet.par('pscale',rsf.doc.rsfpar('float','25','','''percentile of small scale to be preserved (default is 25)'''))
sfpocsseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpocsseislet.par('niter',rsf.doc.rsfpar('int','10','','''total number iterations '''))
sfpocsseislet.par('pclip',rsf.doc.rsfpar('float','99','','''starting data clip percentile (default is 99)'''))
sfpocsseislet.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sfpocsseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfpocsseislet.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfpocsseislet.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocsseislet.version('2.1-git')
sfpocsseislet.synopsis('''sfpocsseislet < Fin.rsf mask=Fmask.rsf > Fout.rsf dip=Fdip.rsf eps=0.01 order=1 pscale=25 verb=n niter=10 pclip=99 p=0.35 type= mode=''','''POCS=projection onto convex sets
''')
rsf.doc.progs['sfpocsseislet']=sfpocsseislet

sfrtm2d = rsf.doc.rsfprog('sfrtm2d','user/pyang/Mrtm2d.c','''2-D zero-offset reverse-time migration''')
sfrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtm2d.par('adj',rsf.doc.rsfpar('bool','n','','''if y, migration; else, modeling '''))
sfrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sfrtm2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfrtm2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval: dt '''))
sfrtm2d.version('2.1-git')
sfrtm2d.synopsis('''sfrtm2d vel=modl.rsf < data.rsf > imag.rsf adj=n n0=0 nt= dt=''','''''')
rsf.doc.progs['sfrtm2d']=sfrtm2d

sfrtmadcig = rsf.doc.rsfprog('sfrtmadcig','user/pyang/Mrtmadcig.c','''RTM and angle gather (ADCIG) extraction using poynting vector''')
sfrtmadcig.par('velsmooth',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtmadcig.par('vecx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmadcig.par('vecz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmadcig.par('amp',rsf.doc.rsfpar('float','1.e3','','''maximum amplitude of ricker wavelet'''))
sfrtmadcig.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfrtmadcig.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfrtmadcig.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfrtmadcig.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfrtmadcig.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfrtmadcig.par('nb',rsf.doc.rsfpar('int','20','','''thickness of split PML '''))
sfrtmadcig.par('na',rsf.doc.rsfpar('int','30','','''number of angles'''))
sfrtmadcig.par('kt',rsf.doc.rsfpar('int','200','','''record poynting vector at kt '''))
sfrtmadcig.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfrtmadcig.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfrtmadcig.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfrtmadcig.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfrtmadcig.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfrtmadcig.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfrtmadcig.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfrtmadcig.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfrtmadcig.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfrtmadcig.version('2.1-git')
sfrtmadcig.synopsis('''sfrtmadcig < vmodl.rsf velsmooth=vmods.rsf > rtmadcig.rsf vecx=vecx.rsf vecz=vecz.rsf amp=1.e3 fm= dt= nt= ns= ng= nb=20 na=30 kt=200 jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y''','''SPML boundary condition combined with 4-th order finite difference,
effective boundary saving strategy used!
''')
rsf.doc.progs['sfrtmadcig']=sfrtmadcig

sfrtmodcig = rsf.doc.rsfprog('sfrtmodcig','user/pyang/Mrtmodcig.c','''RTM output ODCIG with extended images''')
sfrtmodcig.par('vel1stlayer',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtmodcig.par('amp',rsf.doc.rsfpar('float','1.','','''maximum amplitude of ricker wavelet'''))
sfrtmodcig.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfrtmodcig.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfrtmodcig.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfrtmodcig.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfrtmodcig.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfrtmodcig.par('nb',rsf.doc.rsfpar('int','20','','''thickness of split PML '''))
sfrtmodcig.par('nh',rsf.doc.rsfpar('int','30','','''number of points in offset coordinate'''))
sfrtmodcig.par('kt',rsf.doc.rsfpar('int','200','','''record poynting vector at kt '''))
sfrtmodcig.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfrtmodcig.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfrtmodcig.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfrtmodcig.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfrtmodcig.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfrtmodcig.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfrtmodcig.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfrtmodcig.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfrtmodcig.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfrtmodcig.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq noise, unit=m/s'''))
sfrtmodcig.par('tdmute',rsf.doc.rsfpar('int','2./(fm*dt)','','''number of deleyed time samples to mute '''))
sfrtmodcig.version('2.1-git')
sfrtmodcig.synopsis('''sfrtmodcig < vmodl.rsf vel1stlayer=vmods.rsf > Fodcig.rsf amp=1. fm= dt= nt= ns= ng= nb=20 nh=30 kt=200 jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y vmute=1500 tdmute=2./(fm*dt)''','''''')
rsf.doc.progs['sfrtmodcig']=sfrtmodcig

sfrtmva2d = rsf.doc.rsfprog('sfrtmva2d','user/pyang/Mrtmva2d.c','''RTM with checkpointing in 2D acoustic media''')
sfrtmva2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtmva2d.par('tau',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtmva2d.par('tauo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtmva2d.par('p1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmva2d.par('p2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrtmva2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfrtmva2d.par('nb',rsf.doc.rsfpar('int','20','','''thickness of PML ABC '''))
sfrtmva2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfrtmva2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfrtmva2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfrtmva2d.par('ns',rsf.doc.rsfpar('int','','','''number of shots '''))
sfrtmva2d.par('ng',rsf.doc.rsfpar('int','','','''number of geophones/receivers per shot '''))
sfrtmva2d.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfrtmva2d.par('nob',rsf.doc.rsfpar('int','(int)log2f(nt)','','''number of buffers, default=optimal value '''))
sfrtmva2d.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfrtmva2d.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfrtmva2d.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfrtmva2d.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfrtmva2d.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfrtmva2d.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfrtmva2d.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfrtmva2d.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfrtmva2d.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfrtmva2d.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq noise, unit=m/s'''))
sfrtmva2d.par('tdmute',rsf.doc.rsfpar('int','2./(fm*dt)','','''number of deleyed time samples to mute '''))
sfrtmva2d.version('2.1-git')
sfrtmva2d.synopsis('''sfrtmva2d < Fv.rsf rho=Frho.rsf tau=Ftau.rsf tauo=Ftauo.rsf > Fw.rsf p1=Fp1.rsf p2=Fp2.rsf verb=n nb=20 nt= dt= fm=20.0 ns= ng= kt= nob=(int)log2f(nt) jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y vmute=1500 tdmute=2./(fm*dt)''','''The real value of checkpointing technology resides in the backpropagation with
viscoacoustic and viscoelastic wave equation, where the wavefield 
reconstruction method using saved boundaries fails. Here, we only
demonstrate how to implement it in acoustic media without dissipation.
Note the backpropagation operator should be the adjoint of forward modeling!
Here we just use forward modeling operator for the time being!
''')
rsf.doc.progs['sfrtmva2d']=sfrtmva2d

sfTestfd2d = rsf.doc.rsfprog('sfTestfd2d','user/pyang/MTestfd2d.c','''A demo of 2D FD test''')
sfTestfd2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestfd2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestfd2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestfd2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestfd2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestfd2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestfd2d.version('2.1-git')
sfTestfd2d.synopsis('''sfTestfd2d < Fv.rsf > Fw.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''Sponage absorbing boundary condition
''')
rsf.doc.progs['sfTestfd2d']=sfTestfd2d

sfTestfd3d = rsf.doc.rsfprog('sfTestfd3d','user/pyang/MTestfd3d.c','''3D acoustic time-domain FD modeling''')
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestfd3d.par('frsf',rsf.doc.rsfpar('bool','n','','''free surface or not '''))
sfTestfd3d.par('nt',rsf.doc.rsfpar('int','','',''''''))
sfTestfd3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfTestfd3d.par('ns',rsf.doc.rsfpar('int','1','',''''''))
sfTestfd3d.par('nb',rsf.doc.rsfpar('int','30','',''''''))
sfTestfd3d.par('dt',rsf.doc.rsfpar('float','','',''''''))
sfTestfd3d.par('fm',rsf.doc.rsfpar('float','20','',''''''))
sfTestfd3d.version('2.1-git')
sfTestfd3d.synopsis('''sfTestfd3d < Fv.rsf > Fw.rsf verb=n verb=n frsf=n nt= kt= ns=1 nb=30 dt= fm=20''','''4th order in space, 2nd order in time, sponge absorbing boundary condition.
''')
rsf.doc.progs['sfTestfd3d']=sfTestfd3d

sfTesteb = rsf.doc.rsfprog('sfTesteb','user/pyang/MTesteb.c','''Demo for effective boundary saving in regular grid''')
sfTesteb.par('back',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTesteb.par('nb',rsf.doc.rsfpar('int','20','','''thickness of sponge ABC '''))
sfTesteb.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTesteb.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTesteb.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTesteb.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTesteb.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTesteb.par('ns',rsf.doc.rsfpar('int','1','','''number of shots '''))
sfTesteb.par('ng',rsf.doc.rsfpar('int','nx','','''number of receivers '''))
sfTesteb.version('2.1-git')
sfTesteb.synopsis('''sfTesteb < Fv.rsf > Fw1.rsf back=Fw2.rsf nb=20 nt= dt= fm=20.0 ft=0 jt=1 ns=1 ng=nx''','''The sponge absorbing boundary condition is applied for simplicity!
2N-order FD: effective boundary needs N points on each side!
Note: In this demo, 2N=4 (N=2). 
''')
rsf.doc.progs['sfTesteb']=sfTesteb

sfTestelastic2d = rsf.doc.rsfprog('sfTestelastic2d','user/pyang/MTestelastic2d.c','''2D 8-th order elastic wave propagation using sponge ABC''')
sfTestelastic2d.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestelastic2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestelastic2d.par('wavx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestelastic2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestelastic2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML boundary '''))
sfTestelastic2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestelastic2d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfTestelastic2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestelastic2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestelastic2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestelastic2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestelastic2d.version('2.1-git')
sfTestelastic2d.synopsis('''sfTestelastic2d < Fvp.rsf vs=Fvs.rsf rho=Frho.rsf > Fwavz.rsf wavx=Fwavx.rsf verb=n nb=30 nt= kt= dt= fm=20.0 ft=0 jt=1''','''''')
rsf.doc.progs['sfTestelastic2d']=sfTestelastic2d

sfTestaniso = rsf.doc.rsfprog('sfTestaniso','user/pyang/MTestaniso.c','''A 2D demo of elliptically-anisotropic wave propagation (4th order)''')
sfTestaniso.par('vx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfTestaniso.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfTestaniso.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfTestaniso.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestaniso.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestaniso.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestaniso.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestaniso.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestaniso.version('2.1-git')
sfTestaniso.synopsis('''sfTestaniso < Fvz.rsf vx=Fvx.rsf > Fw.rsf verb=n nb=30 nt= dt= fm=20.0 ft=0 jt=1''','''Note: It is adapted according to Seregy Fomel's lecture on Seismic imaging.
''')
rsf.doc.progs['sfTestaniso']=sfTestaniso

sfTestspml = rsf.doc.rsfprog('sfTestspml','user/pyang/MTestspml.c','''2D acoustic FD using Split PML (SPML) absorbing boundary condition''')
sfTestspml.par('pz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('px',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTestspml.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML ABC '''))
sfTestspml.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTestspml.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTestspml.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTestspml.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTestspml.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTestspml.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfTestspml.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfTestspml.version('2.1-git')
sfTestspml.synopsis('''sfTestspml < Fv.rsf > Fw.rsf pz=Fpz.rsf px=Fpx.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt=''','''NB: Staggered grid finite difference used!
''')
rsf.doc.progs['sfTestspml']=sfTestspml

sfviscoa2d = rsf.doc.rsfprog('sfviscoa2d','user/pyang/Mviscoa2d.c','''2D visco-acoustic modeling with 8th order staggered-grid FD''')
sfviscoa2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('tau',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('tauo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoa2d.par('pz',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoa2d.par('px',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoa2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of PML ABC '''))
sfviscoa2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfviscoa2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfviscoa2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfviscoa2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfviscoa2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfviscoa2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity, if y, output px and pz '''))
sfviscoa2d.par('kt',rsf.doc.rsfpar('int','','','''output px and pz component at kt '''))
sfviscoa2d.version('2.1-git')
sfviscoa2d.synopsis('''sfviscoa2d < Fv.rsf rho=Frho.rsf tau=Ftau.rsf tauo=Ftauo.rsf > Fw.rsf pz=Fpz.rsf px=Fpx.rsf nb=30 nt= dt= fm=20.0 ft=0 jt=1 verb=n kt=''','''''')
rsf.doc.progs['sfviscoa2d']=sfviscoa2d

sfviscoe2d = rsf.doc.rsfprog('sfviscoe2d','user/pyang/Mviscoe2d.c','''2D 4-th order visco-elastic wave propagation using sponge ABC''')
sfviscoe2d.par('vs',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('rho',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('taup',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('taus',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('tauo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfviscoe2d.par('wavx',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfviscoe2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfviscoe2d.par('nb',rsf.doc.rsfpar('int','30','','''thickness of sponge ABC '''))
sfviscoe2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfviscoe2d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfviscoe2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfviscoe2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfviscoe2d.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfviscoe2d.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfviscoe2d.version('2.1-git')
sfviscoe2d.synopsis('''sfviscoe2d < Fvp.rsf vs=Fvs.rsf rho=Frho.rsf taup=Ftaup.rsf taus=Ftaus.rsf tauo=Ftauo.rsf > Fwavz.rsf wavx=Fwavx.rsf verb=n nb=30 nt= kt= dt= fm=20.0 ft=0 jt=1''','''''')
rsf.doc.progs['sfviscoe2d']=sfviscoe2d

sfexcitationic = rsf.doc.rsfprog('sfexcitationic','user/pyang/Mexcitationic.c','''Demo for excitation imaging condition''')
sfexcitationic.par('nb',rsf.doc.rsfpar('int','20','','''thickness of sponge ABC '''))
sfexcitationic.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfexcitationic.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfexcitationic.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfexcitationic.par('kt',rsf.doc.rsfpar('int','300','','''output wavefield at time kt '''))
sfexcitationic.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfexcitationic.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfexcitationic.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfexcitationic.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfexcitationic.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfexcitationic.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfexcitationic.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfexcitationic.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfexcitationic.par('csdgather',rsf.doc.rsfpar('bool','y','',''''''))
sfexcitationic.par('ns',rsf.doc.rsfpar('int','1','','''number of shots '''))
sfexcitationic.par('ng',rsf.doc.rsfpar('int','nx','','''number of receivers '''))
sfexcitationic.version('2.1-git')
sfexcitationic.synopsis('''sfexcitationic < Fv.rsf > Fout.rsf nb=20 nt= dt= fm=20.0 kt=300 jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y ns=1 ng=nx''','''Note that excitation imaging condition has some multipathing artifacts.
The significance of this imaging condition is the cheap computation and
low memory requirement. (1) Cheap computation: only 2 times of simulation,
one for source wavefield the other for receiver wavefield, are needed for 
single shot imaging before stacking. (2) Low memory request: this imaging 
condition only asks for the excitation time and the amplitude. Therefore,
it differs from cross-correlation imaging condition which needs storing 
or reconstructing the source wavefield to cross-correlate with receiver
wavefield at each time step.
''')
rsf.doc.progs['sfexcitationic']=sfexcitationic

sfdlct = rsf.doc.rsfprog('sfdlct','user/pyang/Mdlct.c','''discrete linear chirp transfrom (DLCT)''')
sfdlct.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform (Here adjoint is the same as inverse!) '''))
sfdlct.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdlct.par('C',rsf.doc.rsfpar('float','0.005','','''C=2*Lambda/L, unit slice '''))
sfdlct.par('L',rsf.doc.rsfpar('int','','',''''''))
sfdlct.version('2.1-git')
sfdlct.synopsis('''sfdlct < in.rsf > out.rsf inv=n verb=n C=0.005 L=''','''''')
rsf.doc.progs['sfdlct']=sfdlct

sffpocs2d = rsf.doc.rsfprog('sffpocs2d','user/pyang/Mfpocs2d.c','''2-D Two-step POCS interpolation using a general Lp-norm optimization''')
sffpocs2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffpocs2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffpocs2d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sffpocs2d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sffpocs2d.par('pclip',rsf.doc.rsfpar('float','99.','','''starting data clip percentile (default is 99)'''))
sffpocs2d.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sffpocs2d.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sffpocs2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffpocs2d.version('2.1-git')
sffpocs2d.synopsis('''sffpocs2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6 pclip=99. p=0.35 mode=''','''''')
rsf.doc.progs['sffpocs2d']=sffpocs2d

sffpocs3d = rsf.doc.rsfprog('sffpocs3d','user/pyang/Mfpocs3d.c','''3-D Two-step POCS interpolation using a general Lp-norm optimization''')
sffpocs3d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffpocs3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffpocs3d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sffpocs3d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sffpocs3d.par('pclip',rsf.doc.rsfpar('float','99.','','''starting data clip percentile (default is 99)'''))
sffpocs3d.par('p',rsf.doc.rsfpar('float','0.35','','''norm=p, where 0<p<=1 '''))
sffpocs3d.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sffpocs3d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffpocs3d.version('2.1-git')
sffpocs3d.synopsis('''sffpocs3d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6 pclip=99. p=0.35 mode=''','''''')
rsf.doc.progs['sffpocs3d']=sffpocs3d

sfistinterp = rsf.doc.rsfprog('sfistinterp','user/pyang/Mistinterp.c','''n-D IST interpolation using a generalized shrinkage operator''')
sfistinterp.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistinterp.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfistinterp.par('niter',rsf.doc.rsfpar('int','100','','''total number of iterations '''))
sfistinterp.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 10)'''))
sfistinterp.par('normp',rsf.doc.rsfpar('float','0.9','','''quasi-norm: normp<2 '''))
sfistinterp.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfistinterp.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	'soft', soft thresholding; 
       'pthresh', generalized quasi-p; 'exp', exponential shrinkage '''))
sfistinterp.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfistinterp.version('2.1-git')
sfistinterp.synopsis('''sfistinterp < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. normp=0.9 n#= mode=''','''Note: Acquistion geometry specified by mask operator
''')
rsf.doc.progs['sfistinterp']=sfistinterp

sflsinterp2d = rsf.doc.rsfprog('sflsinterp2d','user/pyang/Mlsinterp2d.c','''Least-squares interpolation for 2D validition''')
sflsinterp2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsinterp2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsinterp2d.par('niter',rsf.doc.rsfpar('int','100','','''inner iterations '''))
sflsinterp2d.par('nouter',rsf.doc.rsfpar('int','5','','''outer iterations '''))
sflsinterp2d.par('eps',rsf.doc.rsfpar('float','1.e-2','','''regularization parameter '''))
sflsinterp2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsinterp2d.version('2.1-git')
sflsinterp2d.synopsis('''sflsinterp2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 nouter=5 eps=1.e-2''','''''')
rsf.doc.progs['sflsinterp2d']=sflsinterp2d

sfistpad = rsf.doc.rsfprog('sfistpad','user/pyang/Mistpad.c','''n-D IST interpolation using a generalized shrinkage operator and zero-padding''')
sfistpad.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfistpad.par('pad',rsf.doc.rsfpar('ints','','','''number of zeros to be padded for each axis  [dim]'''))
sfistpad.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfistpad.par('pow2',rsf.doc.rsfpar('bool','n','','''round up the length of each axis to be power of 2 '''))
sfistpad.par('niter',rsf.doc.rsfpar('int','100','','''total number of iterations '''))
sfistpad.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 10)'''))
sfistpad.par('normp',rsf.doc.rsfpar('float','1.','','''quasi-norm: normp<2 '''))
sfistpad.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfistpad.par('mode',rsf.doc.rsfpar('string ',desc='''thresholding mode: 'hard', 'soft','pthresh','exp';
       'hard', hard thresholding;	   'soft', soft thresholding; 
       'pthresh', generalized quasi-p;  'exp', exponential shrinkage '''))
sfistpad.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfistpad.version('2.1-git')
sfistpad.synopsis('''sfistpad < in.rsf > out.rsf mask=Fmask.rsf pad= verb=n pow2=n niter=100 pclip=10. normp=1. n#= mode=''','''Note: Acquistion geometry specified by mask operator
''')
rsf.doc.progs['sfistpad']=sfistpad

sfpocs3d = rsf.doc.rsfprog('sfpocs3d','user/pyang/Mpocs3d.c','''POCS for 3D missing data interpolation''')
sfpocs3d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocs3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpocs3d.par('niter',rsf.doc.rsfpar('int','100','','''total number of POCS iterations '''))
sfpocs3d.par('pclip',rsf.doc.rsfpar('float','99.','','''starting data clip percentile (default is 99)'''))
sfpocs3d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocs3d.version('2.1-git')
sfpocs3d.synopsis('''sfpocs3d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 pclip=99.''','''''')
rsf.doc.progs['sfpocs3d']=sfpocs3d

sfpocs = rsf.doc.rsfprog('sfpocs','user/pyang/Mpocs.c','''n-D POCS interpolation using a hard thresholding''')
sfpocs.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpocs.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfpocs.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfpocs.par('pclip',rsf.doc.rsfpar('float','10.','','''starting data clip percentile (default is 99)'''))
sfpocs.par('n#',rsf.doc.rsfpar('int','','','''size of #-th axis '''))
sfpocs.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpocs.version('2.1-git')
sfpocs.synopsis('''sfpocs < in.rsf > out.rsf mask=Fmask.rsf verb=n niter=100 pclip=10. n#=''','''Note: Acquistion geometry specified by mask operator.
''')
rsf.doc.progs['sfpocs']=sfpocs

sfps2d = rsf.doc.rsfprog('sfps2d','user/pyang/Mps2d.c','''2-D attenuating wavefield simulation using Fourier Pseudo Spectral method ''')
sfps2d.par('Qp',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfps2d.par('nb',rsf.doc.rsfpar('int','20','','''thickness of sponge ABC '''))
sfps2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfps2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfps2d.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfps2d.par('kt',rsf.doc.rsfpar('int','nt','',''''''))
sfps2d.version('2.1-git')
sfps2d.synopsis('''sfps2d < Fv.rsf Qp=FQp.rsf > Fw.rsf nb=20 nt= dt= fm=20.0 kt=nt''','''for computing fractional laplacian instead of fractional time derivative
''')
rsf.doc.progs['sfps2d']=sfps2d

sfmwni2d = rsf.doc.rsfprog('sfmwni2d','user/pyang/Mmwni2d.c','''2-D bandlimited minimum weighted-norm interpolation (MWNI) ''')
sfmwni2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmwni2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfmwni2d.par('niter',rsf.doc.rsfpar('int','100','','''total number iterations '''))
sfmwni2d.par('tol',rsf.doc.rsfpar('float','1.0e-6','','''iteration tolerance '''))
sfmwni2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfmwni2d.version('2.1-git')
sfmwni2d.synopsis('''sfmwni2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 tol=1.0e-6''','''implemented with conjugate gradient least squares (CGLS) method
''')
rsf.doc.progs['sfmwni2d']=sfmwni2d

sfmyradon2 = rsf.doc.rsfprog('sfmyradon2','user/pyang/Mmyradon2.c','''Linear/parabolic radon transform frequency domain implementation ''')
sfmyradon2.par('adj',rsf.doc.rsfpar('bool','y','','''if y, perform adjoint operation '''))
sfmyradon2.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse operation '''))
sfmyradon2.par('np',rsf.doc.rsfpar('int','','','''number of p values (if adj=y) '''))
sfmyradon2.par('dp',rsf.doc.rsfpar('float','','','''p sampling (if adj=y) '''))
sfmyradon2.par('p0',rsf.doc.rsfpar('float','','','''p origin (if adj=y) '''))
sfmyradon2.par('niter',rsf.doc.rsfpar('int','100','','''number of CGLS iterations '''))
sfmyradon2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization parameter '''))
sfmyradon2.par('nx',rsf.doc.rsfpar('int','','','''number of offsets (if adj=n) '''))
sfmyradon2.par('ox',rsf.doc.rsfpar('float','','','''x origin '''))
sfmyradon2.par('dx',rsf.doc.rsfpar('float','','','''sampling interval in x '''))
sfmyradon2.par('parab',rsf.doc.rsfpar('bool','n','','''if y, parabolic Radon transform '''))
sfmyradon2.par('x0',rsf.doc.rsfpar('float','1.','','''reference offset '''))
sfmyradon2.par('invmode',rsf.doc.rsfpar('string ',desc='''inverse method: 'ls' if least-squares; 'toeplitz' if use FFT '''))
sfmyradon2.version('2.1-git')
sfmyradon2.synopsis('''sfmyradon2 < in.rsf > out.rsf adj=y inv=n np= dp= p0= niter=100 eps=0.01 nx= ox= dx= parab=n x0=1. invmode=''','''Also referred to as high-resolution radon transform
Note: I borrowed a lot from /system/seismic/radon+Mradon.c. The distinction:
I am using FFTW because I am inexperienced in invoking kiss_fft. 
''')
rsf.doc.progs['sfmyradon2']=sfmyradon2

sfmpifwi = rsf.doc.rsfprog('sfmpifwi','user/pyang/Mmpifwi.c','''Time domain full waveform inversion using MPI parallel programming ''')
sfmpifwi.par('vinit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpifwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpifwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpifwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpifwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpifwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfmpifwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfmpifwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmpifwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfmpifwi.version('2.1-git')
sfmpifwi.synopsis('''sfmpifwi vinit=vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf illums=illums.rsf objs=objs.rsf verb=y precon=n niter=100 rbell=2''','''Note: 	Clayton-Enquist absorbing boundary condition (A2) is applied!
''')
rsf.doc.progs['sfmpifwi']=sfmpifwi

sffbrec = rsf.doc.rsfprog('sffbrec','user/pyang/Mfbrec.cu','''Forward-backword exact reconstruction using boundary saving''')
sffbrec.par('back',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffbrec.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sffbrec.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sffbrec.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sffbrec.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sffbrec.par('ns',rsf.doc.rsfpar('int','1','','''total shots '''))
sffbrec.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sffbrec.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sffbrec.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sffbrec.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sffbrec.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sffbrec.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sffbrec.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sffbrec.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sffbrec.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sffbrec.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sffbrec.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sffbrec.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sffbrec.version('2.1-git')
sffbrec.synopsis('''sffbrec < vinit.rsf > Fw1.rsf back=Fw2.rsf amp=1000 fm=10 dt= nt= ns=1 ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=y ft=0 jt=1''','''Note: It is used as a demonstration that we can reconstruct the modeled
wavefield exactly via boundary saving.
''')
rsf.doc.progs['sffbrec']=sffbrec

sfgpurtm = rsf.doc.rsfprog('sfgpurtm','user/pyang/Mgpurtm.cu','''2D prestack GPU-based RTM using effective boundary saving.''')
sfgpurtm.par('imag2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpurtm.par('fm',rsf.doc.rsfpar('float','','','''dominant freq of ricker '''))
sfgpurtm.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgpurtm.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgpurtm.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgpurtm.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgpurtm.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgpurtm.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgpurtm.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgpurtm.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgpurtm.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgpurtm.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgpurtm.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgpurtm.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgpurtm.par('order',rsf.doc.rsfpar('int','6','','''order of finite difference, order=2,4,6,8,10 '''))
sfgpurtm.par('phost',rsf.doc.rsfpar('float','0','','''phost% points on host with zero-copy pinned memory, the rest on device '''))
sfgpurtm.par('csdgather',rsf.doc.rsfpar('bool','y','','''default, common shot-gather; if n, record at every point'''))
sfgpurtm.par('vmute',rsf.doc.rsfpar('float','1500','','''muting velocity to remove the low-freq artifacts, unit=m/s'''))
sfgpurtm.par('tdmute',rsf.doc.rsfpar('int','2.0/(fm*dt)','','''number of deleyed time samples to mute '''))
sfgpurtm.version('2.1-git')
sfgpurtm.synopsis('''sfgpurtm < vmodl.rsf > imag1.rsf imag2=imag2.rsf fm= dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= order=6 phost=0 csdgather=y vmute=1500 tdmute=2.0/(fm*dt)''','''
Some basic descriptions of this code are in order.
1) Coordinate configuration of seismic data:

o--------------> x (2nd dim: *.y)
|
|
|
|
|
z (1st dim: *.x)
1st dim: i1=threadIdx.x+blockDim.x*blockIdx.x;
2nd dim: i2=threadIdx.y+blockDim.y*blockIdx.y;
(i1, i2)=i1+i2*nnz;

2) stability condition:	
min(dx, dz)>sqrt(2)*dt*max(v) (NJ=2)
numerical dispersion condition:	
max(dx, dz)<min(v)/(10*fmax)  (NJ=2)
max(dx, dz)<min(v)/(5*fmax)   (NJ=4)

3) This code doesn't save the history of forward time steps. We 
just save the least boundaries (referred to as effective boundary 
in our work) of every time step and the two final steps of the 
wavefield. Using this information, we can easily reconstruct 
the exact wavefield in the reverse time steps. It is noteworthy
that to implement large scale seismic imaging, pinned memory is 
employed to save the boundaries of each step so that all the saved
data can be computed on the device directly.

4) In our implementation, we employ staggered grid based 
convolutional PML (CPML) boundary condition. Using 20 points for 
CPML is enough to obtain perfect absorbing effect (while commonly 
used sponge ABC may need 30 or more). However, we use 32 points on
each side due to the grid alignment reasons. (To make your code 
fast, you should consider that the GPU codes implementation unit 
is half-warp (16 threads). The thickness of the boundary should be 
times of 16. 

5) The final images can be two kinds: result of correlation imaging 
condition and the normalized one. The normalized correlation imaging
result is preferred due to compensated illumination. Some filters 
are popular and effective to remove the low frequency artifacts of 
the imaging: the Laplacian filtering, derivative filtering and 
the bandpass filtering. In this code, we use laplacian filtering.
''')
rsf.doc.progs['sfgpurtm']=sfgpurtm

sfgpufwi = rsf.doc.rsfprog('sfgpufwi','user/pyang/Mgpufwi.cu','''CUDA based FWI using Enquist absorbing boundary condition (A2)''')
sfgpufwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpufwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgpufwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfgpufwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfgpufwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfgpufwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfgpufwi.version('2.1-git')
sfgpufwi.synopsis('''sfgpufwi < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf objs=objs.rsf illums=illums.rsf verb=y precon=n niter=100 rbell=2''','''
Note: You can try other complex boundary condition but we do not
recommend to do so. The main reason is that FWI is to recover
the low-frequency information of the earth model. Low-freq 
means that exact absorbing is not necessarilly needed. The 
result will be improved with the optimization precedure. 
Furthermore, complex boundary condition (such as sponge ABC or
PML) implies more computational cost, which will degrade the
efficiency of FWI. 
''')
rsf.doc.progs['sfgpufwi']=sfgpufwi

sfgenshots = rsf.doc.rsfprog('sfgenshots','user/pyang/Mgenshots.cu','''Generate shots for FWI using Enquist absorbing boundary condition''')
sfgenshots.par('time',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('check',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfgenshots.par('chk',rsf.doc.rsfpar('bool','n','','''check whether GPU-CPU implementation coincide with each other or not '''))
sfgenshots.par('kt',rsf.doc.rsfpar('int','100','','''check it at it=100 '''))
sfgenshots.par('amp',rsf.doc.rsfpar('float','1000','','''maximum amplitude of ricker '''))
sfgenshots.par('fm',rsf.doc.rsfpar('float','10','','''dominant freq of ricker '''))
sfgenshots.par('dt',rsf.doc.rsfpar('float','','','''time interval '''))
sfgenshots.par('nt',rsf.doc.rsfpar('int','','','''total modeling time steps '''))
sfgenshots.par('ns',rsf.doc.rsfpar('int','','','''total shots '''))
sfgenshots.par('ng',rsf.doc.rsfpar('int','','','''total receivers in each shot '''))
sfgenshots.par('jsx',rsf.doc.rsfpar('int','','','''source x-axis  jump interval  '''))
sfgenshots.par('jsz',rsf.doc.rsfpar('int','0','','''source z-axis jump interval  '''))
sfgenshots.par('jgx',rsf.doc.rsfpar('int','1','','''receiver x-axis jump interval '''))
sfgenshots.par('jgz',rsf.doc.rsfpar('int','0','','''receiver z-axis jump interval '''))
sfgenshots.par('sxbeg',rsf.doc.rsfpar('int','','','''x-begining index of sources, starting from 0 '''))
sfgenshots.par('szbeg',rsf.doc.rsfpar('int','','','''z-begining index of sources, starting from 0 '''))
sfgenshots.par('gxbeg',rsf.doc.rsfpar('int','','','''x-begining index of receivers, starting from 0 '''))
sfgenshots.par('gzbeg',rsf.doc.rsfpar('int','','','''z-begining index of receivers, starting from 0 '''))
sfgenshots.par('csdgather',rsf.doc.rsfpar('bool','n','','''default, common shot-gather; if n, record at every point'''))
sfgenshots.version('2.1-git')
sfgenshots.synopsis('''sfgenshots < vinit.rsf > shots.rsf time=time.rsf check=check.rsf chk=n kt=100 amp=1000 fm=10 dt= nt= ns= ng= jsx= jsz=0 jgx=1 jgz=0 sxbeg= szbeg= gxbeg= gzbeg= csdgather=n''','''
Note: You can try other complex boundary condition but we do not
recommend to do so. The main reason is that FWI is to recover
the low-frequency information of the earth model. Low-freq 
means that exact absorbing is not necessarilly needed. The 
result will be improved with the optimization procedure. 
Furthermore, complex boundary condition (such as sponge ABC or
PML) implies more computational cost, which will degrade the
efficiency of FWI. 
''')
rsf.doc.progs['sfgenshots']=sfgenshots

sfgpufd3d = rsf.doc.rsfprog('sfgpufd3d','user/pyang/Mgpufd3d.cu','''GPU-based finite difference on 3-D grid''')
sfgpufd3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosit2 '''))
sfgpufd3d.par('nt',rsf.doc.rsfpar('int','','','''total number of time steps '''))
sfgpufd3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfgpufd3d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfgpufd3d.par('fm',rsf.doc.rsfpar('float','20','','''dominant frequency of Ricker wavelet '''))
sfgpufd3d.par('ns',rsf.doc.rsfpar('int','1','','''number of sources '''))
sfgpufd3d.par('szbeg',rsf.doc.rsfpar('int','','','''source beginning of z-axis '''))
sfgpufd3d.par('sxbeg',rsf.doc.rsfpar('int','','','''source beginning of x-axis '''))
sfgpufd3d.par('sybeg',rsf.doc.rsfpar('int','','','''source beginning of y-axis '''))
sfgpufd3d.par('jsz',rsf.doc.rsfpar('int','','','''source jump interval in z-axis '''))
sfgpufd3d.par('jsx',rsf.doc.rsfpar('int','','','''source jump interval in x-axis '''))
sfgpufd3d.par('jsy',rsf.doc.rsfpar('int','','','''source jump interval in y-axis '''))
sfgpufd3d.version('2.1-git')
sfgpufd3d.synopsis('''sfgpufd3d < Fv.rsf > Fw.rsf verb=n nt= kt= dt= fm=20 ns=1 szbeg= sxbeg= sybeg= jsz= jsx= jsy=''','''''')
rsf.doc.progs['sfgpufd3d']=sfgpufd3d

sfgpufbrec3d = rsf.doc.rsfprog('sfgpufbrec3d','user/pyang/Mgpufbrec3d.cu','''Backward reconstruction of forward modeling with random boundary''')
sfgpufbrec3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfgpufbrec3d.par('nb',rsf.doc.rsfpar('int','20','','''thickness of random boundary '''))
sfgpufbrec3d.par('nt',rsf.doc.rsfpar('int','','','''total number of time steps '''))
sfgpufbrec3d.par('kt',rsf.doc.rsfpar('int','','','''record wavefield at time kt '''))
sfgpufbrec3d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfgpufbrec3d.par('fm',rsf.doc.rsfpar('float','20','','''dominant frequency of Ricker wavelet '''))
sfgpufbrec3d.par('ns',rsf.doc.rsfpar('int','1','','''number of sources '''))
sfgpufbrec3d.par('szbeg',rsf.doc.rsfpar('int','','','''source beginning of z-axis '''))
sfgpufbrec3d.par('sxbeg',rsf.doc.rsfpar('int','','','''source beginning of x-axis '''))
sfgpufbrec3d.par('sybeg',rsf.doc.rsfpar('int','','','''source beginning of y-axis '''))
sfgpufbrec3d.par('jsz',rsf.doc.rsfpar('int','','','''source jump interval in z-axis '''))
sfgpufbrec3d.par('jsx',rsf.doc.rsfpar('int','','','''source jump interval in x-axis '''))
sfgpufbrec3d.par('jsy',rsf.doc.rsfpar('int','','','''source jump interval in y-axis '''))
sfgpufbrec3d.version('2.1-git')
sfgpufbrec3d.synopsis('''sfgpufbrec3d < Fv.rsf > Fw.rsf verb=n nb=20 nt= kt= dt= fm=20 ns=1 szbeg= sxbeg= sybeg= jsz= jsx= jsy=''','''''')
rsf.doc.progs['sfgpufbrec3d']=sfgpufbrec3d

sfmpigpufwi = rsf.doc.rsfprog('sfmpigpufwi','user/pyang/Mmpigpufwi.cu','''CUDA based FWI using Enquist absorbing boundary condition''')
sfmpigpufwi.par('shots',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpigpufwi.par('grads',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('objs',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('illums',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpigpufwi.par('verb',rsf.doc.rsfpar('bool','y','','''vebosity '''))
sfmpigpufwi.par('precon',rsf.doc.rsfpar('bool','n','','''precondition or not '''))
sfmpigpufwi.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfmpigpufwi.par('rbell',rsf.doc.rsfpar('int','2','','''radius of bell smooth '''))
sfmpigpufwi.version('2.1-git')
sfmpigpufwi.synopsis('''sfmpigpufwi < vinit.rsf shots=shots.rsf > vupdates.rsf grads=grads.rsf objs=objs.rsf illums=illums.rsf verb=y precon=n niter=100 rbell=2''','''
Note: You can try other complex boundary condition but we do not
recommend to do so. The main reason is that FWI is to recover
the low-frequency information of the earth model. Low-freq 
means that exact absorbing is not necessarilly needed. The 
result will be improved with the optimization precedure. 
Furthermore, complex boundary condition (such as sponge ABC or
PML) implies more computational cost, which will degrade the
efficiency of FWI. 
''')
rsf.doc.progs['sfmpigpufwi']=sfmpigpufwi

