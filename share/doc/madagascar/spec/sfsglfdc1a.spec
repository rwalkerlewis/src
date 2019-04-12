[sfsglfdc1a]
Cat:    RSF/user/fangg
Desc:   1D Lowrank FD coefficient of d/dx on staggered grid (optimized)
DocCmd: sfsglfdc1a | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Port:   Mexact rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sx rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  size   -   -  		stencil length
LDesc:  (defaults to: 6)
Param:  taper   -   -  		taper for stability
LDesc:  (defaults to: 1.e-3)
Param:  wavnumcut   -   -  		wavenumber cut percentile
LDesc:  (defaults to: 1.0)

