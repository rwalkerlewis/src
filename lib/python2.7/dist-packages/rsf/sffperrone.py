import rsf.doc

sfavvvdwe2d = rsf.doc.rsfprog('sfavvvdwe2d','user/fperrone/Mavvvdwe2d.c','''2D acoustic variable-velocity variable-density time-domain FD modeling ''')
sfavvvdwe2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe2d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfavvvdwe2d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfavvvdwe2d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfavvvdwe2d.par('free',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfavvvdwe2d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfavvvdwe2d.par('adj',rsf.doc.rsfpar('bool','n','','''Adjoint flag'''))
sfavvvdwe2d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfavvvdwe2d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfavvvdwe2d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfavvvdwe2d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfavvvdwe2d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfavvvdwe2d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfavvvdwe2d.version('2.1-git')
sfavvvdwe2d.synopsis('''sfavvvdwe2d < Fwav.rsf vel=Fvel.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf > Fdat.rsf wfl=Fwfl.rsf verb=n snap=n free=n dabc=n adj=n jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) oqz=sf_o(az) oqx=sf_o(ax)''','''
The code uses a standard second-order stencil in time.
The coefficients of the spatial stencil are computed 
by matching the transfer function of the discretized 
first-derivative operator to the ideal response. 
The optimized coefficients minimize dispersion 
given that particular size of the stencil.

The term 
	ro div (1/ro grad (u))
where
	ro   : density
	div  : divergence op
	grad : gradient  op
	u    : wavefield
	
is implemented in order to obtain a positive semi-definite operator.

The code implements both the forward (adj=n) and adjoint (adj=y) modeling operator.

============= FILE DESCRIPTIONS   ========================      

Fdat.rsf - An RSF file containing your data in the following format:
			axis 1 - Receiver location
			axis 2 - Time
			
Fwav.rsf - An RSF file containing your VOLUME DENSITY INJECTION RATE 
wavelet information.  The sampling interval, origin time, 
and number of time samples will be used as the defaults for the modeling code.
	       i.e. your wavelet needs to have the same length and parameters that you want to model with!
	       The first axis is the number of source locations.
	       The second axis is time.
		   
Fvel.rsf - An N dimensional RSF file that contains the values for the velocity field at every point in the computational domain.
		
Fden.rsf - An N dimensional RSF file that contains the values for density at every point in the computational domain.

Frec.rsf - Coordinates of the receivers
		axis 1 - (x,z) of the receiver
		axis 2 - receiver index

Fsou.rsf - Coordinate of the sources
		axis 1 - (x,y,z) of the source
		axis 2 - source index

Fwfl.rsf - Output wavefield

verb=y/n - verbose flag

snap=y/n - wavefield snapshots flag

free=y/n - free surface on/off

dabc=y/n - absorbing boundary conditions on/off

jdata    - data sampling 

jsnap    - wavefield snapshots sampling


Author: Francesco Perrone
Date: November 2013
''')
rsf.doc.progs['sfavvvdwe2d']=sfavvvdwe2d

sfavvvdwe3d = rsf.doc.rsfprog('sfavvvdwe3d','user/fperrone/Mavvvdwe3d.c','''3D acoustic variable-velocity variable-density time-domain FD modeling ''')
sfavvvdwe3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe3d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe3d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe3d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfavvvdwe3d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfavvvdwe3d.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfavvvdwe3d.par('snap',rsf.doc.rsfpar('bool','n','','''Wavefield snapshots flag '''))
sfavvvdwe3d.par('free',rsf.doc.rsfpar('bool','n','','''Free surface flag '''))
sfavvvdwe3d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfavvvdwe3d.par('adj',rsf.doc.rsfpar('bool','n','','''Adjoint flag'''))
sfavvvdwe3d.par('jdata',rsf.doc.rsfpar('int','1','','''# of t steps at which to save receiver data '''))
sfavvvdwe3d.par('jsnap',rsf.doc.rsfpar('int','nt','','''# of t steps at which to save wavefield '''))
sfavvvdwe3d.par('nqz',rsf.doc.rsfpar('int','sf_n(az)','','''Saved wfld window nz '''))
sfavvvdwe3d.par('nqx',rsf.doc.rsfpar('int','sf_n(ax)','','''Saved wfld window nx '''))
sfavvvdwe3d.par('nqy',rsf.doc.rsfpar('int','sf_n(ay)','','''Saved wfld window ny '''))
sfavvvdwe3d.par('oqz',rsf.doc.rsfpar('float','sf_o(az)','','''Saved wfld window oz '''))
sfavvvdwe3d.par('oqx',rsf.doc.rsfpar('float','sf_o(ax)','','''Saved wfld window ox '''))
sfavvvdwe3d.par('oqy',rsf.doc.rsfpar('float','sf_o(ay)','','''Saved wfld window oy '''))
sfavvvdwe3d.version('2.1-git')
sfavvvdwe3d.synopsis('''sfavvvdwe3d < Fwav.rsf vel=Fvel.rsf den=Fden.rsf sou=Fsou.rsf rec=Frec.rsf > Fdat.rsf wfl=Fwfl.rsf verb=n snap=n free=n dabc=n adj=n jdata=1 jsnap=nt nqz=sf_n(az) nqx=sf_n(ax) nqy=sf_n(ay) oqz=sf_o(az) oqx=sf_o(ax) oqy=sf_o(ay)''','''
The code uses a standard second-order stencil in time.
The coefficients of the spatial stencil are computed 
by matching the transfer function of the discretized 
first-derivative operator to the ideal response. 
The optimized coefficients minimize dispersion 
given that particular size of the stencil.

The term 
	ro div (1/ro grad (u))
where
	ro   : density
	div  : divergence op
	grad : gradient  op
	u    : wavefield
	
is implemented in order to obtain a positive semi-definite operator.

The code implements both the forward (adj=n) and adjoint (adj=y) modeling operator.

============= FILE DESCRIPTIONS   ========================      

Fdat.rsf - An RSF file containing your data in the following format:
			axis 1 - Receiver location
			axis 2 - Time
			
Fwav.rsf - An RSF file containing your VOLUME DENSITY INJECTION RATE 
wavelet information.  The sampling interval, origin time, 
and number of time samples will be used as the defaults for the modeling code.
	       i.e. your wavelet needs to have the same length and parameters that you want to model with!
	       The first axis is the number of source locations.
	       The second axis is time.
		   
Fvel.rsf - An N dimensional RSF file that contains the values for the velocity field at every point in the computational domain.
		
Fden.rsf - An N dimensional RSF file that contains the values for density at every point in the computational domain.

Frec.rsf - Coordinates of the receivers
		axis 1 - (x,z) of the receiver
		axis 2 - receiver index

Fsou.rsf - Coordinate of the sources
		axis 1 - (x,y,z) of the source
		axis 2 - source index

Fwfl.rsf - Output wavefield

verb=y/n - verbose flag

snap=y/n - wavefield snapshots flag

free=y/n - free surface on/off

dabc=y/n - absorbing boundary conditions on/off

jdata    - data sampling 

jsnap    - wavefield snapshots sampling



Author: Francesco Perrone
Date: November 2013
''')
rsf.doc.progs['sfavvvdwe3d']=sfavvvdwe3d

sfbvvvdwe2d = rsf.doc.rsfprog('sfbvvvdwe2d','user/fperrone/Mbvvvdwe2d.c','''Born variable-density variable-velocity acoustic 2D time-domain FD modeling ''')
sfbvvvdwe2d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe2d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe2d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe2d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe2d.par('liw',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe2d.par('lid',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe2d.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfbvvvdwe2d.par('ompnth',rsf.doc.rsfpar('int','0','','''OpenMP available threads '''))
sfbvvvdwe2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfbvvvdwe2d.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfbvvvdwe2d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfbvvvdwe2d.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfbvvvdwe2d.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfbvvvdwe2d.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfbvvvdwe2d.par('nqz',rsf.doc.rsfpar('int','sf_n(a1)','',''''''))
sfbvvvdwe2d.par('nqx',rsf.doc.rsfpar('int','sf_n(a2)','',''''''))
sfbvvvdwe2d.par('oqz',rsf.doc.rsfpar('float','sf_o(a1)','',''''''))
sfbvvvdwe2d.par('oqx',rsf.doc.rsfpar('float','sf_o(a2)','',''''''))
sfbvvvdwe2d.version('2.1-git')
sfbvvvdwe2d.synopsis('''sfbvvvdwe2d < Fwav.rsf sou=Fsou.rsf rec=Frec.rsf vel=Fvel.rsf den=Fden.rsf ref=Fref.rsf wfl=Fwfl.rsf > Fdat.rsf liw=Fliw.rsf lid=Flid.rsf ompchunk=1 ompnth=0 verb=n snap=n dabc=n free=n jdata=1 jsnap=nt nqz=sf_n(a1) nqx=sf_n(a2) oqz=sf_o(a1) oqx=sf_o(a2)''','''''')
rsf.doc.progs['sfbvvvdwe2d']=sfbvvvdwe2d

sfbvvvdwe3d = rsf.doc.rsfprog('sfbvvvdwe3d','user/fperrone/Mbvvvdwe3d.c','''Born variable-density variable-velocity acoustic 3D time-domain FD modeling ''')
sfbvvvdwe3d.par('sou',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe3d.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe3d.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe3d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfbvvvdwe3d.par('wfl',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe3d.par('liw',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe3d.par('lid',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfbvvvdwe3d.par('ompchunk',rsf.doc.rsfpar('int','1','','''OpenMP data chunk size '''))
sfbvvvdwe3d.par('ompnth',rsf.doc.rsfpar('int','0','','''OpenMP available threads '''))
sfbvvvdwe3d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfbvvvdwe3d.par('snap',rsf.doc.rsfpar('bool','n','','''wavefield snapshots flag '''))
sfbvvvdwe3d.par('dabc',rsf.doc.rsfpar('bool','n','','''Absorbing BC '''))
sfbvvvdwe3d.par('free',rsf.doc.rsfpar('bool','n','','''free surface flag '''))
sfbvvvdwe3d.par('jdata',rsf.doc.rsfpar('int','1','',''''''))
sfbvvvdwe3d.par('jsnap',rsf.doc.rsfpar('int','nt','',''''''))
sfbvvvdwe3d.par('nqz',rsf.doc.rsfpar('int','sf_n(a1)','',''''''))
sfbvvvdwe3d.par('nqx',rsf.doc.rsfpar('int','sf_n(a2)','',''''''))
sfbvvvdwe3d.par('nqy',rsf.doc.rsfpar('int','sf_n(a3)','',''''''))
sfbvvvdwe3d.par('oqz',rsf.doc.rsfpar('float','sf_o(a1)','',''''''))
sfbvvvdwe3d.par('oqx',rsf.doc.rsfpar('float','sf_o(a2)','',''''''))
sfbvvvdwe3d.par('oqy',rsf.doc.rsfpar('float','sf_o(a3)','',''''''))
sfbvvvdwe3d.version('2.1-git')
sfbvvvdwe3d.synopsis('''sfbvvvdwe3d < Fwav.rsf sou=Fsou.rsf rec=Frec.rsf vel=Fvel.rsf den=Fden.rsf ref=Fref.rsf wfl=Fwfl.rsf > Fdat.rsf liw=Fliw.rsf lid=Flid.rsf ompchunk=1 ompnth=0 verb=n snap=n dabc=n free=n jdata=1 jsnap=nt nqz=sf_n(a1) nqx=sf_n(a2) nqy=sf_n(a3) oqz=sf_o(a1) oqx=sf_o(a2) oqy=sf_o(a3)''','''''')
rsf.doc.progs['sfbvvvdwe3d']=sfbvvvdwe3d

