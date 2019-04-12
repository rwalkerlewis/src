[sfescbsc3]
Cat:    RSF/user/cram
Desc:   Prepare supercells for stitching escape tables in 3-D
DocCmd: sfescbsc3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing adom data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  df float  -  0.1 		< Maximum distance to travel per step (fraction of the cell size) >
Param:  dx float  -   -  		Sampling of x axis 
Param:  dy float  -   -  		Sampling of y axis 
Param:  dz float  -   -  		Sampling of z axis 
Param:  md float  -   -  		Half-width of a supercell 
LDesc:  (defaults to: dz)
Param:  na int  -   -  		Number of samples in azimuth dimension 
Param:  nb int  -   -  		Number of samples in inclination dimension 
Param:  nc int  -  0 		Number of threads to use for ray tracing (OMP_NUM_THREADS by default) 
Param:  nx int  -   -  		Number of samples in x axis 
Param:  ny int  -   -  		Number of samples in y axis 
Param:  nz int  -   -  		Number of samples in z axis 
Param:  ox float  -   -  		Beginning of x axis 
Param:  oy float  -   -  		Beginning of y axis 
Param:  oz float  -   -  		Beginning of z axis 
Param:  parab enum-bool  -  y 		y - use parabolic approximation of trajectories, n - straight line 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vspl string  -   -  		Spline coefficients for velocity model (auxiliary input file name)

