[sfanisodiffuse]
Cat:    RSF/user/dmerzlikin
Desc:   Anisotropic diffusion by regularized inversion. Applied in 3D in a slice by slice fashion: set of
DocCmd: sfanisodiffuse | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vy rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1. 		regularization parameter 
Param:  niter int  -  10 		number of conjugate-gradient iterations 
Param:  repeat int  -  1 		number of smoothing iterations 

