import rsf.doc

sfepisort = rsf.doc.rsfprog('sfepisort','user/yunzhi/Mepisort.c','''Sort microseismic surface array recording traces by their distances or azimuths to a given epicenter. ''')
sfepisort.par('x',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfepisort.par('y',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfepisort.par('dist',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfepisort.par('theta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfepisort.par('epi_x',rsf.doc.rsfpar('float','','','''referenced epicenter coordinate x. '''))
sfepisort.par('epi_y',rsf.doc.rsfpar('float','','','''referenced epicenter coordinate y. '''))
sfepisort.par('sort',rsf.doc.rsfpar('string ',desc='''sort distance[d] (default) or angle[a] '''))
sfepisort.version('2.1-git')
sfepisort.synopsis('''sfepisort < in.rsf x=x_file.rsf y=y_file.rsf > out.rsf dist=dist_file.rsf theta=theta_file.rsf epi_x= epi_y= sort=''','''''')
rsf.doc.progs['sfepisort']=sfepisort

sfspiralsort = rsf.doc.rsfprog('sfspiralsort','user/yunzhi/Mspiralsort.c','''Sort microseismic surface array recording traces with a given epicenter along a spiral shape R = r0 + d(a-a0). ''')
sfspiralsort.par('x',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfspiralsort.par('y',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfspiralsort.par('dist',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfspiralsort.par('theta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfspiralsort.par('epi_x',rsf.doc.rsfpar('float','','','''referenced epicenter coordinate x. '''))
sfspiralsort.par('epi_y',rsf.doc.rsfpar('float','','','''referenced epicenter coordinate y. '''))
sfspiralsort.par('radius0',rsf.doc.rsfpar('float','1.0','','''Starting radius of spiral. '''))
sfspiralsort.par('angle0',rsf.doc.rsfpar('float','0.0','','''Starting angle of spiral. '''))
sfspiralsort.par('dr',rsf.doc.rsfpar('float','','','''Spiral interval parameter. '''))
sfspiralsort.version('2.1-git')
sfspiralsort.synopsis('''sfspiralsort < in.rsf x=x_file.rsf y=y_file.rsf > out.rsf dist=dist_file.rsf theta=theta_file.rsf epi_x= epi_y= radius0=1.0 angle0=0.0 dr=''','''''')
rsf.doc.progs['sfspiralsort']=sfspiralsort

sffaultrbf1d = rsf.doc.rsfprog('sffaultrbf1d','user/yunzhi/Mfaultrbf1d.c','''Compute RBF across fault using fault attribute computed by Sobel filter. ''')
sffaultrbf1d.par('i0',rsf.doc.rsfpar('int','','','''Reference trace position. '''))
sffaultrbf1d.par('scale',rsf.doc.rsfpar('float','1.0','','''Fault attribute scaling factor (0.0 ~ factor). '''))
sffaultrbf1d.par('r0',rsf.doc.rsfpar('float','1.0','','''Reference radial in RBF. '''))
sffaultrbf1d.par('useinput',rsf.doc.rsfpar('bool','y','','''Flag: whether use the input fault attribute. '''))
sffaultrbf1d.version('2.1-git')
sffaultrbf1d.synopsis('''sffaultrbf1d < in.rsf > out.rsf i0= scale=1.0 r0=1.0 useinput=y''','''''')
rsf.doc.progs['sffaultrbf1d']=sffaultrbf1d

