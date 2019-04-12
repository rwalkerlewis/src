[sfproj]
Cat:    RSF/user/gee
Desc:   Projection filter
DocCmd: sfproj | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularizion parameter 
LDesc:  (defaults to: 1.0f)
Param:  lag int  -  1 		lag for internal convolution 
Param:  niter int  -  100 		number of iterations 
Param:  single enum-bool  -  y 		single channel or multichannel 
Param:  verb enum-bool  -  n 		verbosity flag 

