import rsf.doc

sfR2to3 = rsf.doc.rsfprog('sfR2to3','user/mehdi/MR2to3.f90','''None''')
sfR2to3.par('common',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfR2to3.par('cut',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfR2to3.par('offset',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfR2to3.version('2.1-git')
sfR2to3.synopsis('''sfR2to3 < two.rsf > three.rsf common=commonoffset.rsf cut= offset=''','''''')
rsf.doc.progs['sfR2to3']=sfR2to3

sfTTinv = rsf.doc.rsfprog('sfTTinv','user/mehdi/MTTinv.f90','''None''')
sfTTinv.par('CCorrect',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTTinv.par('Cpredicted',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTTinv.par('common',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTTinv.par('azimuth',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfTTinv.par('offset',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfTTinv.version('2.1-git')
sfTTinv.synopsis('''sfTTinv CCorrect=Ccor.rsf Cpredicted=Cpred.rsf common=commonoffset.rsf azimuth= offset=''','''''')
rsf.doc.progs['sfTTinv']=sfTTinv

sfconverted = rsf.doc.rsfprog('sfconverted','user/mehdi/Mconverted.f90','''None''')
sfconverted.par('actual_weights',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconverted.par('weights',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconverted.par('Rps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconverted.par('NoisyRps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconverted.par('Wip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfconverted.par('phi',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfconverted.par('theta',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfconverted.version('2.1-git')
sfconverted.synopsis('''sfconverted actual_weights=aw.rsf weights=w1.rsf Rps=Refl.rsf NoisyRps=NoisyRps.rsf Wip=Winvpred.rsf phi= theta=''','''''')
rsf.doc.progs['sfconverted']=sfconverted

sfAzsort = rsf.doc.rsfprog('sfAzsort','user/mehdi/MAzsort.f90','''None''')
sfAzsort.par('out2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfAzsort.par('common',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfAzsort.par('sectio',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfAzsort.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfAzsort.par('dimen',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfAzsort.par('win',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfAzsort.par('radius',rsf.doc.rsfpar('','','','''command-line parameter'''))
sfAzsort.version('2.1-git')
sfAzsort.synopsis('''sfAzsort < three.rsf > two.rsf out2=two2.rsf common=commonoffset.rsf sectio=sectionf.rsf filt=filtered.rsf dimen= win= radius=''','''''')
rsf.doc.progs['sfAzsort']=sfAzsort

sfthickat = rsf.doc.rsfprog('sfthickat','user/mehdi/Mthickat.f90','''None''')
sfthickat.par('refseis',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthickat.version('2.1-git')
sfthickat.synopsis('''sfthickat < reflectors.rsf refseis=reference.rsf > thickness.rsf''','''''')
rsf.doc.progs['sfthickat']=sfthickat

