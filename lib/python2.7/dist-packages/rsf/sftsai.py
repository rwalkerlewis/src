import rsf.doc

sfrickerfit = rsf.doc.rsfprog('sfrickerfit','user/tsai/Mrickerfit.c','''Model wavelet spectrum by fitting spectral components of ricker wavelet.''')
sfrickerfit.par('ma1',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickerfit.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickerfit.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickerfit.par('n',rsf.doc.rsfpar('int','','',''''''))
sfrickerfit.par('niter',rsf.doc.rsfpar('int','100','',''''''))
sfrickerfit.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrickerfit.version('2.1-git')
sfrickerfit.synopsis('''sfrickerfit < in.rsf > out.rsf ma1=ma1.rsf ma2=ma2.rsf m= n= niter=100 verb=n''','''
n is the number of components. ma1 is amplitude, ma2 is peak frequency.
''')
rsf.doc.progs['sfrickerfit']=sfrickerfit

sfrickback = rsf.doc.rsfprog('sfrickback','user/tsai/Mrickback.c','''None linear Ricker wavelet spectral fit. ''')
sfrickback.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickback.par('gamma',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('m',rsf.doc.rsfpar('floats','','',''' [n]'''))
sfrickback.par('n',rsf.doc.rsfpar('int','','',''''''))
sfrickback.par('niter',rsf.doc.rsfpar('int','100','',''''''))
sfrickback.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrickback.par('gamma',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfrickback.version('2.1-git')
sfrickback.synopsis('''sfrickback < in.rsf > out.rsf ma=ma.rsf gamma=debug.rsf m= m= m= m= m= m= m= m= m= m= n= niter=100 verb=n''','''''')
rsf.doc.progs['sfrickback']=sfrickback

