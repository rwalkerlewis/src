[sfpiazpwdmig3]
Cat:    RSF/user/dmerzlikin
Desc:   Least-Squares 3D Path-Summation Integral, Azimuthal Plane-Wave Destruction and Kirchhoff Modeling/Migration Chain of Operators
DocCmd: sfpiazpwdmig3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   az rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		Adjoint flag 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias string  -   -  		antialiasing type [triangle,flat,steep,none] 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  domod enum-bool  -  y 		if perform Kirchhoff modeling/migration 
Param:  doomp enum-bool  -  n 		OpenMP 
Param:  dopi enum-bool  -  y 		if perform PI filtering 
Param:  eps float  -  0.001 		Damper for pi 
Param:  epst2 float  -  0.001 		Damper for t2warp 
Param:  nj1 int  -  1 		antialiasing iline 
Param:  nj2 int  -  1 		antialiasing xline 
Param:  order int  -  1 		accuracy order 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		Threshold for tail elimination 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  sm enum-bool  -  y 		if perform AzPWD filtering 
Param:  v_1 float  -   -  		Path-integral range 
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		
Param:  vel float  -   -  		migration velocity for Kirchhoff 

