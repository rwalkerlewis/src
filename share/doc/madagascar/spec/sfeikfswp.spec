[sfeikfswp]
Cat:    RSF/user/bash
Desc:   Fast sweeping eikonal solver (2-D/3-D)
DocCmd: sfeikfswp | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Param:  horizon string  -   -  		File with a reflection interface 
Param:  niter int  -  2 		number of sweeping iterations 
Param:  shotfile string  -   -  		File with shot locations (n2=number of shots, n1=3) 
Param:  vel enum-bool  -  y 		if y, the input is velocity; n - slowness 
Param:  xshot float  -   -  		
LDesc:  (defaults to: o3 + 0.5*(n3-1)*d3)
Param:  yshot float  -   -  		
LDesc:  (defaults to: o2 + 0.5*(n2-1)*d2)
Param:  zshot float  -  0. 		Shot location (used if no shotfile) 

