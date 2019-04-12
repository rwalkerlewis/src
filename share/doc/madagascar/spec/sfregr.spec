[sfregr]
Cat:    RSF/user/fomels
Desc:   Linear regression
DocCmd: sfregr | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reg rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  method int  -  2 		method (L1-like or L2) 
Param:  n1iter int  -  10 		number of POCS iterations 
Param:  niter int  -  10 		number of CG iterations 
Param:  perc float  -  90.0 		percentage for sharpening 
Param:  verb enum-bool  -  n 		verbosity flag 

