[sfewelr3grad]
Cat:    RSF/user/jsun
Desc:   None
DocCmd: sfewelr3grad | cat
Port:   stdin  rsf r req 	RSF standard input (containing c11 data)
Port:   C11dx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   C12dy rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   C13dz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   c14 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   theta rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt   -   -  		time step size
LDesc:  (defaults to: 1.e-3)
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  grad   -   -  		include gradient term
LDesc:  (defaults to: false)
Param:  jump   -   -  		jump step for reduced lowrank decomposition
LDesc:  (defaults to: 1)
Param:  mode   -   -  		mode of decomposition: 0->mixed, 1->p, 2->s
LDesc:  (defaults to: 0)
Param:  nb   -   -  		boundary padding
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  tilt   -   -  		tilting of TTI
LDesc:  (defaults to: false)
Param:  tric   -   -  		triclinic anisotropy
LDesc:  (defaults to: false)
Param:  verb   -   -  		verbosity flag
LDesc:  (defaults to: false)

