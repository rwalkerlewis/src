[sfcell3]
Cat:    RSF/system/seismic
Desc:   Second-order cell ray tracing with locally parabolic rays in 3-D
DocCmd: sfcell3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Param:  a0 float  -  0. 		First azimuth angle in degrees (if anglefile is not specified) 
Param:  amax float  -  360. 		Maximum azimuth angle in degrees (if anglefile is not specified) 
Param:  anglefile string  -   -  		file with initial angles (auxiliary input file name)
Param:  b0 float  -  0. 		First inclination angle in degrees (if anglefile is not specified) 
Param:  bmax float  -  180. 		Maximum inclination angle in degrees (if anglefile is not specified) 
Param:  na int  -   -  		Number of azimuths (if anglefile is not specified) 
Param:  nb int  -   -  		Number of inclinations (if anglefile is not specified) 
Param:  nt int  -   -  		number of time steps 
LDesc:  (defaults to: nx*nz)
Param:  order int  -  4 		Interpolation accuracy 
Param:  shotfile string  -   -  		file with shot locations (auxiliary input file name)
Param:  traj string  -   -  		
Param:  vel enum-bool  -  y 		If y, the input is velocity; if n, slowness 

