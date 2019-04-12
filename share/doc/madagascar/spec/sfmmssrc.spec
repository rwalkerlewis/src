[sfmmssrc]
Cat:    RSF/user/fangg
Desc:   Source for the method of manufactured solution
DocCmd: sfmmssrc | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel data)
Port:   stdout rsf w req 	RSF standard output (containing Fsrc data)
Port:   mslt rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  alpha float  -  1.0e-2 		source parameter
Param:  beta float  -  1.0 		source parameter
Param:  dt float  -   -  		time step
Param:  nt int  -   -  		number of time step
Param:  slx float  -   -  		center of source location: x
LDesc:  (defaults to: nx*dx*0.5)
Param:  slz float  -   -  		center of source location: z
LDesc:  (defaults to: nz*dz*0.5)

