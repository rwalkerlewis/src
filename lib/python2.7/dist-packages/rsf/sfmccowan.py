import rsf.doc

sfdmeig = rsf.doc.rsfprog('sfdmeig','user/mccowan/Mdmeig.c','''Find eigenvalues and eigenvectors of an spd matrix. ''')
sfdmeig.par('eval',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfdmeig.version('2.1-git')
sfdmeig.synopsis('''sfdmeig < mat.rsf eval=evals.rsf > evecs.rsf''','''''')
rsf.doc.progs['sfdmeig']=sfdmeig

sffastft = rsf.doc.rsfprog('sffastft','user/mccowan/Mfastft.c','''Fast Fourier Transform. ''')
sffastft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sffastft.version('2.1-git')
sffastft.synopsis('''sffastft < in.rsf > out.rsf inv=n''','''''')
rsf.doc.progs['sffastft']=sffastft

sfkernel = rsf.doc.rsfprog('sfkernel','user/mccowan/Mkernel.c','''Test migration kernel. ''')
sfkernel.par('ncalls',rsf.doc.rsfpar('int','5000','','''number of calls '''))
sfkernel.version('2.1-git')
sfkernel.synopsis('''sfkernel ncalls=5000''','''''')
rsf.doc.progs['sfkernel']=sfkernel

