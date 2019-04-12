[sfmatchoper]
Cat:    RSF/user/yliu
Desc:   Local matching-radon operator
DocCmd: sfmatchoper | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  anti float  -  1. 		antialiasing, only when freq=n 
Param:  dp float  -   -  		p sampling 
Param:  freq enum-bool  -  y 		if y, parabolic Radon transform 
Param:  niter int  -  100 		number of iterations 
Param:  np int  -   -  		number of p values 
Param:  p0 float  -   -  		p origin 
Param:  p1 float  -  0. 		reference slope, only when freq=n 
Param:  parab enum-bool  -  n 		if y, parabolic Radon transform, only when freq=y 
Param:  pclip float  -  100. 		
Param:  rho enum-bool  -  y 		rho filtering, only when freq=n 
Param:  shift int  -   -  		
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary output file name
Param:  x0 float  -  1. 		reference offset 

