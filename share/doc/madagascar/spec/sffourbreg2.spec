[sffourbreg2]
Cat:    RSF/user/yliu
Desc:   Missing data interpolation in 2-D using Fourier Bregman shaping iteration
DocCmd: sffourbreg2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  error enum-bool  -  n 		error verbosity flag 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  20 		number of iterations 
Param:  perc float  -  99. 		percentage for soft-thresholding 
Param:  res string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

