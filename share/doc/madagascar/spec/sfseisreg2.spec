[sfseisreg2]
Cat:    RSF/user/yliu
Desc:   Data regularization in 2-D using seislet transform
DocCmd: sfseisreg2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization parameter 
Param:  head string  -   -  		
Param:  interp int  -  2 		interpolation length 
Param:  niter int  -  50 		number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb enum-bool  -  n 		verbosity flag 

