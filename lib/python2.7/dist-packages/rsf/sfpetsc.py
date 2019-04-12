import rsf.doc

sfaimplfd1 = rsf.doc.rsfprog('sfaimplfd1','user/petsc/Maimplfd1.c','''Implicit solution of 1-D acoustic wave equation. ''')
sfaimplfd1.par('src',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfaimplfd1.par('niter',rsf.doc.rsfpar('int','10','','''Number of solver iterations '''))
sfaimplfd1.par('src',rsf.doc.rsfpar('string ',desc='''Source wavelet (auxiliary input file name)'''))
sfaimplfd1.version('2.1-git')
sfaimplfd1.synopsis('''sfaimplfd1 < vel.rsf > usol.rsf src=src.rsf niter=10''','''''')
rsf.doc.progs['sfaimplfd1']=sfaimplfd1

sfaimplfd2 = rsf.doc.rsfprog('sfaimplfd2','user/petsc/Maimplfd2.c','''Implicit solution of 2-D acoustic wave equation. ''')
sfaimplfd2.par('src',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfaimplfd2.par('niter',rsf.doc.rsfpar('int','10','','''Number of solver iterations '''))
sfaimplfd2.par('fourth',rsf.doc.rsfpar('bool','y','','''Higher order flag '''))
sfaimplfd2.par('src',rsf.doc.rsfpar('string ',desc='''Source wavelet (auxiliary input file name)'''))
sfaimplfd2.version('2.1-git')
sfaimplfd2.synopsis('''sfaimplfd2 < vel.rsf > usol.rsf src=src.rsf niter=10 fourth=y''','''''')
rsf.doc.progs['sfaimplfd2']=sfaimplfd2

sfheatgmres1 = rsf.doc.rsfprog('sfheatgmres1','user/petsc/Mheatgmres1.c','''Solution of 1-D heat equation with GMRES. ''')
sfheatgmres1.par('alpha',rsf.doc.rsfpar('float','','','''Conductivity '''))
sfheatgmres1.par('dt',rsf.doc.rsfpar('float','','','''Time step '''))
sfheatgmres1.par('nt',rsf.doc.rsfpar('int','','','''Number of time steps '''))
sfheatgmres1.par('Ta',rsf.doc.rsfpar('float','0','','''Boundary condition on the left '''))
sfheatgmres1.par('Tb',rsf.doc.rsfpar('float','0','','''Boundary condition on the right '''))
sfheatgmres1.version('2.1-git')
sfheatgmres1.synopsis('''sfheatgmres1 < tinitial.rsf > solution.rsf alpha= dt= nt= Ta=0 Tb=0''','''''')
rsf.doc.progs['sfheatgmres1']=sfheatgmres1

sfpetscawefd2d = rsf.doc.rsfprog('sfpetscawefd2d','user/petsc/Mpetscawefd2d.c','''Implicit solution of 2-D acoustic wave equation, compatibility interface with sfawefd2d ''')
sfpetscawefd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpetscawefd2d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpetscawefd2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpetscawefd2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpetscawefd2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpetscawefd2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpetscawefd2d.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfpetscawefd2d.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfpetscawefd2d.par('expl',rsf.doc.rsfpar('bool','n','','''"exploding reflector" '''))
sfpetscawefd2d.par('dabc',rsf.doc.rsfpar('bool','n','','''absorbing BC '''))
sfpetscawefd2d.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfpetscawefd2d.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfpetscawefd2d.par('nqz',rsf.doc.rsfpar('int','sf_n (az)','',''''''))
sfpetscawefd2d.par('nqx',rsf.doc.rsfpar('int','sf_n (ax)','',''''''))
sfpetscawefd2d.par('oqz',rsf.doc.rsfpar('float','sf_o (az)','',''''''))
sfpetscawefd2d.par('oqx',rsf.doc.rsfpar('float','sf_o (ax)','',''''''))
sfpetscawefd2d.version('2.1-git')
sfpetscawefd2d.synopsis('''sfpetscawefd2d < Fwav.rsf vel=Fvel.rsf sou=Fsou.rsf rec=Frec.rsf wfl=Fwfl.rsf > Fdat.rsf den=Fden.rsf verb=n snap=n free=n expl=n dabc=n jdata=1 jsnap=nt nqz=sf_n (az) nqx=sf_n (ax) oqz=sf_o (az) oqx=sf_o (ax)''','''''')
rsf.doc.progs['sfpetscawefd2d']=sfpetscawefd2d

sfrtmgeompetsc = rsf.doc.rsfprog('sfrtmgeompetsc','user/petsc/Mrtmgeompetsc.c','''Rice HPCSS reverse time migration. ''')
sfrtmgeompetsc.version('2.1-git')
sfrtmgeompetsc.synopsis('''sfrtmgeompetsc''','''''')
rsf.doc.progs['sfrtmgeompetsc']=sfrtmgeompetsc

sfwavegeompetsc = rsf.doc.rsfprog('sfwavegeompetsc','user/petsc/Mwavegeompetsc.c','''Rice HPCSS forward modeling. ''')
sfwavegeompetsc.version('2.1-git')
sfwavegeompetsc.synopsis('''sfwavegeompetsc''','''''')
rsf.doc.progs['sfwavegeompetsc']=sfwavegeompetsc

