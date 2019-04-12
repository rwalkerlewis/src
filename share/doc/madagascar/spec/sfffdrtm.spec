[sfffdrtm]
Cat:    RSF/user/songxl
Desc:   2-D FFD RTM: MPI + OMP
DocCmd: sfffdrtm | cat
Port:   geo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   source rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  alpha float  -  -0.7 		
Param:  ax float  -  2.0 		suppress HF parameter
Param:  az float  -  2.0 		suppress HF parameter
Param:  cb float  -  0.01 		decaying parameter
Param:  cl float  -  0.01 		decaying parameter
Param:  cr float  -  0.01 		decaying parameter
Param:  ct float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  err float  -  0.00001 		
Param:  factor float  -  2.0/3.0 		suppress HF parameter
Param:  irz int  -   -  		if (!sf_getint('r0',&r0)) r0=0; 
LDesc:  (defaults to: isz)
Param:  isz int  -   -  		
Param:  jm int  -  20 		
Param:  jr int  -  1 		
Param:  nbb int  -  44 		
Param:  nbl int  -  44 		
Param:  nbr int  -  44 		
Param:  nbt int  -  44 		
Param:  nr int  -   -  		streamer total length
Param:  nt int  -   -  		
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 
Param:  sht int  -  0 		Time shift parameter
Param:  tskip int  -  0 		Time shift parameter

