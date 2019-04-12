[sfnfmiss]
Cat:    RSF/user/gchliu
Desc:   Missing data interpolation in freq domain
DocCmd: sfnfmiss | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  exact enum-bool  -  y 		If y, preserve the known data values 
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  niter int  -   -  		number of iterations 
LDesc:  (defaults to: n1)
Param:  ty string  -   -  		Prediction type: all=backward+forward
Param:  verb enum-bool  -  n 		verbosity flag 

