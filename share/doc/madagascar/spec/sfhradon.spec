[sfhradon]
Cat:    RSF/user/chenyk
Desc:   Time domain high-resolution hyperbolic Radon transform
DocCmd: sfhradon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  N1 int  -  10 		CG Iterations (Internal loop) 
Param:  N2 int  -  3 		Update of weights for the sparse solution, N1 = 1 LS , N2 > 3 for High Res (Sparse) solution 
Param:  adj enum-bool  -  n 		if implement the adjoint transform instead of the inverse transform 
Param:  dh float  -   -  		
Param:  dv float  -   -  		
Param:  h0 float  -   -  		
Param:  inv enum-bool  -  y 		if implement the inverse transform 
Param:  nh int  -   -  		
Param:  nv int  -   -  		
Param:  offset string  -   -  		auxiliary input file name
Param:  solver enum-bool  -  n 		if use Madagascar bigsolver, default is not 
Param:  v0 float  -   -  		
Param:  vel string  -   -  		auxiliary input file name
Param:  verb int  -  0 		If output the debugging process 

