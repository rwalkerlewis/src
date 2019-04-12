[sflrvc0]
Cat:    RSF/user/fomels
Desc:   Lowrank decomposition for zero-offset time migration
DocCmd: sflrvc0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing fft data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  fmin   -   -  		minimum frequency
LDesc:  (defaults to: dw)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  tmax   -   -  		
LDesc:  (defaults to: t0+(nt-1)
Param:  tol   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  v0   -   -  		minimum velocity
LDesc:  (defaults to: 0.0)

