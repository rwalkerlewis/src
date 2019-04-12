[sfrickback]
Cat:    RSF/user/tsai
Desc:   None linear Ricker wavelet spectral fit
DocCmd: sfrickback | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  gamma string  -   -  		auxiliary output file name
Param:  m float-list  -   -  		 [n]
Param:  n int  -   -  		
Param:  niter int  -  100 		
Param:  verb enum-bool  -  n 		

