[sftomo]
Cat:    RSF/user/fomels
Desc:   Simple tomography test
DocCmd: sftomo | cat
Port:   stdin  rsf r req 	RSF standard input (containing time data)
Port:   stdout rsf w req 	RSF standard output (containing slow data)
Param:  adj enum-bool  -  n 		if n, generate traveltime from slowness; 
LDesc:         if y, invert slowness from traveltime 
Param:  ds int  -   -  		step size 
LDesc:  (defaults to: nz)
Param:  eps float  -  1. 		scaling parameter 
Param:  niter int  -  100 		maximum number of iterations 
Param:  np int  -  11 		
Param:  ns int  -  1 		number of depth steps 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing length in z and x 
Param:  tol float  -  1.e-7 		tolerance for stopping iterations 

