[sfwlslfdc1tw2]
Cat:    RSF/user/fangg
Desc:   None
DocCmd: sfwlslfdc1tw2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Port:   Mapp rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Mwatpw rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   tp rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   waw rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wfun rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  a0   -   -  		weight parameters
LDesc:  (defaults to: 0.0001)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  f0   -   -  		dominant frequency
LDesc:  (defaults to: 15)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  size   -   -  		stencil length
LDesc:  (defaults to: 6)
Param:  taper   -   -  		
LDesc:  (defaults to: true)
Param:  tpa   -   -  		taper for stability
LDesc:  (defaults to: 0.0)
Param:  tpb   -   -  		
LDesc:  (defaults to: 0.0)
Param:  weight   -   -  		
LDesc:  (defaults to: true)

