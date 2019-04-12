[sfshapesigk]
Cat:    RSF/user/pwd
Desc:   Signal component separation using plane-wave shaping
DocCmd: sfshapesigk | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dips rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  50 		maximum number of iterations 
Param:  rect1 int  -  1 		vertical smoothing radius 
Param:  rect2 int  -  1 		lateral smoothing radius 
Param:  verb enum-bool  -  n 		verbosity flag 

