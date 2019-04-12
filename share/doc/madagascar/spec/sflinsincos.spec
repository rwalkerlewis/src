[sflinsincos]
Cat:    RSF/system/seismic
Desc:   Solve for angle in equation vx*sin(d) + vy*cos(d) = 1/s0
DocCmd: sflinsincos | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  da float  -   -  		angle sampling. 
Param:  dr float  -   -  		radius sampling. 
LDesc:  (defaults to: dvx)
Param:  dt float  -  2. 		polar angle sampling. 
Param:  extend int  -  4 		tmp extension 
Param:  na int  -   -  		number of angle values. 
Param:  nr int  -   -  		number of radius on radial lines 
LDesc:  (defaults to: nvx/2)
Param:  nt int  -  180 		number of polar angle for integration. 
Param:  oa float  -   -  		angle origin 
Param:  ot float  -  0. 		polar angle origin 
Param:  s0 float  -   -  		reference slowness 

