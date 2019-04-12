[sftest1_matchl1]
Cat:    RSF/user/lcasasan
Desc:   L1 1D matched filter
DocCmd: sftest1_matchl1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  mult string  -   -  		auxiliary input file name
Param:  nb int  -  3 		matched-filter order 
Param:  niter int  -  100 		number of POCS iterations 
Param:  perc float  -  90.0 		percentage for sharpening 
Param:  verb enum-bool  -  n 		verbosity flag 

