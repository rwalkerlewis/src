[sfabalance]
Cat:    RSF/user/fomels
Desc:   Amplitude balancing
DocCmd: sfabalance | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  100 		Hilbert transformer order 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 
Param:  reverse enum-bool  -  y 		reverse weight 
Param:  weight string  -   -  		optional weight output (auxiliary output file name)

