[sfradonoper]
Cat:    RSF/user/yliu
Desc:   Linear Radon operator
DocCmd: sfradonoper | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		if y, perform adjoint operation 
Param:  dp float  -   -  		p sampling (if adj=y) 
Param:  dx float  -   -  		
Param:  np int  -   -  		number of p values (if adj=y) 
Param:  nx int  -   -  		number of offsets (if adj=n) 
Param:  ox float  -   -  		
Param:  p0 float  -   -  		p origin (if adj=y) 
Param:  parab enum-bool  -  n 		if y, parabolic Radon transform 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x0 float  -  1. 		reference offset 

