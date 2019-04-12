[sflinmig3]
Cat:    RSF/user/dmerzlikin
Desc:   3-D Kirchhoff time migration with antialiasing with adjoint flag
DocCmd: sflinmig3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  angle float  -  90.0 		angle aperture 
Param:  antialias string  -   -  		antialiasing type [triangle,flat,steep,none] 
Param:  apt int  -   -  		integral aperture 
LDesc:  (defaults to: nx)
Param:  doomp enum-bool  -  n 		perform OpenMP optimization 
Param:  n1 int  -   -  		
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  vel float  -   -  		migration velocity 

