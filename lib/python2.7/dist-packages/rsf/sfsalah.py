import rsf.doc

sfshotequal = rsf.doc.rsfprog('sfshotequal','user/salah/Mshotequal.c','''sfshotequal projects amplitudes of each shot to Z-score distribution''')
sfshotequal.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshotequal.par('scaler',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshotequal.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfshotequal.par('amp',rsf.doc.rsfpar('float','','','''Exclude amplitudes greater than amp && less than -amp for statistics computations'''))
sfshotequal.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfshotequal.par('scaler',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfshotequal.version('2.1-git')
sfshotequal.synopsis('''sfshotequal < in.rsf > out.rsf mask=msk.rsf scaler=scl.rsf verb=n amp=''','''''')
rsf.doc.progs['sfshotequal']=sfshotequal

sfrsf2handvel = rsf.doc.rsfprog('sfrsf2handvel','user/salah/Mrsf2handvel.c','''Convert RSF to velocity picks ''')
sfrsf2handvel.par('skip',rsf.doc.rsfpar('int','4','','''number of distance bins '''))
sfrsf2handvel.version('2.1-git')
sfrsf2handvel.synopsis('''sfrsf2handvel < in.rsf > out.rsf skip=4''','''''')
rsf.doc.progs['sfrsf2handvel']=sfrsf2handvel

sfhandvel2rsf = rsf.doc.rsfprog('sfhandvel2rsf','user/salah/Mhandvel2rsf.py','''Converts 2D/3D velocity files from handvel.txt to handvel.rsf''')
sfhandvel2rsf.par('n1',rsf.doc.rsfpar('int','','','''size of the first axis'''))
sfhandvel2rsf.par('o1',rsf.doc.rsfpar('float','','','''origin of the first axis'''))
sfhandvel2rsf.par('d1',rsf.doc.rsfpar('float','','','''sampling in the first axis'''))
sfhandvel2rsf.version('2.1-git')
sfhandvel2rsf.synopsis('''sfhandvel2rsf n1= o1= d1=''','''
- sfhandvel2rsf < handvels.txt o1=0 d1=.001 n1=3000 > handvel.rsf

- The program converts time samples from ms to s

- The rsf output file will have traces equal to the number
of CMP locations in handvel.txt. You need to interploate
between traces for a denser grid e.g. using sfremap1

- This program uses sfspline for interpolation. 

''')
rsf.doc.progs['sfhandvel2rsf']=sfhandvel2rsf

