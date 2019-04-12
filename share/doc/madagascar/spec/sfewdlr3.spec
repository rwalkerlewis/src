[sfewdlr3]
Cat:    RSF/user/jsun
Desc:   None
DocCmd: sfewdlr3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing c11 data)
Port:   c14 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   theta rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt   -   -  		time step size
LDesc:  (defaults to: 1.e-3)
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  jump   -   -  		jump step for reduced lowrank decomposition
LDesc:  (defaults to: 1)
Param:  mode   -   -  		wavefield decomposition mode (0->slow S, 1->fast S, 2->P)
LDesc:  (defaults to: 0)
Param:  nb   -   -  		boundary padding
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  tau   -   -  		smoothing radius
LDesc:  (defaults to: 1.e-1)
Param:  tilt   -   -  		tilting of TTI
LDesc:  (defaults to: false)
Param:  tric   -   -  		triclinic anisotropy
LDesc:  (defaults to: false)
Param:  verb   -   -  		verbosity flag
LDesc:  (defaults to: false)

