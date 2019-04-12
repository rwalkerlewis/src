[sfpick31]
Cat:    RSF/user/yliu
Desc:   Automatic picking from 3D semblance-like panels plus additional axis
DocCmd: sfpick31 | cat
Port:   stdin  rsf r req 	RSF standard input (containing scn data)
Port:   stdout rsf w req 	RSF standard output (containing pik data)
Param:  an1 float  -  1. 		
Param:  an2 float  -  1. 		axes anisotropy 
Param:  gate1 int  -  3 		
Param:  gate2 int  -  3 		picking gate 
Param:  niter int  -  100 		number of iterations 
Param:  rect1 int  -  1 		smoothing radius 
Param:  smooth enum-bool  -  y 		if apply smoothing 
Param:  vel1 float  -   -  		
LDesc:  (defaults to: o2)
Param:  vel2 float  -   -  		surface velocity 
LDesc:  (defaults to: o3)
Param:  verb enum-bool  -  y 		verbosity 

