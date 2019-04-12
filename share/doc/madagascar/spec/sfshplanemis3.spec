[sfshplanemis3]
Cat:    RSF/user/pwd
Desc:   Missing data interpolation in 3-D using plane-wave shaping regularization
DocCmd: sfshplanemis3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of iterations 
Param:  ns1 int  -  1 		
Param:  ns2 int  -  1 		smoothing radius 
Param:  order1 int  -  1 		
Param:  order2 int  -  1 		accuracy order 

