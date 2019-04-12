[sfconjgrad]
Cat:    RSF/system/main
Desc:   Generic conjugate-gradient solver for linear inversion
DocCmd: sfconjgrad | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing to data)
Port:   mod rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  known string  -   -  		auxiliary input file name
Param:  mwt string  -   -  		auxiliary input file name
Param:  niter int  -  1 		number of iterations 
Param:  x0 string  -   -  		auxiliary input file name

