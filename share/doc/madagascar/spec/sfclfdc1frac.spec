[sfclfdc1frac]
Cat:    RSF/user/jsun
Desc:   1D 10th-order Lowrank Onestep FD coefficient
DocCmd: sfclfdc1frac | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Param:  SIZE   -   -  		stencil size
Param:  cpxexp   -   -  		complex exponential
LDesc:  (defaults to: true)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  mode   -   -  		symbol
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  perc   -   -  		cutoff percentage
LDesc:  (defaults to: 50)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

