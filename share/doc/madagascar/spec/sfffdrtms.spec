[sfffdrtms]
Cat:    RSF/user/songxl
Desc:   2-D FFD isotropic RTM: MPI + OMP
DocCmd: sfffdrtms | cat
Port:   geo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   source rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cb float  -  0.01 		decaying parameter
Param:  cl float  -  0.01 		decaying parameter
Param:  cr float  -  0.01 		decaying parameter
Param:  ct float  -  0.01 		decaying parameter
Param:  dt float  -   -  		time step size
Param:  irz int  -   -  		receiver depth
LDesc:  (defaults to: isz)
Param:  isz int  -   -  		source depth
Param:  jm int  -  20 		snap sampling
Param:  jr int  -  1 		receiver sampling
Param:  left int  -  2400 		left
Param:  nbb int  -  44 		boundary nodes
Param:  nbl int  -  44 		boundary nodes
Param:  nbr int  -  44 		boundary nodes
Param:  nbt int  -  44 		boundary nodes
Param:  nr int  -   -  		streamer total length
Param:  nt int  -   -  		total time length
Param:  opt enum-bool  -  y 		optimal padding
Param:  right int  -  800 		right
Param:  sht int  -  0 		Time shift parameter
Param:  tskip int  -  0 		Time shift parameter

