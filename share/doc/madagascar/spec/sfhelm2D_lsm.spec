[sfhelm2D_lsm]
Cat:    RSF/user/hzhu
Desc:   2D Frequency Domain Least Squares Reverse Time Migration
DocCmd: sfhelm2D_lsm | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   misfit rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  niter int  -  0 		Number of iterations 
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  receiver string  -   -  		auxiliary input file name
Param:  record string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		

