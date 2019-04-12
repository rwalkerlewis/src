[sfditime3d]
Cat:    RSF/user/aklokov
Desc:   3D Hybrid Radon transform for diffraction imaging in the time dip-angle domain
DocCmd: sfditime3d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reflMod rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dip0d float  -   -  		dip0 sampling (if adj=y) 
Param:  dip0n int  -   -  		number of dip0 values (if adj=y) 
Param:  dip0o float  -   -  		dip0 origin (if adj=y) 
Param:  dipd float  -   -  		dip sampling in x-direction 
Param:  dipn int  -   -  		number of dips in x-direction 
Param:  dipo float  -   -  		dip origin in x-direction 
Param:  dweight string  -   -  		input file containing data weights (auxiliary input file name)
Param:  eps float  -  0. 		regularization parameter 
Param:  invMod int  -  2 		number of nonlinear iterations (for inversion) 
Param:  isAA enum-bool  -  n 		if y, apply anti-aliasing 
Param:  liter int  -  100 		number of linear iterations (for inversion) 
Param:  niter int  -  0 		number of nonlinear iterations (for inversion) 
Param:  sdip0d float  -   -  		sdip0 sampling (if adj=y) 
Param:  sdip0n int  -   -  		number of sdip0 values (if adj=y) 
Param:  sdip0o float  -   -  		sdip0 origin (if adj=y) 
Param:  sdipd float  -   -  		dip sampling in y-direction 
Param:  sdipn int  -   -  		number of dips in y-direction 
Param:  sdipo float  -   -  		dip origin in y-direction 
Param:  sxid float  -   -  		xi sampling (if adj=y) 
Param:  sxin int  -   -  		number of xi values (if adj=y) 
Param:  sxio float  -   -  		xi origin (if adj=y) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  xid float  -   -  		xi sampling (if adj=y) 
Param:  xin int  -   -  		number of xi values (if adj=y) 
Param:  xio float  -   -  		xi origin (if adj=y) 

