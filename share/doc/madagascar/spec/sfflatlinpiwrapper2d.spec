[sfflatlinpiwrapper2d]
Cat:    RSF/user/dmerzlikin
Desc:   pi operator building wrapping test function flat gaussian weighting smoothing after pi
DocCmd: sfflatlinpiwrapper2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		kirchhoff parameters 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias float  -  1.0 		antialiasing 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  dh float  -   -  		offset sampling (for modeling) 
Param:  diff# enum-bool  -   -  		differentiation on #-th axis 
LDesc:  (defaults to: (n,n,...))
Param:  domod enum-bool  -  y 		
Param:  eps float  -  0.001 		
Param:  epst2 float  -  0.001 		
Param:  gather string  -   -  		auxiliary output file name
Param:  h0 float  -   -  		first offset (for modeling) 
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  nh int  -   -  		number of offsets (for modeling) 
Param:  normalize enum-bool  -  y 		normalize for the fold 
Param:  offset string  -   -  		auxiliary input file name
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		
Param:  pifk string  -   -  		auxiliary output file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  repeat int  -  1 		repeat filtering several times 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  sm enum-bool  -  y 		if y, do adjoint integration 
Param:  v_1 float  -   -  		
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		
Param:  verb enum-bool  -  y 		verbosity flag 

