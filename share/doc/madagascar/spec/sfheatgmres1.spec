[sfheatgmres1]
Cat:    RSF/user/petsc
Desc:   Solution of 1-D heat equation with GMRES
DocCmd: sfheatgmres1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing tinitial data)
Port:   stdout rsf w req 	RSF standard output (containing solution data)
Param:  Ta float  -  0 		Boundary condition on the left 
Param:  Tb float  -  0 		Boundary condition on the right 
Param:  alpha float  -   -  		Conductivity 
Param:  dt float  -   -  		Time step 
Param:  nt int  -   -  		Number of time steps 

