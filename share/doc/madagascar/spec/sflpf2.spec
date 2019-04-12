[sflpf2]
Cat:    RSF/user/yliu
Desc:   2D Local prediction filter
DocCmd: sflpf2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Port:   match rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		file with PEF lags (optional) 
Param:  niter int  -  100 		number of iterations 
Param:  pef string  -   -  		signal PEF file (optional) 
Param:  pred string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  y 		verbosity flag 

