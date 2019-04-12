[sfpermlr2]
Cat:    RSF/user/fomels
Desc:   Lowrank decomposition for 2-D prestack exploding reflector in V(z)
DocCmd: sfpermlr2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  nh   -   -  		
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  tol   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)

