[sflstri2d]
Cat:    RSF/user/jsun
Desc:   2-D passive seismic RTM and its adjoint
DocCmd: sflstri2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  abc enum-bool  -  n 		absorbing boundary condition 
Param:  adj enum-bool  -  n 		adjoint flag, 0: modeling, 1: migration 
Param:  cb float  -   -  		allocate arrays 
LDesc:  (defaults to: 0.0f)
Param:  ctr enum-bool  -  n 		CTR IC flag 
Param:  depth int  -  0 		acquisition surface 
Param:  geop string  -   -  		auxiliary input file name
Param:  hard float  -   -  		hard thresholding 
LDesc:  (defaults to: 0.0f)
Param:  inv enum-bool  -  n 		inversion flag 
Param:  ngrp int  -  1 		number of groups of receivers 
Param:  niter int  -  0 		number of iterations 
Param:  perc float  -   -  		stable division padding percentage (of max) 
LDesc:  (defaults to: SF_EPS)
Param:  prec enum-bool  -  n 		use ctr as precondioner 
Param:  rectt int  -  1 		smoothing radius in t 
Param:  rectx int  -  1 		smoothing radius in x 
Param:  rectz int  -  1 		smoothing radius in z 
Param:  repeat int  -  1 		smoothing repeatation 
Param:  size int  -  0 		sliding window size 
Param:  stack int  -  1 		local stacking length 
Param:  sw enum-bool  -  n 		inversion flag 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary input file name

