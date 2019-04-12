[sfwave2dss]
Cat:    RSF/user/songxl
Desc:   1-D finite-difference wave extrapolation
DocCmd: sfwave2dss | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   grad1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   grad2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nb1 int  -  20 		x boundary nodes 
Param:  nb2 int  -  20 		z boundary nodes
Param:  sl int  -   -  		source location
LDesc:  (defaults to: nx/2)
Param:  what int  -  2 		2nd or 4th order for FD

