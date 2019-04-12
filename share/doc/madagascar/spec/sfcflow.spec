[sfcflow]
Cat:    RSF/user/fomels
Desc:   Fast mean-curvature flow
DocCmd: sfcflow | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  band float  -  1. 		narrow band 
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  3 		interpolation order 
Param:  rect int  -  3 		smoothing radius 
Param:  tol float  -  0.1 		error tolerance 

