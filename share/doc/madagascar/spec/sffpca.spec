[sffpca]
Cat:    RSF/user/chen
Desc:   Fast PCA by iterative algorithm
DocCmd: sffpca | cat
Port:   stdin  rsf r req 	RSF standard input (containing pin data)
Port:   stdout rsf w req 	RSF standard output (containing pout data)
Param:  nc int  -  1 		component number
Param:  niter int  -  1 		iterations for each component
Param:  seed int  -  2012 		seed for random number

