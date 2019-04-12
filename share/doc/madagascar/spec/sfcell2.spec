[sfcell2]
Cat:    RSF/system/seismic
Desc:   Second-order cell ray tracing with locally parabolic rays
DocCmd: sfcell2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Param:  a0 float  -  0. 		First angle in degrees (if anglefile is not specified) 
Param:  amax float  -  360. 		Maximum angle in degrees (if anglefile is not specified) 
Param:  anglefile string  -   -  		file with initial angles (auxiliary input file name)
Param:  lsint enum-bool  -  n 		if use least-squares interpolation 
Param:  nr int  -   -  		Number of angles (if anglefile is not specified) 
Param:  nt int  -   -  		number of time steps 
LDesc:  (defaults to: nx*nz)
Param:  order int  -  4 		Interpolation accuracy 
Param:  shotfile string  -   -  		file with shot locations (auxiliary input file name)
Param:  traj string  -   -  		
Param:  vel enum-bool  -  y 		If y, the input is velocity; if n, slowness 

