[sfdzest2d]
Cat:    RSF/user/zhiguang
Desc:   Estimation of depth-delay of common-image gathers
DocCmd: sfdzest2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fnp data)
Port:   stdout rsf w req 	RSF standard output (containing Fs data)
Port:   Fp rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if adj=y, adjoint operator 
Param:  eps1 float  -  0. 		shaping regularization parameter 
Param:  eps2 float  -  1e3 		regularization parameter in model constraint 
Param:  inv enum-bool  -  n 		if inv=y, perform inversion 
Param:  niter int  -  100 		number of iterations 
Param:  rect1 int  -  3 		shaping smoothing parameter in 1st axis 
Param:  rect2 int  -  3 		shaping smoothing parameter in 2nd axis 
Param:  seed int  -  0 		index of reference trace 
Param:  shape enum-bool  -  n 		if shape=y, use projection method 

