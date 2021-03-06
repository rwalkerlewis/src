[sfsglfdcx2_7]
Cat:    RSF/user/fangg
Desc:   2D Lowrank FD coefficient of d/dx on staggered grid (optimized)
DocCmd: sfsglfdcx2_7 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Port:   sx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sz rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 50)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  size   -   -  		stencil length
LDesc:  (defaults to: 6)
Param:  wavnumcut   -   -  		wavenumber cut percentile
LDesc:  (defaults to: 1.0)

