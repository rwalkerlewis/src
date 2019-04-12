import rsf.doc

sfbackdireazi = rsf.doc.rsfprog('sfbackdireazi','user/parvaneh/Mbackdireazi.c','''Background directivity(Azimuth). ''')
sfbackdireazi.par('verb',rsf.doc.rsfpar('bool','0','',''''''))
sfbackdireazi.version('2.1-git')
sfbackdireazi.synopsis('''sfbackdireazi < Zz.rsf > Zo.rsf verb=0''','''''')
rsf.doc.progs['sfbackdireazi']=sfbackdireazi

sfbackdire = rsf.doc.rsfprog('sfbackdire','user/parvaneh/Mbackdire.c','''Background directivity(Dip). ''')
sfbackdire.par('verb',rsf.doc.rsfpar('bool','0','',''''''))
sfbackdire.version('2.1-git')
sfbackdire.synopsis('''sfbackdire < Zz.rsf > Zo.rsf verb=0''','''''')
rsf.doc.progs['sfbackdire']=sfbackdire

sfcurvature = rsf.doc.rsfprog('sfcurvature','user/parvaneh/Mcurvature.c','''Curvature ''')
sfcurvature.par('rotation',rsf.doc.rsfpar('bool','n','','''if y: rotation, if n: convergence '''))
sfcurvature.par('scale',rsf.doc.rsfpar('float','1.0','','''scaling (from time to depth) '''))
sfcurvature.par('vscale',rsf.doc.rsfpar('float','1.0','','''scaling (from time to depth) '''))
sfcurvature.par('what',rsf.doc.rsfpar('string ',desc='''what to compute '''))
sfcurvature.version('2.1-git')
sfcurvature.synopsis('''sfcurvature < hor.rsf > cur.rsf rotation=n scale=1.0 vscale=1.0 what=''','''''')
rsf.doc.progs['sfcurvature']=sfcurvature

sfshuffle2 = rsf.doc.rsfprog('sfshuffle2','user/parvaneh/Mshuffle2.c','''Shuffling an array ''')
sfshuffle2.par('iteration',rsf.doc.rsfpar('int','1','',''''''))
sfshuffle2.par('seed',rsf.doc.rsfpar('int','2012','',''''''))
sfshuffle2.version('2.1-git')
sfshuffle2.synopsis('''sfshuffle2 < bshuffle.rsf > ashuffle.rsf iteration=1 seed=2012''','''''')
rsf.doc.progs['sfshuffle2']=sfshuffle2

sfstcurvature = rsf.doc.rsfprog('sfstcurvature','user/parvaneh/Mstcurvature.c','''Curvature in stratigraphic coordinates ''')
sfstcurvature.par('yh',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstcurvature.par('zh',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstcurvature.par('scale',rsf.doc.rsfpar('float','1.0','','''scaling (from time to depth) '''))
sfstcurvature.par('what',rsf.doc.rsfpar('string ',desc='''what to compute '''))
sfstcurvature.version('2.1-git')
sfstcurvature.synopsis('''sfstcurvature < xhor.rsf yh=yhor.rsf zh=zhor.rsf > cur.rsf scale=1.0 what=''','''''')
rsf.doc.progs['sfstcurvature']=sfstcurvature

