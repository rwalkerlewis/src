[sfcisolr2abc1]
Cat:    RSF/user/jsun
Desc:   Complex lowrank decomposition for 2-D isotropic wave propagation with absorbing boundaries
DocCmd: sfcisolr2abc1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cb   -   -  		
LDesc:  (defaults to: 0.0)
Param:  cl   -   -  		
LDesc:  (defaults to: 0.0)
Param:  cr   -   -  		
LDesc:  (defaults to: 0.0)
Param:  ct   -   -  		
LDesc:  (defaults to: 0.0)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  nbb   -   -  		
LDesc:  (defaults to: 0)
Param:  nbl   -   -  		
LDesc:  (defaults to: 0)
Param:  nbr   -   -  		
LDesc:  (defaults to: 0)
Param:  nbt   -   -  		
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  rev   -   -  		reversal
LDesc:  (defaults to: false)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

