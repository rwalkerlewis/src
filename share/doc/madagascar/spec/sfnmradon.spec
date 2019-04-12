[sfnmradon]
Cat:    RSF/user/yliu
Desc:   Nonstationary-matching Radon transform
DocCmd: sfnmradon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, perform adjoint operation 
Param:  anti float  -  1. 		antialiasing, only when freq=n 
Param:  dp float  -   -  		p sampling 
Param:  dx float  -   -  		x sampling 
Param:  freq enum-bool  -  y 		if y, parabolic Radon transform 
Param:  inv enum-bool  -  n 		if y, perform inverse operation 
Param:  np int  -   -  		number of p values 
Param:  nx int  -   -  		number of x values 
Param:  ox float  -   -  		x origin 
Param:  p0 float  -   -  		p origin 
Param:  p1 float  -  0. 		reference slope, only when freq=n 
Param:  parab enum-bool  -  n 		if y, parabolic Radon transform, only when freq=y 
Param:  rho enum-bool  -  y 		rho filtering, only when freq=n 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary input file name
Param:  x0 float  -  1. 		reference offset 

