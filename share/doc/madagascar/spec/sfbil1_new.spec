[sfbil1_new]
Cat:    RSF/user/lcasasan
Desc:   L1 regression 0 ~= d - G * m
DocCmd: sfbil1_new | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reg rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  Liter int  -  10 		number of CG iterations 
Param:  niter int  -  10 		number of POCS iterations 
Param:  perc float  -  90.0 		percentage for sharpening 
Param:  verb enum-bool  -  n 		

