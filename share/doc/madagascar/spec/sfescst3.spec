[sfescst3]
Cat:    RSF/user/cram
Desc:   Escape tables by stitching of escape solutions in supercells in 3-D
DocCmd: sfescst3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing spdom data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  aper float  -   -  		Maximum aperture in x and y directions from current point (default - up to grid boundaries) 
LDesc:  (defaults to: SF_HUGE)
Param:  inet int  -  1 		Network interface index 
Param:  mmaped enum-bool  -  y 		n - do not use memory mapping for local data access 
Param:  morder int  -  1 		Order of interpolation accuracy in the angular domain (1-3) 
Param:  mp int  -  1 		Bufferization factor for multicore processing (number of points in buffer = mp*nc) 
Param:  na int  -  360 		Number of azimuth phase angles 
Param:  nb int  -  180 		Number of inclination phase angles 
Param:  nc int  -  0 		Number of threads to use for ray tracing (OMP_NUM_THREADS by default) 
Param:  parab enum-bool  -  y 		y - use parabolic approximation of trajectories, n - straight line 
Param:  rfail enum-bool  -  y 		n - do not quit if remote processing fails, try local processing 
Param:  scdaemon string  -   -  		Daemon for distributed computation (auxiliary input file name)
Param:  scgrid string  -   -  		Grid of supercells of local escape solutions (auxiliary input file name)
Param:  tdel int  -  0 		Optional delay time before connecting (seconds) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vspl string  -   -  		Spline coefficients for velocity model (auxiliary input file name)

