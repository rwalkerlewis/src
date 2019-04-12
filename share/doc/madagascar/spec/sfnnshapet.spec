[sfnnshapet]
Cat:    RSF/user/fomels
Desc:   2-D irregular data interpolation of traces using natural neighbors and shaping regularization
DocCmd: sfnnshapet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 float  -  1. 		
Param:  d2 float  -  1. 		
Param:  eps float  -  1.0e-6 		division parameter 
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  niter int  -   -  		GMRES memory 
LDesc:  (defaults to: niter)
Param:  nw int  -  2 		interpolator size 
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		
Param:  pattern string  -   -  		pattern file for output dimensions (auxiliary input file name)
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		
Param:  rect3 int  -  1 		smoothing regularization 
Param:  sym enum-bool  -  n 		if y, use symmetric shaping 
Param:  tol float  -  1e-3 		tolerance for stopping iteration 
Param:  weight string  -   -  		auxiliary input file name

