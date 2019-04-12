[sfpick2]
Cat:    RSF/user/fomels
Desc:   Automatic picking from semblance-like panels (3-D input)
DocCmd: sfpick2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing scn data)
Port:   stdout rsf w req 	RSF standard output (containing pik data)
Param:  an float  -  1. 		axes anisotropy 
Param:  gate int  -  3 		picking gate 
Param:  niter int  -  100 		number of iterations 
Param:  rect1 int  -  1 		smoothing radius on the first axis 
Param:  rect2 int  -  1 		smoothing radius on the second axis 
Param:  slice int  -  0 		if only one kind of slicing (1: inline, 2: time) 
Param:  vel0 float  -   -  		surface velocity 
LDesc:  (defaults to: o2)

