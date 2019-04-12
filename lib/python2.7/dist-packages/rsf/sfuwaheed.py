import rsf.doc

sffacttieikonal = rsf.doc.rsfprog('sffacttieikonal','user/uwaheed/Mfacttieikonal.c','''Fast sweeping factored TTI eikonal solver (2D) ''')
sffacttieikonal.par('niter',rsf.doc.rsfpar('int','4','','''number of sweeping iterations '''))
sffacttieikonal.par('nfpi',rsf.doc.rsfpar('int','3','','''number of fixed-point iterations '''))
sffacttieikonal.par('fac',rsf.doc.rsfpar('int','1','','''Type of factorization: (0)Additive, (1)Multiplicative '''))
sffacttieikonal.par('optloc',rsf.doc.rsfpar('bool','n','','''Selects optimal location for homogeneous medium parameter '''))
sffacttieikonal.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sffacttieikonal.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sffacttieikonal.par('epsilon',rsf.doc.rsfpar('string ',desc=''''''))
sffacttieikonal.par('delta',rsf.doc.rsfpar('string ',desc=''''''))
sffacttieikonal.par('theta',rsf.doc.rsfpar('string ',desc=''''''))
sffacttieikonal.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) '''))
sffacttieikonal.version('2.1-git')
sffacttieikonal.synopsis('''sffacttieikonal < vzf.rsf > time.rsf niter=4 nfpi=3 fac=1 optloc=n zshot=0. yshot=o2 + 0.5*(n2-1)*d2 epsilon= delta= theta= shotfile=''','''''')
rsf.doc.progs['sffacttieikonal']=sffacttieikonal

sfttieikonal = rsf.doc.rsfprog('sfttieikonal','user/uwaheed/Mttieikonal.c','''Fast sweeping TTI eikonal solver (2D) ''')
sfttieikonal.par('niter',rsf.doc.rsfpar('int','4','','''number of sweeping iterations '''))
sfttieikonal.par('nfpi',rsf.doc.rsfpar('int','3','','''number of fixed-point iterations '''))
sfttieikonal.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfttieikonal.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfttieikonal.par('epsilon',rsf.doc.rsfpar('string ',desc=''''''))
sfttieikonal.par('delta',rsf.doc.rsfpar('string ',desc=''''''))
sfttieikonal.par('theta',rsf.doc.rsfpar('string ',desc=''''''))
sfttieikonal.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) '''))
sfttieikonal.version('2.1-git')
sfttieikonal.synopsis('''sfttieikonal < vzf.rsf > time.rsf niter=4 nfpi=3 zshot=0. yshot=o2 + 0.5*(n2-1)*d2 epsilon= delta= theta= shotfile=''','''''')
rsf.doc.progs['sfttieikonal']=sfttieikonal

