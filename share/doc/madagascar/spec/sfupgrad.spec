[sfupgrad]
Cat:    RSF/user/fomels
Desc:   Causal gradient operator
DocCmd: sfupgrad | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dim int  -   -  		
Param:  grad enum-bool  -  y 		if y, gradient; if n, Laplacian 

