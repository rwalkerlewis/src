[sfttirtmsa]
Cat:    RSF/user/songxl
Desc:   2-D TTI FFD RTM: MPI + OMP
DocCmd: sfttirtmsa | cat
Port:   geo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   seta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   source rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   yita rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cb float  -  0.02 		decaying parameter
Param:  cl float  -  0.02 		decaying parameter
Param:  cr float  -  0.02 		decaying parameter
Param:  ct float  -  0.02 		decaying parameter
Param:  de enum-bool  -  y 		in angle
Param:  dt float  -   -  		time step size
Param:  err float  -  0.00001 		error control
Param:  irz int  -   -  		receiver depth
LDesc:  (defaults to: isz)
Param:  isz int  -   -  		source depth
Param:  jm int  -  20 		snap sampling
Param:  jr int  -  1 		receiver sampling
Param:  left int  -   -  		left
LDesc:  (defaults to: nr*3/2*jr)
Param:  nbb int  -  102 		boundary nodes
Param:  nbl int  -  128 		boundary nodes
Param:  nbr int  -  127 		boundary nodes
Param:  nbt int  -  102 		boundary nodes
Param:  nr int  -   -  		streamer total length
Param:  nt int  -   -  		total time length
Param:  opt enum-bool  -  y 		optimal padding
Param:  ratio float  -  2.0 		v0/vmax
Param:  right int  -   -  		right
LDesc:  (defaults to: nr/2*jr)
Param:  sht int  -  0 		time shift
Param:  tskip int  -  1000 		time skipped

