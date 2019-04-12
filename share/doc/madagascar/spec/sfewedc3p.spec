[sfewedc3p]
Cat:    RSF/user/jsun
Desc:   None
DocCmd: sfewedc3p | cat
Port:   stdin  rsf r req 	RSF standard input (containing c11 data)
Port:   c14 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   theta rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt   -   -  		time step size
LDesc:  (defaults to: 1.e-3)
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
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

