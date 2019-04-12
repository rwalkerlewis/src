[sfttieikonal]
Cat:    RSF/user/uwaheed
Desc:   Fast sweeping TTI eikonal solver (2D)
DocCmd: sfttieikonal | cat
Port:   stdin  rsf r req 	RSF standard input (containing vzf data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Param:  delta string  -   -  		
Param:  epsilon string  -   -  		
Param:  nfpi int  -  3 		number of fixed-point iterations 
Param:  niter int  -  4 		number of sweeping iterations 
Param:  shotfile string  -   -  		File with shot locations (n2=number of shots, n1=3) 
Param:  theta string  -   -  		
Param:  yshot float  -   -  		
LDesc:  (defaults to: o2 + 0.5*(n2-1)*d2)
Param:  zshot float  -  0. 		Shot location (used if no shotfile) 

