[sfescfgrid2]
Cat:    RSF/user/cram
Desc:   Solution of escape equations by Gauss-Seidel solver on full grid for 2-D (an)isotropic media
DocCmd: sfescfgrid2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing spdom data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  atraced enum-bool  -  n 		true - output map of all traced points 
Param:  cmix enum-bool  -  n 		true - check for color mixing 
Param:  mdist float  -   -  		Maximum distance between points in F-D stencil 
LDesc:  (defaults to: SF_HUGE)
Param:  morder int  -   -  		Maximum order in F-D stencil 
LDesc:  (defaults to: ESC2_MORDER)
Param:  mtraced enum-bool  -  n 		true - output map of points traced because of mdist criterion 
Param:  na int  -  360 		Number of phase angles 
Param:  niter int  -   -  		Maximum number of Gauss-Seidel iterations 
LDesc:  (defaults to: nx)
Param:  thresh float  -  1e-6 		Convergence threshold 
Param:  tracebc enum-bool  -  y 		n - do not trace B.C. points 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vspl string  -   -  		Spline coefficients for velocity model (auxiliary input file name)

