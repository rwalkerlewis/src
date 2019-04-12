[sfgsrayvti]
Cat:    RSF/user/roman
Desc:   Gauss Seidel iterative solver for phase space escape positions, angle and traveltime
DocCmd: sfgsrayvti | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velz rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  iq int  -   -  		switch for escape variable 0=x, 1=a, 2=t, 3=z, 4=l 
Param:  niter int  -  50 		number of Gauss-Seidel iterations 
Param:  tol float  -   -  		accuracy tolerance 
LDesc:  (defaults to: 0.000002*nx*nz)
Param:  vti string  -   -  		what to compute (p=qP, v=qSV, h=SH) 
Param:  vti_delta float  -  0.0 		VTI constants Thomsen  
Param:  vti_eps float  -  0.0 		
Param:  vti_gamma float  -  0.0 		

