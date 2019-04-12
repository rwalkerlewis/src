[sfpwdecon]
Cat:    RSF/user/gchliu
Desc:   Deconvolution with known wavelelt using pwc to control sparsity
DocCmd: sfpwdecon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dips rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wav rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cut_p enum-bool  -  y 		cut off value of precondition 
Param:  eps float  -  0. 		regularization parameter 
Param:  niter int  -  50 		maximum number of iterations 
Param:  nliter int  -  1 		number of reweighting iterations 
Param:  order int  -  1 		accuracy order 
Param:  reg int  -  0 		cut off value of precondition 
Param:  sparse enum-bool  -  y 		if sparse = ture   sparse deconvolution cauchy-norm
LDesc:            if reg = 0: regularization A = |I|
LDesc:            if reg = 1:  regularization A = |PWD|
LDesc:         if sparse = false  2-norn deconvolution regularization A = ||I||
LDesc:      
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  weight string  -   -  		auxiliary output file name

