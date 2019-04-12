[sfpwddiffuse]
Cat:    RSF/user/dmerzlikin
Desc:   Anisotropic diffusion by regularized inversion. Instead of a gradient PWDs in inline and crossline directions are used. 3D
DocCmd: sfpwddiffuse | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vy rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag - when test=y 
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  10 		number of conjugate-gradient iterations 
Param:  nj1 int  -  1 		antialiasing iline 
Param:  nj2 int  -  1 		antialiasing xline 
Param:  order int  -  1 		accuracy order 
Param:  repeat int  -  1 		number of smoothing iterations 
Param:  sm enum-bool  -  y 		if perform PWD filtering 
Param:  test enum-bool  -  n 		test - applied in either forward or adjoint mode (no inversion) 

