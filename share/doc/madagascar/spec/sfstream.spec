[sfstream]
Cat:    RSF/user/fomels
Desc:   Streaming PEF
DocCmd: sfstream | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag (for linear operator) 
Param:  eps float  -   -  		regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  known string  -   -  		known data locations (optional) (auxiliary input file name)
Param:  na int  -   -  		PEF filter size (not including leading one) 
Param:  pattern string  -   -  		pattern data (for linear operator) (auxiliary input file name)
Param:  pef string  -   -  		output PEF (optional) (auxiliary output file name)

