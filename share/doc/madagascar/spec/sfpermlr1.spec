[sfpermlr1]
Cat:    RSF/user/fomels
Desc:   Lowrank decomposition for prestack exploding reflector in v(z)
DocCmd: sfpermlr1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   size rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 5)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

