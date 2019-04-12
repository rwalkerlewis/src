[sfzfraclr2]
Cat:    RSF/user/jsun
Desc:   Complex lowrank decomposition for 2-D viscoacoustic isotropic wave propagation
DocCmd: sfzfraclr2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing right data)
Port:   fft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  abc   -   -  		
LDesc:  (defaults to: 0)
Param:  avg   -   -  		whether use average value of gamma
LDesc:  (defaults to: false)
Param:  cb   -   -  		
LDesc:  (defaults to: 0.0)
Param:  cl   -   -  		
LDesc:  (defaults to: 0.0)
Param:  compen   -   -  		compensate attenuation, only works if mode=0,1 (viscoacoustic)
LDesc:  (defaults to: false)
Param:  cr   -   -  		
LDesc:  (defaults to: 0.0)
Param:  ct   -   -  		
LDesc:  (defaults to: 0.0)
Param:  cutoff   -   -  		cutoff frequency
LDesc:  (defaults to: 250.)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  gamma   -   -  		
Param:  mode   -   -  		mode of propagation: 0 is viscoacoustic (default); 1 is loss-dominated; 2 is dispersion dominated; 3 is acoustic
LDesc:  (defaults to: 0)
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
Param:  rev   -   -  		reverse propagation
LDesc:  (defaults to: false)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)
Param:  sign   -   -  		sign of solution: 0 is positive, 1 is negative
LDesc:  (defaults to: 0)
Param:  taper   -   -  		taper ratio for tukey window
LDesc:  (defaults to: 0.2)
Param:  vmax   -   -  		maximum velocity
LDesc:  (defaults to: 6000.)
Param:  w0   -   -  		reference frequency

