[sfapef2]
Cat:    RSF/user/yliu
Desc:   2D adaptive nonstationary PEF on aliased traces
DocCmd: sfapef2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing mat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Param:  a int-list  -   -  		 [mdim]
Param:  jump int  -  2 		Jump parameter 
Param:  maskin string  -   -  		optional input mask file (auxiliary input file name)
Param:  maskout string  -   -  		optional output mask file (auxiliary output file name)
Param:  niter int  -  100 		number of iterations 
Param:  pred string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

