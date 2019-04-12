[sfditime2d]
Cat:    RSF/user/aklokov
Desc:   2D Hybrid Radon transform for diffraction imaging in the time dip-angle domain
DocCmd: sfditime2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   reflMod rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dip0d float  -   -  		dip0 sampling (if adj=y) 
Param:  dip0n int  -   -  		number of dip0 values (if adj=y) 
Param:  dip0o float  -   -  		dip0 origin (if adj=y) 
Param:  dipd float  -   -  		offset sampling 
Param:  dipn int  -   -  		number of offsets 
Param:  dipo float  -   -  		offset origin 
Param:  dweight string  -   -  		input file containing data weights (auxiliary input file name)
Param:  eps float  -  0. 		regularization parameter 
Param:  invMod int  -  2 		number of nonlinear iterations (for inversion) 
Param:  isAA enum-bool  -  n 		if y, apply anti-aliasing 
Param:  liter int  -  100 		number of linear iterations (for inversion) 
Param:  niter int  -  0 		number of nonlinear iterations (for inversion) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  xid float  -   -  		xi sampling (if adj=y) 
Param:  xin int  -   -  		number of xi values (if adj=y) 
Param:  xio float  -   -  		xi origin (if adj=y) 

