[sfpipwdmig2]
Cat:    RSF/user/dmerzlikin
Desc:   Chain of Path Integral, Plane-Wave Destruction and Kirchhoff migration (based on sfmig2)
DocCmd: sfpipwdmig2 | cat
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
Param:  domod enum-bool  -  y 		if perform modeling via Kirchhoff (if disabled -> chain = P PWD) 
Param:  doomp enum-bool  -  y 		OMP flag - currently hard-coded to y 
Param:  eps float  -  0.001 		damper for pi 
Param:  epst2 float  -  0.001 		damper for t2warp 
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  hd enum-bool  -  y 		half derivative 
Param:  nj1 int  -  1 		antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		threshold for tail elimination 
Param:  pi enum-bool  -  y 		if perform Path-Integral filtering (if disabled -> chain = PWD L) 
Param:  ps enum-bool  -  y 		amplitude correction 
Param:  rho float  -   -  		leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  sm enum-bool  -  y 		if perform Plane-Wave destruction (if disabled -> chain = P L) 
Param:  v_1 float  -   -  		no pass velocity 
Param:  v_2 float  -   -  		first pass velocity 
Param:  v_3 float  -   -  		second pass velocity 
Param:  v_4 float  -   -  		no pass velocity 
Param:  verb enum-bool  -  n 		verbose flag 

