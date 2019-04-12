[sffastpwd]
Cat:    RSF/user/chen
Desc:   2-D dip estimation using analytical equation
DocCmd: sffastpwd | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  niter int  -  100 		number of iterations 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing radius 
Param:  verb enum-bool  -  y 		verbosity 

