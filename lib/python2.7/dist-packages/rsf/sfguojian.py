import rsf.doc

sfisoimpulse = rsf.doc.rsfprog('sfisoimpulse','user/guojian/Misoimpulse.c','''Impulse response for plane-wave migration in tilted coordinates ''')
sfisoimpulse.par('wave',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisoimpulse.par('t',rsf.doc.rsfpar('float','0.8','',''''''))
sfisoimpulse.par('ep',rsf.doc.rsfpar('float','0.4','',''''''))
sfisoimpulse.par('dl',rsf.doc.rsfpar('float','0.2','',''''''))
sfisoimpulse.par('vti',rsf.doc.rsfpar('bool','y','',''''''))
sfisoimpulse.version('2.1-git')
sfisoimpulse.synopsis('''sfisoimpulse wave=wave.rsf t=0.8 ep=0.4 dl=0.2 vti=y''','''''')
rsf.doc.progs['sfisoimpulse']=sfisoimpulse

