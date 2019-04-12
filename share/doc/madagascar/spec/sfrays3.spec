[sfrays3]
Cat:    RSF/system/seismic
Desc:   Ray tracing by a Runge-Kutta integrator in 3-D
DocCmd: sfrays3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing rays data)
Param:  a0 float  -  0. 		First azimuth angle in degrees (if anglefile is not specified) 
Param:  amax float  -  360. 		Maximum azimuth angle in degrees (if anglefile is not specified) 
Param:  anglefile string  -   -  		file with initial angles (auxiliary input file name)
Param:  b0 float  -  0. 		First inclination angle in degrees (if anglefile is not specified) 
Param:  bmax float  -  180. 		Maximum inclination angle in degrees (if anglefile is not specified) 
Param:  dt float  -   -  		Sampling in time 
Param:  escvar enum-bool  -  n 		If y - output escape values, n - trajectories 
Param:  na int  -   -  		Number of azimuths (if anglefile is not specified) 
Param:  nb int  -   -  		Number of inclinations (if anglefile is not specified) 
Param:  nt int  -   -  		Number of time steps 
Param:  order int  -  4 		Interpolation order 
Param:  shotfile string  -   -  		file with shot locations (auxiliary input file name)
Param:  sym enum-bool  -  y 		if y, use symplectic integrator 
Param:  vel enum-bool  -  y 		If y, input is velocity; if n, slowness 
Param:  xshot float  -   -  		shot location crossline (if shotfile is not specified) 
LDesc:  (defaults to: o[2] + 0.5*(n[2]-1)*d[2])
Param:  yshot float  -   -  		shot location inline (if shotfile is not specified) 
LDesc:  (defaults to: o[1] + 0.5*(n[1]-1)*d[1])
Param:  zshot float  -   -  		shot location in depth (if shotfile is not specified) 
LDesc:  (defaults to: o[0])

