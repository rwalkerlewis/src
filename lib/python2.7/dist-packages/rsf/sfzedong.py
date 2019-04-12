import rsf.doc

sfisolr25 = rsf.doc.rsfprog('sfisolr25','user/zedong/Misolr25.cc','''Lowrank decomposition for 2-D isotropic wave propagation. ''')
sfisolr25.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr25.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr25.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr25.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr25.par('stablecoef',rsf.doc.rsfpar('','0','','''tolerance'''))
sfisolr25.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr25.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr25.version('2.1-git')
sfisolr25.synopsis('''sfisolr25 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 stablecoef=0 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr25']=sfisolr25

