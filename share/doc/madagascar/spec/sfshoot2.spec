[sfshoot2]
Cat:    RSF/system/seismic
Desc:   2-D ray shooting
DocCmd: sfshoot2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dr float  -   -  		receiver increment 
LDesc:  (defaults to: dx)
Param:  lsint enum-bool  -  n 		if use least-squares interpolation 
Param:  nr int  -  1 		number of recievers 
Param:  nt int  -   -  		Maximum number of time steps 
LDesc:  (defaults to: nx*nz)
Param:  order int  -  4 		Interpolation order 
Param:  r0 float  -   -  		first receiver 
LDesc:  (defaults to: x0)
Param:  shotfile string  -   -  		file with shot locations (auxiliary input file name)
Param:  tol float  -  0.01 		Shooting tolerance (in degrees) 
Param:  vel enum-bool  -  y 		If y, the input is velocity; if n, slowness 

