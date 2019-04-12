[sfcurvature]
Cat:    RSF/user/parvaneh
Desc:   Curvature
DocCmd: sfcurvature | cat
Port:   stdin  rsf r req 	RSF standard input (containing hor data)
Port:   stdout rsf w req 	RSF standard output (containing cur data)
Param:  rotation enum-bool  -  n 		if y: rotation, if n: convergence 
Param:  scale float  -  1.0 		scaling (from time to depth) 
Param:  vscale float  -  1.0 		scaling (from time to depth) 
Param:  what string  -   -  		what to compute 

