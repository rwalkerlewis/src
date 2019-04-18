[sfpwefd2D_PML]
Cat:    RSF/user/rlwalker
Desc:   Short description line
DocCmd: sfpwefd2D_PML | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   fro rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fvs rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   kdr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   kfl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ksg rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   phi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   prm rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   shm rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sro rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tor rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  K_MAX_PML float  -   -  		! from Stephen Gedney's unpublished class notes for class EE699, lecture 8, slide 8-11 
LDesc:  (defaults to: 1.0f)
Param:  NPOINTS_PML int  -  10 		
Param:  NPOWER float  -   -  		power to compute d0 profile 
LDesc:  (defaults to: 2.0f)
Param:  Rcoef float  -   -  		Reflection coefficient 
LDesc:  (defaults to: 0.001f)
Param:  USE_PML_BOTTOM enum-bool  -  n 		'PML ABC' 
Param:  USE_PML_LEFT enum-bool  -  n 		'PML ABC' 
Param:  USE_PML_RIGHT enum-bool  -  n 		'PML ABC' 
Param:  USE_PML_TOP enum-bool  -  n 		'PML ABC' 
Param:  abcone enum-bool  -  n 		use sharp brake at end of boundary layer 
Param:  abcpml enum-bool  -  n 		'PML ABC' 
Param:  ani int  -  -1 		Anisotropy type, see comments 
Param:  cfl enum-bool  -  y 		use CFL check, will cause program to fail if not satisfied 
Param:  dabc enum-bool  -  y 		use sponge absorbing BC 
Param:  debug enum-bool  -  y 		print debugging info 
Param:  fmax float  -   -  		
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		Absorbing Boundary 
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  nb int  -  100 		padding size for absorbing boundary 
Param:  nbell int  -  1 		bell size 
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  opot enum-bool  -  n 		output potentials 
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  srctype int  -  0 		source type, see comments 
Param:  verb enum-bool  -  y 		verbosity flag 

