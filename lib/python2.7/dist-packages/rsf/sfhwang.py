import rsf.doc

sfpermwave2d = rsf.doc.rsfprog('sfpermwave2d','user/hwang/Mpermwave2d.c','''Wavefield Extrapolation for 2D PERM ''')
sfpermwave2d.par('wavelet',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermwave2d.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermwave2d.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpermwave2d.par('mig',rsf.doc.rsfpar('bool','n','','''if n, modeling; if y, migration '''))
sfpermwave2d.par('nz',rsf.doc.rsfpar('int','','','''depth axis '''))
sfpermwave2d.par('dz',rsf.doc.rsfpar('float','','',''''''))
sfpermwave2d.par('imageit',rsf.doc.rsfpar('int','0','','''time for extracting image '''))
sfpermwave2d.version('2.1-git')
sfpermwave2d.synopsis('''sfpermwave2d < data.rsf > image.rsf wavelet=wavelet_file.rsf left=left.rsf right=right.rsf mig=n nz= dz= imageit=0''','''''')
rsf.doc.progs['sfpermwave2d']=sfpermwave2d

sfpermlr2ddti = rsf.doc.rsfprog('sfpermlr2ddti','user/hwang/Mpermlr2ddti.cc','''None''')
sfpermlr2ddti.version('2.1-git')
sfpermlr2ddti.synopsis('''sfpermlr2ddti''','''''')
rsf.doc.progs['sfpermlr2ddti']=sfpermlr2ddti

sfawefd3dgpu = rsf.doc.rsfprog('sfawefd3dgpu','user/hwang/Mawefd3dgpu.cu','''3D acoustic wave equation finite difference time domain modeling ''')
sfawefd3dgpu.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3dgpu.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3dgpu.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3dgpu.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfawefd3dgpu.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfawefd3dgpu.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfawefd3dgpu.par('nbd',rsf.doc.rsfpar('int','20','',''''''))
sfawefd3dgpu.par('snap',rsf.doc.rsfpar('bool','n','',''''''))
sfawefd3dgpu.par('cden',rsf.doc.rsfpar('bool','y','',''''''))
sfawefd3dgpu.par('jsnap',rsf.doc.rsfpar('int','1','',''''''))
sfawefd3dgpu.version('2.1-git')
sfawefd3dgpu.synopsis('''sfawefd3dgpu < file_wav.rsf > file_dat.rsf vel=file_vel.rsf sou=file_src.rsf rec=file_rec.rsf den=file_den.rsf wfl=file_wfl.rsf verb=n nbd=20 snap=n cden=y jsnap=1''','''''')
rsf.doc.progs['sfawefd3dgpu']=sfawefd3dgpu

sfmpitransp = rsf.doc.rsfprog('sfmpitransp','user/hwang/Mmpitransp.c','''Large rectangular matrix in-place transpose with MPI ''')
sfmpitransp.par('indat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmpitransp.par('transp',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmpitransp.version('2.1-git')
sfmpitransp.synopsis('''sfmpitransp indat=Fin.rsf transp=Fout.rsf''','''''')
rsf.doc.progs['sfmpitransp']=sfmpitransp

