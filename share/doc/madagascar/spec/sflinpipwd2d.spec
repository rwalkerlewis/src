[sflinpipwd2d]
Cat:    RSF/user/dmerzlikin
Desc:   pi operator building wrapping test function flat gaussian weighting smoothing after pi
DocCmd: sflinpipwd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias string  -   -  		antialiasing type [triangle,flat,steep,none] 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  dd enum-bool  -  y 		differentiation in the data domain 
Param:  domod enum-bool  -  y 		if perform modeling via Kirchhoff 
Param:  doomp enum-bool  -  y 		OMP is forced currently 
Param:  dopi enum-bool  -  y 		if do pi 
Param:  eps float  -  0.001 		damper for pi 
Param:  epst2 float  -  0.001 		damper for t2warp 
Param:  hd enum-bool  -  y 		half differentiation 
Param:  nj1 int  -  1 		antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		threshold for tail elimination 
Param:  ps enum-bool  -  y 		spherical divergence 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  sm enum-bool  -  y 		if perform derivative filtering = PWD 
Param:  v_1 float  -   -  		
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		
Param:  verb enum-bool  -  y 		verbosity flag 

