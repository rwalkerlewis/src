[sfpde2dadp]
Cat:    RSF/user/browaeys
Desc:   Numerical solution of linear pde 2-d (X-Z-a) for phase space escape positions, angle and traveltime
DocCmd: sfpde2dadp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   slow rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowz rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cvgce string  -   -  		output file for convergence 
Param:  iq int  -   -  		switch for escape variable 0=x, 1=a, 2=t, 3=z 
Param:  is_xinf int  -   -  		
Param:  is_zinf int  -   -  		
Param:  ixsmooth int  -   -  		
Param:  izsmooth int  -   -  		
Param:  method int  -   -  		
Param:  method_2d int  -   -  		
Param:  niter int  -  100 		number of Gauss-Seidel iterations 
Param:  tol float  -   -  		accuracy tolerance 
LDesc:  (defaults to: 0.000002*nx*nz)
Param:  xsmooth float  -   -  		
Param:  zsmooth float  -   -  		

