[sfahpef]
Cat:    RSF/user/gee
Desc:   Adaptive multidimensional nonstationary PEF
DocCmd: sfahpef | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing filt data)
Param:  a int-list  -   -  		 [dim]
Param:  center int-list  -   -  		 [dim]
Param:  dim int  -   -  		number of dimensions 
LDesc:  (defaults to: ndim)
Param:  gap int-list  -   -  		 [dim]
Param:  lag string  -   -  		output file for filter lags 
Param:  maskin string  -   -  		optional input mask file (auxiliary input file name)
Param:  n int-list  -   -  		 [dim]
Param:  na int  -  0 		filter size 
Param:  niter int  -  100 		number of iterations 
Param:  res string  -   -  		output residual (optional) 
Param:  verb enum-bool  -  y 		verbosity flag 

