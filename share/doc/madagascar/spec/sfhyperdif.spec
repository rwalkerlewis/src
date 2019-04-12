[sfhyperdif]
Cat:    RSF/user/chenyk
Desc:   Solving 1-D transportation equation using finite difference algorithm
DocCmd: sfhyperdif | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dinit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   dtrue rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		temporal sampling 
Param:  dx float  -   -  		spatial sampling 
Param:  nt int  -   -  		number of temporal points 
Param:  nx int  -   -  		number of spatial points 
Param:  ox float  -   -  		spatial starting point 
Param:  type string  -   -  		[upwind, friedrichs, wendroff] get the type for solving hyperbola partial differential equation, the default is upwind 
Param:  wantinit enum-bool  -  n 		if want initial value. y: want, n: don't want. 
Param:  wanttrue enum-bool  -  n 		if want true solution. y: want, n: don't want. 

