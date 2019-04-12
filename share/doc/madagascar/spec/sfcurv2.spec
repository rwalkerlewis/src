[sfcurv2]
Cat:    RSF/user/chen
Desc:   Joint estimation of curvature and slope
DocCmd: sfcurv2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   slope rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 
Param:  niter int  -  5 		iterations 

