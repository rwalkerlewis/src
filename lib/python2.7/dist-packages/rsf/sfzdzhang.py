import rsf.doc

sfhelloworld = rsf.doc.rsfprog('sfhelloworld','user/zdzhang/Mhelloworld.f90','''None''')
sfhelloworld.version('2.1-git')
sfhelloworld.synopsis('''sfhelloworld''','''''')
rsf.doc.progs['sfhelloworld']=sfhelloworld

sfintv2rms = rsf.doc.rsfprog('sfintv2rms','user/zdzhang/Mintv2rms.f90','''None''')
sfintv2rms.version('2.1-git')
sfintv2rms.synopsis('''sfintv2rms < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfintv2rms']=sfintv2rms

sfintv2avg = rsf.doc.rsfprog('sfintv2avg','user/zdzhang/Mintv2avg.f90','''None''')
sfintv2avg.version('2.1-git')
sfintv2avg.synopsis('''sfintv2avg < in.rsf > out.rsf''','''''')
rsf.doc.progs['sfintv2avg']=sfintv2avg

sffindmaximum = rsf.doc.rsfprog('sffindmaximum','user/zdzhang/Mfindmaximum.f90','''None''')
sffindmaximum.version('2.1-git')
sffindmaximum.synopsis('''sffindmaximum < in.rsf > out.rsf''','''''')
rsf.doc.progs['sffindmaximum']=sffindmaximum

sffdac2d = rsf.doc.rsfprog('sffdac2d','user/zdzhang/Mfdac2d.f90','''None''')
sffdac2d.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffdac2d.par('glo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffdac2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffdac2d.par('wavelet',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffdac2d.par('frec',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffdac2d.par('verb',rsf.doc.rsfpar('','y','',''''''))
sffdac2d.par('npml',rsf.doc.rsfpar('','','','''Grid points for PML'''))
sffdac2d.par('nthreads',rsf.doc.rsfpar('','','','''Threads for OMP'''))
sffdac2d.version('2.1-git')
sffdac2d.synopsis('''sffdac2d slo=Fslo.rsf glo=Fglo.rsf vel=Fvel.rsf wavelet=Fwav.rsf frec=Frec.rsf verb=y npml= nthreads=''','''''')
rsf.doc.progs['sffdac2d']=sffdac2d

