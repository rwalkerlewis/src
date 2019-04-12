[sfmiss3]
Cat:    RSF/user/fomels
Desc:   Missing data interpolation (N-dimensional) using shaping regularization
DocCmd: sfmiss3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  force enum-bool  -  y 		if y, keep known values 
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  niter int  -  100 		Number of iterations 

