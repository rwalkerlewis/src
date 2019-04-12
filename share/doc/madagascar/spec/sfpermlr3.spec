[sfpermlr3]
Cat:    RSF/user/fomels
Desc:   Lowrank decomposition for 2-D prestack exploding reflector in V(x,z)
DocCmd: sfpermlr3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		regularization
LDesc:  (defaults to: 0.0)
Param:  equation   -   -  		equation type
LDesc:  (defaults to: 3)
Param:  nh   -   -  		
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sub   -   -  		if subtract one
LDesc:  (defaults to: true)
Param:  tol   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)

