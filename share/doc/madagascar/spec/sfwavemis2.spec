[sfwavemis2]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation in 2-D using wavelet transform and compressive sensing
DocCmd: sfwavemis2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mask string  -   -  		auxiliary input file name
Param:  nbreg int  -  1 		number of iterations for Bregman iteration 
Param:  niter int  -  20 		number of iterations 
Param:  oper string  -   -  		[shaping,pocs,bregman] method, the default is shaping  
Param:  ordert float  -  1. 		Curve order for thresholding parameter, default is linear 
Param:  perc float  -  99. 		percentage for soft-thresholding 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb enum-bool  -  n 		verbosity flag 

