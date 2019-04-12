[sfsymposolver]
Cat:    RSF/user/chenyk
Desc:   Symmetric positive definite matrix equation solver using square root method (cholesky decomposition method)
DocCmd: sfsymposolver | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   rhs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  n int  -   -  		
Param:  verb enum-bool  -  n 		

