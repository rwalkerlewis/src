[sfcgconst]
Cat:    RSF/user/llisiw
Desc:   Test Beam for constant velocity gradient
DocCmd: sfcgconst | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  b float  -  0. 		velocity gradient 
Param:  p float  -   -  		
LDesc:  (defaults to: 1/v0)
Param:  source float  -   -  		real source point 
LDesc:  (defaults to: o2)
Param:  v0 float  -  1. 		surface velocity 
Param:  w float  -  0. 		beam width 

