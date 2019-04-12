[sfmonof2]
Cat:    RSF/system/generic
Desc:   Gaussian wavelet estimation in 2-D
DocCmd: sfmonof2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ma rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  a0 float  -  1. 		starting sharpness in xx 
Param:  b0 float  -  0. 		starting sharpness in xy 
Param:  c0 float  -  1. 		starting sharpness in yy 
Param:  niter int  -  100 		number of iterations 
Param:  nliter int  -  1 		number of reweighting iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

