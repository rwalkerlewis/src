[sfhmiss]
Cat:    RSF/user/gee
Desc:   Multi-dimensional missing data interpolation with shaping regularization
DocCmd: sfhmiss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  lag string  -   -  		
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  n int-list  -   -  		 [dim]
Param:  niter int  -  100 		Number of iterations 
Param:  ns int  -   -  		scaling 
Param:  verb enum-bool  -  y 		verbosity flag 

