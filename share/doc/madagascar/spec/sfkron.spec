[sfkron]
Cat:    RSF/user/fomels
Desc:   Kroneker product with square matrices
DocCmd: sfkron | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mat1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mat2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -  0. 		regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  niter int  -  100 		maximum number of iterations 
Param:  nliter int  -  1 		number of nonlinear iterations 

