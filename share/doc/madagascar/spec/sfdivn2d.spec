[sfdivn2d]
Cat:    RSF/user/chen
Desc:   2D divn
DocCmd: sfdivn2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing radius 
Param:  verb enum-bool  -  n 		verbosity 

