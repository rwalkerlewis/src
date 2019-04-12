[sfortholrzone]
Cat:    RSF/user/jsun
Desc:   Lowrank decomposition for 3-D orthorhombic wave propagation with zone's approximation
DocCmd: sfortholrzone | cat
Port:   stdin  rsf r req 	RSF standard input (containing c11 data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   seta1 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  approx   -   -  		if true, use zone's approximation instead of exact phase velocity
LDesc:  (defaults to: false)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  mode   -   -  		'0' means quasi-P (default), '1' means quasi-S, '2' means quasi-S2
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  reduce   -   -  		if true, use the expirical linear relationship between qv and qh
LDesc:  (defaults to: false)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  tilt   -   -  		
LDesc:  (defaults to: false)

