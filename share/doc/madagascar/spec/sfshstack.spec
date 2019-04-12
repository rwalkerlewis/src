[sfshstack]
Cat:    RSF/user/kregimbal
Desc:   Shaping stack
DocCmd: sfshstack | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing stack data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  fhi float  -   -  		High frequency in band, default is Nyquist 
Param:  flo float  -   -  		Low frequency in band, default is 0 
Param:  h0 float  -  0. 		reference offset 
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  jump int  -  1 		subsampling 
Param:  niter int  -  10 		number of iterations 
Param:  nphi int  -  6 		number of poles for high cutoff 
Param:  nplo int  -  6 		number of poles for low cutoff 
Param:  offset string  -   -  		auxiliary input file name
Param:  restart int  -   -  		GMRES memory 
LDesc:  (defaults to: niter)
Param:  slowness enum-bool  -  n 		if y, use slowness instead of velocity 
Param:  tol float  -  1e-5 		GMRES tolerance 

