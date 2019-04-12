[sfhelmrhs]
Cat:    RSF/user/sparse
Desc:   Reconstruct right-hand side from wavefield
DocCmd: sfhelmrhs | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  model string  -   -  		auxiliary input file name
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  uts int  -  0 		number of OMP threads 

