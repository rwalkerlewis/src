[sfcisolr2grad]
Cat:    RSF/user/jsun
Desc:   Complex lowrank decomposition for 2-D isotropic wave propagation (including velocity gradient term)
DocCmd: sfcisolr2grad | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   grad1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   grad2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

