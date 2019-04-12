[sfdivnls]
Cat:    RSF/user/chen
Desc:   2D divn by stationary LS
DocCmd: sfdivnls | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  angle enum-bool  -  n 		angle or slope 
Param:  rect1 int  -  0 		
Param:  rect2 int  -  0 		
Param:  rect3 int  -  0 		smoothing radius 
Param:  tls enum-bool  -  n 		total least squares 

