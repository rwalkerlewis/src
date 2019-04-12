[sflsm_dsr2d]
Cat:    RSF/user/seisinv
Desc:   2-D prestack least-squares migration with split-step DSR
DocCmd: sflsm_dsr2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   error rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   slowness rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.004 		time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  niter int  -  10 		number of iterations 
Param:  npad int  -  0 		padding on offset wavenumber 
Param:  nr int  -  1 		maximum number of references 
Param:  nt int  -  1 		taper size 
Param:  verb enum-bool  -  n 		verbosity flag 

