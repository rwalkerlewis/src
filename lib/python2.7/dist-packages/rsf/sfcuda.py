import rsf.doc

sfgpuktmig = rsf.doc.rsfprog('sfgpuktmig','user/cuda/Mgpuktmig.cu','''Prestack time migration (2-D/3-D) with CUDA. ''')
sfgpuktmig.par('vrms',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpuktmig.par('sxsy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpuktmig.par('gxgy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpuktmig.par('cxcy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfgpuktmig.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfgpuktmig.par('time',rsf.doc.rsfpar('bool','n','','''Total time measurement time '''))
sfgpuktmig.par('aa',rsf.doc.rsfpar('bool','y','','''Antialiaing flag '''))
sfgpuktmig.par('diff',rsf.doc.rsfpar('bool','y','','''Differentiation flag '''))
sfgpuktmig.par('dbtr',rsf.doc.rsfpar('int','-1','','''Desired number of traces per block of threads '''))
sfgpuktmig.par('apx',rsf.doc.rsfpar('int','onx/2','','''Apperture half-width in x direction '''))
sfgpuktmig.par('apy',rsf.doc.rsfpar('int','ony/2','','''Apperture half-width in y direction '''))
sfgpuktmig.par('maxtri',rsf.doc.rsfpar('int','13','','''Maximum half-length of the antialias filter '''))
sfgpuktmig.par('trfact',rsf.doc.rsfpar('float','4.0*(0.5*(odx + ody)/dt)','','''Trace factor for antialias filter length calculation '''))
sfgpuktmig.par('vrms',rsf.doc.rsfpar('string ',desc='''File with RMS velocities (auxiliary input file name)'''))
sfgpuktmig.par('sxsy',rsf.doc.rsfpar('string ',desc='''File with shot coordinates (auxiliary input file name)'''))
sfgpuktmig.par('gxgy',rsf.doc.rsfpar('string ',desc='''File with receiver coordinates (auxiliary input file name)'''))
sfgpuktmig.par('cxcy',rsf.doc.rsfpar('string ',desc='''File with midpoint coordinates (auxiliary input file name)'''))
sfgpuktmig.version('2.1-git')
sfgpuktmig.synopsis('''sfgpuktmig < data.rsf > image.rsf vrms=vrms.rsf sxsy=sxsy.rsf gxgy=gxgy.rsf cxcy=cxcy.rsf verb=n time=n aa=y diff=y dbtr=-1 apx=onx/2 apy=ony/2 maxtri=13 trfact=4.0*(0.5*(odx + ody)/dt)''','''''')
rsf.doc.progs['sfgpuktmig']=sfgpuktmig

