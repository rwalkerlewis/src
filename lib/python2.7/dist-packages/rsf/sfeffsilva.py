import rsf.doc

sfkhshot = rsf.doc.rsfprog('sfkhshot','user/effsilva/Mkhshot.c','''Kirchhoff shot migration ''')
sfkhshot.par('ttfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfkhshot.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfkhshot.par('theta',rsf.doc.rsfpar('float','30.','','''maximum dip '''))
sfkhshot.par('dtheta',rsf.doc.rsfpar('float','theta/3','','''taper zone '''))
sfkhshot.par('df',rsf.doc.rsfpar('float','5.','','''anti-aliasing sampling '''))
sfkhshot.par('fmax',rsf.doc.rsfpar('float','.5/d1','',''''''))
sfkhshot.par('ntaper',rsf.doc.rsfpar('int','11','',''''''))
sfkhshot.par('tmin',rsf.doc.rsfpar('float','3*d1','',''''''))
sfkhshot.par('xs',rsf.doc.rsfpar('float','','','''image parameters '''))
sfkhshot.par('nx',rsf.doc.rsfpar('int','n2t','',''''''))
sfkhshot.par('ox',rsf.doc.rsfpar('float','o2t','',''''''))
sfkhshot.par('dx',rsf.doc.rsfpar('float','d2t','',''''''))
sfkhshot.par('nz',rsf.doc.rsfpar('int','n1t','',''''''))
sfkhshot.par('oz',rsf.doc.rsfpar('float','o1t','',''''''))
sfkhshot.par('dz',rsf.doc.rsfpar('float','d1t','','''checking dimensions '''))
sfkhshot.version('2.1-git')
sfkhshot.synopsis('''sfkhshot < Fin.rsf > Fout.rsf ttfile=Ftt.rsf verb=n theta=30. dtheta=theta/3 df=5. fmax=.5/d1 ntaper=11 tmin=3*d1 xs= nx=n2t ox=o2t dx=d2t nz=n1t oz=o1t dz=d1t''','''''')
rsf.doc.progs['sfkhshot']=sfkhshot

