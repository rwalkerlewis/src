[sfcconst]
Cat:    RSF/user/llisiw
Desc:   Gaussian beam and exact complex eikonal for constant velocity medium
DocCmd: sfcconst | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  angle float  -  45. 		rotation angle (counter-clock wise with respect to vertically downward) 
Param:  s float  -  0. 		complex source shift 
Param:  source float  -   -  		real source point (on surface) 
LDesc:  (defaults to: o2)
Param:  v0 float  -  1. 		constant velocity background 
Param:  what string  -   -  		what to compute (default exact solution) 

