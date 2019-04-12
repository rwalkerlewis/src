[sfseispocs]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation using POCS added 2-D seislet transform
DocCmd: sfseispocs | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  convex string  -   -  		auxiliary input file name
Param:  eps float  -  0.01 		regularization parameter 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  20 		number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  perc float  -  90. 		percentage for smooth 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  n 		verbosity flag 

