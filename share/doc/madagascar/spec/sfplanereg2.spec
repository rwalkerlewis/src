[sfplanereg2]
Cat:    RSF/user/pwd
Desc:   Data regularization in 2-D using plane-wave destruction
DocCmd: sfplanereg2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization parameter 
Param:  head string  -   -  		
Param:  interp int  -  2 		interpolation length 
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity flag 

