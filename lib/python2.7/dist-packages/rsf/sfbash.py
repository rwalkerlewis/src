import rsf.doc

sfdatshift = rsf.doc.rsfprog('sfdatshift','user/bash/Mdatshift.c','''Calculate datum shift from elevation profile for 2-D shot gathers ''')
sfdatshift.par('elev',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdatshift.par('v0',rsf.doc.rsfpar('float','','',''''''))
sfdatshift.par('elev',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfdatshift.version('2.1-git')
sfdatshift.synopsis('''sfdatshift < in.rsf > out.rsf elev=elev.rsf v0=''','''''')
rsf.doc.progs['sfdatshift']=sfdatshift

sfeikfswp = rsf.doc.rsfprog('sfeikfswp','user/bash/Meikfswp.c','''Fast sweeping eikonal solver (2-D/3-D). ''')
sfeikfswp.par('vel',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n - slowness '''))
sfeikfswp.par('niter',rsf.doc.rsfpar('int','2','','''number of sweeping iterations '''))
sfeikfswp.par('zshot',rsf.doc.rsfpar('float','0.','','''Shot location (used if no shotfile) '''))
sfeikfswp.par('yshot',rsf.doc.rsfpar('float','o2 + 0.5*(n2-1)*d2','',''''''))
sfeikfswp.par('xshot',rsf.doc.rsfpar('float','o3 + 0.5*(n3-1)*d3','',''''''))
sfeikfswp.par('shotfile',rsf.doc.rsfpar('string ',desc='''File with shot locations (n2=number of shots, n1=3) '''))
sfeikfswp.par('horizon',rsf.doc.rsfpar('string ',desc='''File with a reflection interface '''))
sfeikfswp.version('2.1-git')
sfeikfswp.synopsis('''sfeikfswp < vel.rsf > time.rsf vel=y niter=2 zshot=0. yshot=o2 + 0.5*(n2-1)*d2 xshot=o3 + 0.5*(n3-1)*d3 shotfile= horizon=''','''''')
rsf.doc.progs['sfeikfswp']=sfeikfswp

sfktmig = rsf.doc.rsfprog('sfktmig','user/bash/Mktmig.c','''Prestack time migration (2-D/3-D) for irregular data. ''')
sfktmig.par('vrms',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfktmig.par('sxsy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfktmig.par('gxgy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfktmig.par('cxcy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfktmig.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfktmig.par('time',rsf.doc.rsfpar('bool','n','','''Measure execution time '''))
sfktmig.par('aa',rsf.doc.rsfpar('bool','y','','''Antialiaing flag '''))
sfktmig.par('diff',rsf.doc.rsfpar('bool','y','','''Differentiation flag '''))
sfktmig.par('dbtr',rsf.doc.rsfpar('int','1000','','''Number of input traces to read at once '''))
sfktmig.par('apx',rsf.doc.rsfpar('int','onx/2','','''Apperture half-width in x direction '''))
sfktmig.par('apy',rsf.doc.rsfpar('int','ony/2','','''Apperture half-width in y direction '''))
sfktmig.par('maxtri',rsf.doc.rsfpar('int','13','','''Maximum half-length of the antialias filter '''))
sfktmig.par('trfact',rsf.doc.rsfpar('float','4.0*(0.5*(odx + ody)/dt)','','''Trace factor for antialias filter length calculation '''))
sfktmig.par('vrms',rsf.doc.rsfpar('string ',desc='''File with RMS velocities (auxiliary input file name)'''))
sfktmig.par('sxsy',rsf.doc.rsfpar('string ',desc='''File with shot coordinates (auxiliary input file name)'''))
sfktmig.par('gxgy',rsf.doc.rsfpar('string ',desc='''File with receiver coordinates (auxiliary input file name)'''))
sfktmig.par('cxcy',rsf.doc.rsfpar('string ',desc='''File with midpoint coordinates (auxiliary input file name)'''))
sfktmig.version('2.1-git')
sfktmig.synopsis('''sfktmig < data.rsf > image.rsf vrms=vrms.rsf sxsy=sxsy.rsf gxgy=gxgy.rsf cxcy=cxcy.rsf verb=n time=n aa=y diff=y dbtr=1000 apx=onx/2 apy=ony/2 maxtri=13 trfact=4.0*(0.5*(odx + ody)/dt)''','''''')
rsf.doc.progs['sfktmig']=sfktmig

sfmaskval = rsf.doc.rsfprog('sfmaskval','user/bash/Mmaskval.c','''Mask values inside or outside of a range.''')
sfmaskval.par('upper',rsf.doc.rsfpar('float','+FLT_MAX','','''upper range limit '''))
sfmaskval.par('lower',rsf.doc.rsfpar('float','-FLT_MAX','','''lower range limit '''))
sfmaskval.par('upperval',rsf.doc.rsfpar('float','+FLT_MAX','','''upper range value '''))
sfmaskval.par('lowerval',rsf.doc.rsfpar('float','-FLT_MAX','','''lower range value '''))
sfmaskval.version('2.1-git')
sfmaskval.synopsis('''sfmaskval < in.rsf > out.rsf upper=+FLT_MAX lower=-FLT_MAX upperval=+FLT_MAX lowerval=-FLT_MAX''','''
sfmaskval < in.rsf > out.rsf upper=ul lower=ll upperval=uv lowerval=lv

If upper > lower, then values larger than ul will be changed to uv and
values belowe ll will be changed to lv.
If upper < lower, then values inside [ul;ll] will be changed to lv.

''')
rsf.doc.progs['sfmaskval']=sfmaskval

sfmpihello = rsf.doc.rsfprog('sfmpihello','user/bash/Mmpihello.c','''MPI example, summation of vectors c = a + b ''')
sfmpihello.par('b',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpihello.version('2.1-git')
sfmpihello.synopsis('''sfmpihello b=bin.rsf''','''''')
rsf.doc.progs['sfmpihello']=sfmpihello

sfwile = rsf.doc.rsfprog('sfwile','user/bash/Mwile.c','''Process data with GIMP 2.0.''')
sfwile.par('command',rsf.doc.rsfpar('string ',desc='''Command to be executed by GIMP '''))
sfwile.version('2.1-git')
sfwile.synopsis('''sfwile < in.rsf > out.rsf command=''','''
Input samples must be in byte (unsigned char) format. Preprocess data
with sfbyte first, if they have float or other samples. Only first 2D
section (n1 x n2) is taken from input data, the rest is ignored.
Use sfwindow and/or sftransp to generate input in adequate order.
o1, o2, d1, and d2 are ignored; data are treated by GIMP as equally
spaced.

Be advised, that a greyscale image file is created; not every
GIMP plugin is capable of working with greyscale input.

Examples:

sfwile < in.rsf command="gimp-equalize TRUE" > out.rsf
sfwile < in.rsf command="plug-in-spread 5 5" > out.rsf
sfwile < in.rsf command="plug-in-gauss-rle 4.0 TRUE TRUE" > out.rsf
sfwile < in.rsf command="plug-in-sobel TRUE TRUE TRUE" > out.rsf
sfwile < in.rsf command="plug-in-neon 5.0 0.0" > out.rsf
sfwile < in.rsf command="plug-in-emboss 315.0 45.0 7 TRUE" > out.rsf
sfwile < in.rsf command="plug-in-ripple 27 2 1 0 0 TRUE TRUE" > out.rsf
sfwile < in.rsf command="plug-in-whirl-pinch 45 0.0 1.0" > out.rsf

Documentation for basic GIMP plugins can be found here:
http://docs.gimp.org/en/filters.html
Information about additional plugins is collected here:
http://registry.gimp.org/
''')
rsf.doc.progs['sfwile']=sfwile

