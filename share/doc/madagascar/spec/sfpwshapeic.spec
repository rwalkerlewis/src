[sfpwshapeic]
Cat:    RSF/user/gchliu
Desc:   Least Square Imaging condition using structure-based shaping regularization
DocCmd: sfpwshapeic | cat
Port:   stdin  rsf r req 	RSF standard input (containing upgw data)
Port:   stdout rsf w req 	RSF standard output (containing refl data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   down rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   weight rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lam float  -  1. 		operator scaling for inversion 
Param:  niter int  -  100 		maximum number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  rect1 int  -  3 		
Param:  rect2 int  -  3 		smoothing radius 

