[sfsc]
Cat:    RSF/user/fomels
Desc:   Surface-consistent decomposition
DocCmd: sfsc | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   index rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  error string  -   -  		prediction (auxiliary output file name)
Param:  niter int  -  0 		number of iterations 
Param:  prec enum-bool  -  y 		if apply preconditioning 
Param:  pred string  -   -  		prediction (auxiliary output file name)

