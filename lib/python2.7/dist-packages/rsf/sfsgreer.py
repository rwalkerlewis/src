import rsf.doc

sfradius = rsf.doc.rsfprog('sfradius','user/sgreer/Mradius.c','''Estimate smoothing radius (min = 1) ''')
sfradius.par('freq',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfradius.par('c',rsf.doc.rsfpar('float','1.','',''''''))
sfradius.par('maxrad',rsf.doc.rsfpar('float','1000.','',''''''))
sfradius.version('2.1-git')
sfradius.synopsis('''sfradius < in.rsf freq=freq.rsf > out.rsf c=1. maxrad=1000.''','''''')
rsf.doc.progs['sfradius']=sfradius

