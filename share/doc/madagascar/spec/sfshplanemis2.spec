[sfshplanemis2]
Cat:    RSF/user/pwd
Desc:   Missing data interpolation in 2-D using plane-wave shaping regularization
DocCmd: sfshplanemis2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of iterations 
Param:  ns int  -  1 		smoothing radius 
Param:  order int  -  1 		accuracy order 

