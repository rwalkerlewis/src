[sfllpf]
Cat:    RSF/user/fomels
Desc:   Local prediction filter (n-dimensional) with an adjoint flag
DocCmd: sfllpf | cat
Port:   stdin  rsf r req 	RSF standard input (containing mat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Port:   basis rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		
Param:  niter int  -  100 		number of iterations 
Param:  verb enum-bool  -  y 		verbosity flag 

