[sfrwe2d]
Cat:    RSF/user/jeff
Desc:   None
DocCmd: sfrwe2d | cat
Port:   Rimage rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   image rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rays rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dxx   -   -  		call from_par('dzz',dzz,az%d)
LDesc:  (defaults to: ax%d)
Param:  forward   -   -  		Forward scattering option
LDesc:  (defaults to: 0.)
Param:  kinematic   -   -  		Kinematic approximation
LDesc:  (defaults to: y)
Param:  norm   -   -  		Whether (1) or not (0) to normalize by gnorm
LDesc:  (defaults to: 1)
Param:  nref   -   -  		starting number of points for calculating reference velocities
LDesc:  (defaults to: 256)
Param:  nsx   -   -  		
LDesc:  (defaults to: 3)
Param:  nsz   -   -  		
LDesc:  (defaults to: 3)
Param:  verbose   -   -  		level of verbosity
LDesc:  (defaults to: n)
Param:  xmax   -   -  		
LDesc:  (defaults to: (ax%n-1)
Param:  xmin   -   -  		call from_par('zmin',zmin,az%o)
LDesc:  (defaults to: ax%o)
Param:  zmax   -   -  		
LDesc:  (defaults to: (az%n-1)

