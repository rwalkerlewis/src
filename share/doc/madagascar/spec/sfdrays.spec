[sfdrays]
Cat:    RSF/user/llisiw
Desc:   2D dynamic ray tracing by a Runge-Kutta integrator
DocCmd: sfdrays | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing gbeam data)
Param:  a0 float  -  0. 		minimum angle (if no anglefile) 
Param:  amax float  -  360. 		maximum angle (if no anglefile) 
Param:  anglefile string  -   -  		file with initial angles [nr,nshot] (auxiliary input file name)
Param:  dmat string  -   -  		auxiliary output file name
Param:  dt float  -   -  		Sampling in time 
Param:  mask string  -   -  		auxiliary output file name
Param:  nr int  -   -  		number of angles (if no anglefile) 
Param:  nt int  -   -  		Number of time steps 
Param:  order int  -  4 		Interpolation order 
Param:  proj string  -   -  		auxiliary output file name
Param:  rays string  -   -  		auxiliary output file name
Param:  shift float  -  0.5 		Complex source shift 
Param:  shotfile string  -   -  		file with shot locations [zshot,yshot,nshot] (auxiliary input file name)
Param:  vel enum-bool  -  y 		If y, input is velocity; if n, slowness 
Param:  verb enum-bool  -  y 		Verbosity flag 
Param:  yshot float  -   -  		
LDesc:  (defaults to: o[1]+0.5*(n[1]-1)*d[1])
Param:  zshot float  -  0. 		

