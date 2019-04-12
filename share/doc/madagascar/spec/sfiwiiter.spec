[sfiwiiter]
Cat:    RSF/user/sparse
Desc:   Image-domain waveform tomography
DocCmd: sfiwiiter | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   riter rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cgiter int  -  10 		number of conjugate-gradient iterations 
Param:  load enum-bool  -  n 		load LU 
Param:  mass enum-bool  -  n 		if y, use discretization-based mass term 
Param:  miter string  -   -  		auxiliary output file name
Param:  model string  -   -  		auxiliary input file name
Param:  nh int  -  0 		horizontal space-lag 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  precon string  -   -  		auxiliary input file name
Param:  rect1 int  -  1 		smoothing radius on axis 1 
Param:  rect2 int  -  1 		smoothing radius on axis 2 
Param:  reg float  -  0. 		regularization parameter 
Param:  shape enum-bool  -  n 		regularization (default Tikhnov) 
Param:  tol float  -  1.e-6 		tolerance for shaping regularization 
Param:  ur string  -   -  		auxiliary input file name
Param:  us string  -   -  		auxiliary input file name
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary input file name

