[sftkirinv]
Cat:    RSF/user/seisinv
Desc:   2-D least-squares Kirchhoff pre-stack time migration with different regul
DocCmd: sftkirinv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  amp enum-bool  -  y 		if y, use amplitue factor 
Param:  antialias float  -  1.0 		antialiasing 
Param:  apt float  -   -  		migration aperture 
LDesc:  (defaults to: ncmp)
Param:  cdp0 float  -   -  		
LDesc:  (defaults to: cmp0)
Param:  dcdp float  -   -  		
LDesc:  (defaults to: dcmp)
Param:  err string  -   -  		output file for error 
Param:  fdip string  -   -  		auxiliary input file name
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  ncdp int  -   -  		
LDesc:  (defaults to: ncmp)
Param:  niter int  -  5 		number of iterations 
Param:  nw int  -  3 		
Param:  offset string  -   -  		auxiliary input file name
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  reg int  -  0 		regularization type 
Param:  rho float  -   -  		Leaky integration constant 
LDesc:  (defaults to: 1.-1./nt)
Param:  verb enum-bool  -  n 		verbosity flag 

