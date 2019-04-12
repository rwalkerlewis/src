[sfseishrink]
Cat:    RSF/user/yliu
Desc:   2-D Seislet shrinkage denoising
DocCmd: sfseishrink | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dwt enum-bool  -  n 		if y, dwt in vertical axis 
Param:  eps float  -  0.01 		regularization parameter 
Param:  hcurve string  -   -  		auxiliary output file name
Param:  lcurve string  -   -  		auxiliary output file name
Param:  norm string  -   -  		auxiliary output file name
Param:  nperc int  -  1 		number of percentage dimension 
Param:  order int  -  1 		accuracy order 
Param:  perc float  -  90. 		percentage for shrinkage 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  n 		verbosity flag 

