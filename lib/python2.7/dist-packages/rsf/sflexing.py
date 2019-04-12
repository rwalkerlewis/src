import rsf.doc

sfclrmatrix = rsf.doc.rsfprog('sfclrmatrix','user/lexing/Mclrmatrix.cc','''Lowrank matrix decomposition for a complex matrix''')
sfclrmatrix.par('name',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfclrmatrix.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfclrmatrix.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfclrmatrix.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfclrmatrix.version('2.1-git')
sfclrmatrix.synopsis('''sfclrmatrix name=mfile.rsf < in.rsf > out.rsf seed=time(NULL eps=1.e-4 npk=20''','''''')
rsf.doc.progs['sfclrmatrix']=sfclrmatrix

sflrmatrix = rsf.doc.rsfprog('sflrmatrix','user/lexing/Mlrmatrix.cc','''Lowrank matrix decomposition''')
sflrmatrix.par('name',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflrmatrix.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sflrmatrix.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sflrmatrix.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sflrmatrix.par('outputs',rsf.doc.rsfpar('','2','','''number of outputs (2 or 3)'''))
sflrmatrix.version('2.1-git')
sflrmatrix.synopsis('''sflrmatrix name=mfile.rsf < in.rsf > out.rsf seed=time(NULL eps=1.e-4 npk=20 outputs=2''','''''')
rsf.doc.progs['sflrmatrix']=sflrmatrix

