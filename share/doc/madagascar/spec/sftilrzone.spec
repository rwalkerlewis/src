[sftilrzone]
Cat:    RSF/user/jsun
Desc:   Lowrank decomposition for 2-D anisotropic wave propagation using exact phase velocity (2 step time marching)
DocCmd: sftilrzone | cat
Port:   stdin  rsf r req 	RSF standard input (containing c11 data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  approx   -   -  		whether to use zone's approximation
LDesc:  (defaults to: false)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  mode   -   -  		wave mode (0=p wave, 1=Sv wave)
LDesc:  (defaults to: 0)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

