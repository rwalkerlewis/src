[sfgsray]
Cat:    RSF/user/browaeys
Desc:   Gauss Seidel iterative solver for phase space escape positions, angle and traveltime
DocCmd: sfgsray | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dtout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   slow rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowz rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dslow string  -   -  		auxiliary input file name
Param:  iq int  -   -  		switch for escape variable 0=x, 1=a, 2=t, 3=z, 4=l, 5=i 
Param:  liter int  -  0 		number of first iterations with low-order scheme 
Param:  niter int  -  50 		number of Gauss-Seidel iterations 
Param:  order int  -  1 		order of upwind 
Param:  sph enum-bool  -  n 		true - half-sphere, false - flat B.C. on left/right 
Param:  tol float  -   -  		accuracy tolerance 
LDesc:  (defaults to: 0.000002*nx*nz)
Param:  verb enum-bool  -  n 		verbosity flag 

