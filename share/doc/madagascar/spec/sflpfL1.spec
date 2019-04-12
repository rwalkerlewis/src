[sflpfL1]
Cat:    RSF/user/lcasasan
Desc:   Local prediction filter (n-dimensional) in L1 norm
DocCmd: sflpfL1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Port:   match rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		file with PEF lags (optional) 
Param:  liter int  -  10 		number of CG iterations 
Param:  niter int  -  25 		number of POCS iterations [L1]
Param:  pef string  -   -  		signal PEF file (optional) 
Param:  perc float  -  90.0 		percentage for sharpening [L1]
Param:  pred string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  y 		verbosity flag 

