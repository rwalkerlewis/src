import rsf.doc

sfeasypath = rsf.doc.rsfprog('sfeasypath','user/zgeng/Measypath.c','''Finding the easy path ''')
sfeasypath.version('2.1-git')
sfeasypath.synopsis('''sfeasypath < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfeasypath']=sfeasypath

sfreorder = rsf.doc.rsfprog('sfreorder','user/zgeng/Mreorder.c','''Reorder the data according to the path ''')
sfreorder.par('path',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfreorder.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfreorder.version('2.1-git')
sfreorder.synopsis('''sfreorder < in.rsf path=path.rsf > out.rsf inv=n''','''''')
rsf.doc.progs['sfreorder']=sfreorder

sfseisletrgt = rsf.doc.rsfprog('sfseisletrgt','user/zgeng/Mseisletrgt.c','''Seislet transform using rgt ''')
sfseisletrgt.par('rgt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseisletrgt.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfseisletrgt.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfseisletrgt.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseisletrgt.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfseisletrgt.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseisletrgt.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseisletrgt.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseisletrgt.version('2.1-git')
sfseisletrgt.synopsis('''sfseisletrgt < in.rsf > out.rsf rgt=rgt.rsf inv=n adj=n eps=0.01 unit=n order=1 verb=n type=''','''''')
rsf.doc.progs['sfseisletrgt']=sfseisletrgt

sfshifts2 = rsf.doc.rsfprog('sfshifts2','user/zgeng/Mshifts2.c','''Apply linear time shifts on multiple traces. ''')
sfshifts2.par('s0',rsf.doc.rsfpar('int','','','''first shift (in number of samples along 1st axis) '''))
sfshifts2.par('ds',rsf.doc.rsfpar('int','','','''shift sampling '''))
sfshifts2.version('2.1-git')
sfshifts2.synopsis('''sfshifts2 < in.rsf > shift.rsf s0= ds=''','''''')
rsf.doc.progs['sfshifts2']=sfshifts2

