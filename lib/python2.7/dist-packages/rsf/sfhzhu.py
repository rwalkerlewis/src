import rsf.doc

sfhelm2D_forward = rsf.doc.rsfprog('sfhelm2D_forward','user/hzhu/Mhelm2D_forward.c','''2D Helmholtz forward solver by LU factorization. ''')
sfhelm2D_forward.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_forward.par('uts',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_forward.par('hermite',rsf.doc.rsfpar('bool','n','','''Hermite operator '''))
sfhelm2D_forward.par('npml',rsf.doc.rsfpar('int','20','','''PML width '''))
sfhelm2D_forward.par('order',rsf.doc.rsfpar('string ',desc='''discretization scheme (default optimal 9-point) '''))
sfhelm2D_forward.par('source',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_forward.version('2.1-git')
sfhelm2D_forward.synopsis('''sfhelm2D_forward < in.rsf > out.rsf source=source.rsf uts=0 hermite=n npml=20 order=''','''''')
rsf.doc.progs['sfhelm2D_forward']=sfhelm2D_forward

sfhelm2D_bornsyn = rsf.doc.rsfprog('sfhelm2D_bornsyn','user/hzhu/Mhelm2D_bornsyn.c','''2D Born synthetic based on Helmholtz forward solver. ''')
sfhelm2D_bornsyn.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_bornsyn.par('refl',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_bornsyn.par('uts',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_bornsyn.par('hermite',rsf.doc.rsfpar('bool','n','','''Hermite operator '''))
sfhelm2D_bornsyn.par('npml',rsf.doc.rsfpar('int','20','','''PML width '''))
sfhelm2D_bornsyn.par('order',rsf.doc.rsfpar('string ',desc='''discretization scheme (default optimal 9-point) '''))
sfhelm2D_bornsyn.par('source',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_bornsyn.par('refl',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_bornsyn.version('2.1-git')
sfhelm2D_bornsyn.synopsis('''sfhelm2D_bornsyn < in.rsf > out.rsf source=source.rsf refl=reflfile.rsf uts=0 hermite=n npml=20 order=''','''''')
rsf.doc.progs['sfhelm2D_bornsyn']=sfhelm2D_bornsyn

sfhelm2D_genshot = rsf.doc.rsfprog('sfhelm2D_genshot','user/hzhu/Mhelm2D_genshot.c','''Generate shot file for Helmholtz solver. ''')
sfhelm2D_genshot.par('fmag',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_genshot.par('n1',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genshot.par('n2',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genshot.par('ns',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genshot.par('d1',rsf.doc.rsfpar('float','0.1','',''''''))
sfhelm2D_genshot.par('d2',rsf.doc.rsfpar('float','0.1','',''''''))
sfhelm2D_genshot.par('nw',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genshot.par('dw',rsf.doc.rsfpar('float','1.0','',''''''))
sfhelm2D_genshot.par('ow',rsf.doc.rsfpar('float','1.0','',''''''))
sfhelm2D_genshot.par('nsource',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genshot.par('dsource',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_genshot.par('srcz',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genshot.par('srcx0',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genshot.par('srcdx',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genshot.par('mag',rsf.doc.rsfpar('float','1.0','',''''''))
sfhelm2D_genshot.par('fmag',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_genshot.version('2.1-git')
sfhelm2D_genshot.synopsis('''sfhelm2D_genshot > out.rsf fmag=fmag.rsf n1=1 n2=1 ns=1 d1=0.1 d2=0.1 nw=1 dw=1.0 ow=1.0 nsource=1 dsource=0 srcz= srcx0= srcdx= mag=1.0''','''''')
rsf.doc.progs['sfhelm2D_genshot']=sfhelm2D_genshot

sfhelm2D_genrec = rsf.doc.rsfprog('sfhelm2D_genrec','user/hzhu/Mhelm2D_genrec.c','''Generate receiver file for Helmholtz solver. ''')
sfhelm2D_genrec.par('n1',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genrec.par('n2',rsf.doc.rsfpar('int','1','',''''''))
sfhelm2D_genrec.par('d1',rsf.doc.rsfpar('float','0.1','',''''''))
sfhelm2D_genrec.par('d2',rsf.doc.rsfpar('float','0.1','',''''''))
sfhelm2D_genrec.par('recz',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genrec.par('recx0',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genrec.par('recdx',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_genrec.version('2.1-git')
sfhelm2D_genrec.synopsis('''sfhelm2D_genrec > out.rsf n1=1 n2=1 d1=0.1 d2=0.1 recz= recx0= recdx=''','''''')
rsf.doc.progs['sfhelm2D_genrec']=sfhelm2D_genrec

sfhelm2D_rtm = rsf.doc.rsfprog('sfhelm2D_rtm','user/hzhu/Mhelm2D_rtm.c','''2D Frequency Domain Reverse Time Migration. ''')
sfhelm2D_rtm.par('receiver',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.par('record',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.par('nh',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_rtm.par('uts',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_rtm.par('npml',rsf.doc.rsfpar('int','20','','''PML width '''))
sfhelm2D_rtm.par('order',rsf.doc.rsfpar('string ',desc='''discretization scheme (default optimal 9-point) '''))
sfhelm2D_rtm.par('receiver',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.par('source',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.par('record',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_rtm.version('2.1-git')
sfhelm2D_rtm.synopsis('''sfhelm2D_rtm < in.rsf > out.rsf receiver=receiver.rsf source=source.rsf record=record.rsf nh=0 uts=0 npml=20 order=''','''''')
rsf.doc.progs['sfhelm2D_rtm']=sfhelm2D_rtm

sfhelm2D_lsm = rsf.doc.rsfprog('sfhelm2D_lsm','user/hzhu/Mhelm2D_lsm.c','''2D Frequency Domain Least Squares Reverse Time Migration. ''')
sfhelm2D_lsm.par('misfit',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfhelm2D_lsm.par('receiver',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.par('record',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.par('uts',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_lsm.par('npml',rsf.doc.rsfpar('int','20','','''PML width '''))
sfhelm2D_lsm.par('niter',rsf.doc.rsfpar('int','0','','''Number of iterations '''))
sfhelm2D_lsm.par('order',rsf.doc.rsfpar('string ',desc='''discretization scheme (default optimal 9-point) '''))
sfhelm2D_lsm.par('receiver',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.par('source',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.par('record',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_lsm.version('2.1-git')
sfhelm2D_lsm.synopsis('''sfhelm2D_lsm < in.rsf > out.rsf misfit=misfit.rsf receiver=receiver.rsf source=source.rsf record=record.rsf uts=0 npml=20 niter=0 order=''','''''')
rsf.doc.progs['sfhelm2D_lsm']=sfhelm2D_lsm

sfhelm2D_fwi = rsf.doc.rsfprog('sfhelm2D_fwi','user/hzhu/Mhelm2D_fwi.c','''2D Frequency Domain Full Waveform Inversion. ''')
sfhelm2D_fwi.par('receiver',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('source',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('record',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('niter',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_fwi.par('uts',rsf.doc.rsfpar('int','0','',''''''))
sfhelm2D_fwi.par('npml',rsf.doc.rsfpar('int','20','','''PML width '''))
sfhelm2D_fwi.par('precond',rsf.doc.rsfpar('bool','n','',''''''))
sfhelm2D_fwi.par('radius',rsf.doc.rsfpar('int','','',''''''))
sfhelm2D_fwi.par('order',rsf.doc.rsfpar('string ',desc='''discretization scheme (default optimal 9-point) '''))
sfhelm2D_fwi.par('receiver',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('source',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('record',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.par('dip',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfhelm2D_fwi.version('2.1-git')
sfhelm2D_fwi.synopsis('''sfhelm2D_fwi < in.rsf > out.rsf receiver=receiver.rsf source=source.rsf record=record.rsf dip=dip.rsf niter=0 uts=0 npml=20 precond=n radius= order=''','''''')
rsf.doc.progs['sfhelm2D_fwi']=sfhelm2D_fwi

