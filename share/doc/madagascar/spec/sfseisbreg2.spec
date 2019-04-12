[sfseisbreg2]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation in 2D using seislet and Bregman shaping iteration
DocCmd: sfseisbreg2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization parameter 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  20 		number of iterations 
Param:  oper string  -   -  		[bregman,thresholding] method, the default is bregman  
Param:  order int  -  1 		accuracy order 
Param:  perc float  -  99. 		percentage for soft thresholding 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  n 		verbosity flag 

