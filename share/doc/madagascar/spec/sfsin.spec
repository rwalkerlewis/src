[sfsin]
Cat:    RSF/system/seismic
Desc:   Simple operations with complex sinusoids
DocCmd: sfsin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   root rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -   -  		scaling for shaping inversion 
LDesc:  (defaults to: 1./n1)
Param:  mask string  -   -  		missing data interpolation (auxiliary input file name)
Param:  niter int  -  0 		number of iterations 
Param:  oper string  -   -  		operation to perform 
Param:  perc float  -  50. 		percentage for thresholding (used when oper=t and niter > 0) 
Param:  rect int  -  1 		smoothing radius (for oper=s) 
Param:  type string  -   -  		[haar,linear,biortho] type of the seislet transform 
Param:  verb enum-bool  -  n 		verbosity flag 

