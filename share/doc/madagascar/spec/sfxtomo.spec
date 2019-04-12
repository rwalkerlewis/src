[sfxtomo]
Cat:    RSF/user/gee
Desc:   Kjartansson-style tomography
DocCmd: sfxtomo | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  dh float  -   -  		
LDesc:  (defaults to: dz)
Param:  dx float  -   -  		
LDesc:  (defaults to: dy)
Param:  dy float  -   -  		
LDesc:  (defaults to: dx)
Param:  dz float  -   -  		
LDesc:  (defaults to: dh)
Param:  nh int  -   -  		
LDesc:  (defaults to: nz)
Param:  niter int  -  -1 		number of iterations 
Param:  nx int  -   -  		
LDesc:  (defaults to: ny)
Param:  ny int  -   -  		
LDesc:  (defaults to: nx)
Param:  nz int  -   -  		
LDesc:  (defaults to: nh)
Param:  oh float  -   -  		
LDesc:  (defaults to: oz)
Param:  ox float  -   -  		
LDesc:  (defaults to: oy)
Param:  oy float  -   -  		
LDesc:  (defaults to: ox)
Param:  oz float  -   -  		
LDesc:  (defaults to: oh)

