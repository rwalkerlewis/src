[sfchaindr]
Cat:    RSF/user/dmerzlikin
Desc:   chain diffraction extraction debug version
DocCmd: sfchaindr | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   diffmod rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dipim rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   outdip rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   outpwd rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if perform derivative filtering = PWD 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias float  -  1.0 		antialiasing 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  debug enum-bool  -   -  		
Param:  dh float  -   -  		offset sampling (for modeling) 
Param:  domod enum-bool  -  y 		get regularization parameter 
Param:  eps float  -  0.001 		
Param:  epst2 float  -  0.001 		
Param:  gather string  -   -  		auxiliary output file name
Param:  h0 float  -   -  		first offset (for modeling) 
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  nh int  -   -  		number of offsets (for modeling) 
Param:  nj1 int  -  1 		antialiasing 
Param:  normalize enum-bool  -  y 		normalize for the fold 
Param:  offset string  -   -  		auxiliary input file name
Param:  order int  -  1 		accuracy order 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		
Param:  reg float  -  0.0 		debug flag 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  sm enum-bool  -  y 		if perform modelling via Kirchhoff 
Param:  v_1 float  -   -  		
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		
Param:  verb enum-bool  -  y 		verbosity flag 

