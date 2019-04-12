[sftrace2]
Cat:    RSF/user/fomels
Desc:   2-D multiple arrivals by cell ray tracing
DocCmd: sftrace2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing outp data)
Port:   grid rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   size rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  a0 float  -  -90. 		initial angle (in degrees) 
Param:  da float  -  3.1 		angle increment (in degrees) 
Param:  lsint enum-bool  -  n 		if use least-squares interpolation 
Param:  maxa float  -   -  		
LDesc:  (defaults to: 2.*da)
Param:  maxsplit int  -  10 		maximum splitting for adaptive grid 
Param:  maxx float  -   -  		
LDesc:  (defaults to: 2.*dx)
Param:  mina float  -   -  		
LDesc:  (defaults to: 0.5*da)
Param:  minx float  -   -  		parameters for adaptive grid 
LDesc:  (defaults to: 0.5*dx)
Param:  na int  -  60 		number of angles 
Param:  order int  -  3 		velocity interpolation order 
Param:  vel enum-bool  -  y 		y: velocity, n: slowness 

