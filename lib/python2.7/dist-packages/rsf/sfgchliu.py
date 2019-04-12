import rsf.doc

sfpwshapeic = rsf.doc.rsfprog('sfpwshapeic','user/gchliu/Mpwshapeic.c','''Least Square Imaging condition using structure-based shaping regularization.''')
sfpwshapeic.par('down',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwshapeic.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwshapeic.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwshapeic.par('rect1',rsf.doc.rsfpar('int','3','',''''''))
sfpwshapeic.par('rect2',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfpwshapeic.par('lam',rsf.doc.rsfpar('float','1.','','''operator scaling for inversion '''))
sfpwshapeic.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwshapeic.par('niter',rsf.doc.rsfpar('int','100','','''maximum number of iterations '''))
sfpwshapeic.version('2.1-git Mdixshape.c 1131 2005-04-20 18:19:10Z fomels')
sfpwshapeic.synopsis('''sfpwshapeic < upgw.rsf > refl.rsf down=dwgw.rsf weight=weight.rsf dip=dip.rsf rect1=3 rect2=3 lam=1. order=1 niter=100 rect1= rect2= ...''','''rectN defines the size of the smoothing stencil in N-th dimension.
''')
rsf.doc.progs['sfpwshapeic']=sfpwshapeic

sfpwic = rsf.doc.rsfprog('sfpwic','user/gchliu/Mpwic.c','''Least square imaging condition with pwc regularization. ''')
sfpwic.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwic.par('down',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwic.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpwic.par('sparse',rsf.doc.rsfpar('bool','y','','''if sparse = ture   sparse deconvolution cauchy-norm
          if reg = 0: regularization A = |I|
          if reg = 1:  regularization A = |PWD|
       if sparse = false  2-norn deconvolution regularization A = ||I||
    '''))
sfpwic.par('reg',rsf.doc.rsfpar('int','0','','''cut off value of precondition '''))
sfpwic.par('cut_p',rsf.doc.rsfpar('bool','n','','''cut off value of precondition '''))
sfpwic.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfpwic.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfpwic.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfpwic.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfpwic.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwic.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpwic.version('2.1-git')
sfpwic.synopsis('''sfpwic < in.rsf dips=dips.rsf down=down.rsf > out.rsf weight=weight.rsf sparse=y reg=0 cut_p=n niter=50 nliter=1 eps=0. verb=y order=1''','''
''')
rsf.doc.progs['sfpwic']=sfpwic

sfpwdecon = rsf.doc.rsfprog('sfpwdecon','user/gchliu/Mpwdecon.c','''Deconvolution with known wavelelt using pwc to control sparsity. ''')
sfpwdecon.par('dips',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwdecon.par('wav',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwdecon.par('weight',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpwdecon.par('sparse',rsf.doc.rsfpar('bool','y','','''if sparse = ture   sparse deconvolution cauchy-norm
          if reg = 0: regularization A = |I|
          if reg = 1:  regularization A = |PWD|
       if sparse = false  2-norn deconvolution regularization A = ||I||
    '''))
sfpwdecon.par('reg',rsf.doc.rsfpar('int','0','','''cut off value of precondition '''))
sfpwdecon.par('cut_p',rsf.doc.rsfpar('bool','y','','''cut off value of precondition '''))
sfpwdecon.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwdecon.par('niter',rsf.doc.rsfpar('int','50','','''maximum number of iterations '''))
sfpwdecon.par('nliter',rsf.doc.rsfpar('int','1','','''number of reweighting iterations '''))
sfpwdecon.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfpwdecon.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfpwdecon.par('weight',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfpwdecon.version('2.1-git')
sfpwdecon.synopsis('''sfpwdecon < in.rsf dips=dips.rsf wav=wav.rsf > out.rsf weight=weight.rsf sparse=y reg=0 cut_p=y order=1 niter=50 nliter=1 eps=0. verb=y''','''
''')
rsf.doc.progs['sfpwdecon']=sfpwdecon

sfsmstack = rsf.doc.rsfprog('sfsmstack','user/gchliu/Msmstack.c','''Stack a dataset over the second dimensions by smart stacking. ''')
sfsmstack.par('s',rsf.doc.rsfpar('int','1','','''exponent'''))
sfsmstack.par('l',rsf.doc.rsfpar('int','0','','''parameter for alpha-trimmed mean '''))
sfsmstack.par('ifwt',rsf.doc.rsfpar('bool','y','',''''''))
sfsmstack.par('esp',rsf.doc.rsfpar('float','1e-10','',''''''))
sfsmstack.version('2.1-git')
sfsmstack.synopsis('''sfsmstack < in.rsf > out.rsf s=1 l=0 ifwt=y esp=1e-10''','''''')
rsf.doc.progs['sfsmstack']=sfsmstack

sfsnrstack = rsf.doc.rsfprog('sfsnrstack','user/gchliu/Msnrstack.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfsnrstack.par('w',rsf.doc.rsfpar('int','50','','''sliding window size'''))
sfsnrstack.par('sft',rsf.doc.rsfpar('float','1','','''weight shift'''))
sfsnrstack.par('ee',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.par('esp',rsf.doc.rsfpar('float','1.0','',''''''))
sfsnrstack.version('2.1-git')
sfsnrstack.synopsis('''sfsnrstack < in.rsf > out.rsf w=50 sft=1 ee=1.0 esp=1.0''','''''')
rsf.doc.progs['sfsnrstack']=sfsnrstack

sfwcorr = rsf.doc.rsfprog('sfwcorr','user/gchliu/Mwcorr.c','''Stack a dataset over the second dimensions by SNR weighted method. ''')
sfwcorr.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwcorr.par('w',rsf.doc.rsfpar('int','50','','''size of window'''))
sfwcorr.par('eps',rsf.doc.rsfpar('float','0','','''stable parameter'''))
sfwcorr.version('2.1-git')
sfwcorr.synopsis('''sfwcorr < in.rsf other=other.rsf > out.rsf w=50 eps=0''','''''')
rsf.doc.progs['sfwcorr']=sfwcorr

sfshiftd2 = rsf.doc.rsfprog('sfshiftd2','user/gchliu/Mshiftd2.c','''Generate shifts for 1-D regularized autoregression double sides (include the trace self for 3D shifts). ''')
sfshiftd2.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd2.version('2.1-git')
sfshiftd2.synopsis('''sfshiftd2 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd2']=sfshiftd2

sfshiftd1 = rsf.doc.rsfprog('sfshiftd1','user/gchliu/Mshiftd1.c','''Generate shifts for 1-D regularized autoregression double sides (not include the trace self). ''')
sfshiftd1.par('ns',rsf.doc.rsfpar('int','','','''number of shifts '''))
sfshiftd1.version('2.1-git')
sfshiftd1.synopsis('''sfshiftd1 < in.rsf > shift.rsf ns=''','''''')
rsf.doc.progs['sfshiftd1']=sfshiftd1

sfcshifts2 = rsf.doc.rsfprog('sfcshifts2','user/gchliu/Mcshifts2.c','''Generate shifts for 2-D regularized autoregression in complex domain. From (x,y,f) to (x,y,s,f) ''')
sfcshifts2.par('ns1',rsf.doc.rsfpar('int','','','''number of shifts in first dim '''))
sfcshifts2.par('ns2',rsf.doc.rsfpar('int','','','''number of shifts in second dim '''))
sfcshifts2.version('2.1-git')
sfcshifts2.synopsis('''sfcshifts2 < in.rsf > shifts.rsf ns1= ns2=''','''''')
rsf.doc.progs['sfcshifts2']=sfcshifts2

sfnfmiss = rsf.doc.rsfprog('sfnfmiss','user/gchliu/Mnfmiss.c','''Missing data interpolation in freq domain. ''')
sfnfmiss.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnfmiss.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnfmiss.par('exact',rsf.doc.rsfpar('bool','y','','''If y, preserve the known data values '''))
sfnfmiss.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfnfmiss.par('niter',rsf.doc.rsfpar('int','n1','','''number of iterations '''))
sfnfmiss.par('ty',rsf.doc.rsfpar('string ',desc='''Prediction type: all=backward+forward'''))
sfnfmiss.par('mask',rsf.doc.rsfpar('string ',desc='''optional input mask file for known data (auxiliary input file name)'''))
sfnfmiss.version('2.1-git Mmiss1.c 7107 2011-04-10 02:04:14Z ivlad')
sfnfmiss.synopsis('''sfnfmiss < in.rsf > out.rsf filt=filt.rsf mask=mask.rsf exact=y verb=n niter=n1 ty=''','''''')
rsf.doc.progs['sfnfmiss']=sfnfmiss

sffxrna = rsf.doc.rsfprog('sffxrna','user/gchliu/Mfxrna.c','''Local prediction filter for complex numbers (n-dimensional). ''')
sffxrna.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffxrna.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffxrna.par('zshift',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffxrna.par('zdata',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffxrna.par('ns',rsf.doc.rsfpar('int','1','','''shifts of both sides npef=2*ns+1'''))
sffxrna.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffxrna.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffxrna.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffxrna.par('ty',rsf.doc.rsfpar('string ',desc='''Prediction type: all=backward+forward'''))
sffxrna.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffxrna.par('zshift',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffxrna.par('zdata',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sffxrna.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sffxrna.version('2.1-git')
sffxrna.synopsis('''sffxrna < dat.rsf > flt.rsf mask=mask.rsf pred=pre.rsf zshift=zshift.rsf zdata=zdata.rsf ns=1 niter=100 verb=y ty=''','''''')
rsf.doc.progs['sffxrna']=sffxrna

sfcmatmult3 = rsf.doc.rsfprog('sfcmatmult3','user/gchliu/Mcmatmult3.c','''Multiplication of two complex matrices for 3D data.''')
sfcmatmult3.par('mat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcmatmult3.version('2.1-git')
sfcmatmult3.synopsis('''sfcmatmult3 < in.rsf > out.rsf mat=mat.rsf''','''I(n1,n2,f)*I(n2,n3,f)=D(n1,n3,f)
''')
rsf.doc.progs['sfcmatmult3']=sfcmatmult3

sfrfxrna = rsf.doc.rsfprog('sfrfxrna','user/gchliu/Mrfxrna.c','''Local prediction filter for complex numbers (n-dimensional). ''')
sfrfxrna.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrfxrna.par('pred',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrfxrna.par('zshift',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrfxrna.par('zdata',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrfxrna.par('ns',rsf.doc.rsfpar('int','1','','''shifts of both sides npef=2*ns+1'''))
sfrfxrna.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfrfxrna.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sfrfxrna.par('jump',rsf.doc.rsfpar('int','1','','''jump '''))
sfrfxrna.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfrfxrna.par('ty',rsf.doc.rsfpar('string ',desc='''Prediction type: all=backward+forward'''))
sfrfxrna.par('pred',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfrfxrna.par('zshift',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfrfxrna.par('zdata',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfrfxrna.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfrfxrna.version('2.1-git')
sfrfxrna.synopsis('''sfrfxrna < dat.rsf > flt.rsf mask=mask.rsf pred=pre.rsf zshift=zshift.rsf zdata=zdata.rsf ns=1 niter=100 verb=y jump=1 ty=''','''''')
rsf.doc.progs['sfrfxrna']=sfrfxrna

