[sfodip2]
Cat:    RSF/user/pwd
Desc:   2-D dip estimation by omnidirectional plane wave destruction
DocCmd: sfodip2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  0. 		initial dip 
Param:  cos string  -   -  		initial dip (cosine) (auxiliary input file name)
Param:  liter int  -  50 		number of linear iterations 
Param:  niter int  -  5 		number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  rect1 int  -  1 		dip smoothness on 1st axis 
Param:  rect2 int  -  1 		dip smoothness on 2nd axis 
Param:  sin string  -   -  		initial dip (sine) (auxiliary input file name)
Param:  verb enum-bool  -  y 		verbosity flag 

