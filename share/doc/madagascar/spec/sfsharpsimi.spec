[sfsharpsimi]
Cat:    RSF/user/yliu
Desc:   Sharpen similarity measure between two datasets
DocCmd: sfsharpsimi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization parameter 
Param:  niter int  -  20 		number of iterations 
Param:  perc float  -  98. 		percentage for sharpen, default is 98
Param:  verb enum-bool  -  n 		verbosity flag 

