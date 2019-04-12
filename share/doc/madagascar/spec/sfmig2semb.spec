[sfmig2semb]
Cat:    RSF/user/dmerzlikin
Desc:   2-D Prestack Kirchhoff time migration with antialiasing
DocCmd: sfmig2semb | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   semblance rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adjoint flag (y for migration, n for modeling) 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias float  -  1.0 		antialiasing 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  dh float  -   -  		offset sampling (for modeling) 
Param:  gather string  -   -  		auxiliary output file name
Param:  h0 float  -   -  		first offset (for modeling) 
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  nh int  -   -  		number of offsets (for modeling) 
Param:  normalize enum-bool  -  y 		normalize for the fold 
Param:  offset string  -   -  		auxiliary input file name
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  verb enum-bool  -  y 		verbosity flag 

