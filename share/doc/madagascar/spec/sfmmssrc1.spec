[sfmmssrc1]
Cat:    RSF/user/fangg
Desc:   1D Source for the method of manufactured solution
DocCmd: sfmmssrc1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel data)
Port:   stdout rsf w req 	RSF standard output (containing Fsrc data)
Port:   mslt rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  alpha float  -  1.0e-2 		source parameter
Param:  beta float  -  1.0 		source parameter
Param:  dt float  -   -  		time step
Param:  nt int  -   -  		number of time step
Param:  slx float  -   -  		center of source location: x
LDesc:  (defaults to: nx*dx*0.5)

