import rsf.doc

sfmedianbalance = rsf.doc.rsfprog('sfmedianbalance','user/mlai/Mmedianbalance.py','''Do median balancing.''')
sfmedianbalance.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfmedianbalance.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfmedianbalance.par('inp',rsf.doc.rsfpar('string','','','''input file'''))
sfmedianbalance.par('out',rsf.doc.rsfpar('string','','','''output file'''))
sfmedianbalance.par('verb',rsf.doc.rsfpar('bool','n','','''if y, print system commands, outputs'''))
sfmedianbalance.par('pclip',rsf.doc.rsfpar('float','99','','''percentile clip'''))
sfmedianbalance.version('2.1-git')
sfmedianbalance.synopsis('''sfmedianbalance inp= out= inp= out= verb=n pclip=99''','''''')
rsf.doc.progs['sfmedianbalance']=sfmedianbalance

