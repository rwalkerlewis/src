[sfseismis2]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation in 2-D using seislet transform
DocCmd: sfseismis2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cnum int  -   -  		Max cutting in cutting operator, default is n2 
LDesc:  (defaults to: n2)
Param:  cut enum-bool  -  n 		cutting flag, the default is shaping 
Param:  eps float  -  0.01 		regularization parameter 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  20 		number of iterations 
Param:  oper string  -   -  		[destruction,construction,shaping,pocs,bregman] method, the default is shaping  
Param:  order int  -  1 		accuracy order 
Param:  orderc float  -  1. 		Curve order for cutting operator, default is linear 
Param:  ordert float  -  1. 		Curve order for thresholding operator, default is linear 
Param:  perc float  -  99. 		percentage for soft-thresholding 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  n 		verbosity flag 

