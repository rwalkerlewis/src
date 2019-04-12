[sflinmig2]
Cat:    RSF/user/dmerzlikin
Desc:   2-D Kirchhoff time migration with antialiasing with adjoint flag
DocCmd: sflinmig2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias string  -   -  		antialiasing type [triangle,flat,steep,none] 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  dd enum-bool  -  y 		differentiation in the data domain 
Param:  doomp enum-bool  -  y 		perform OpenMP optimization 
Param:  hd enum-bool  -  y 		half derivative 
Param:  n1 int  -   -  		
Param:  ps enum-bool  -  y 		spherical divergence 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)

