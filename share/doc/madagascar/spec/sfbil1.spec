[sfbil1]
Cat:    RSF/user/fomels
Desc:   Bi-variate L1 regression
DocCmd: sfbil1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reg rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  10 		number of POCS iterations 
Param:  perc float  -  90.0 		percentage for sharpening 

