[sflocalsnr]
Cat:    RSF/user/yliu
Desc:   Local signal-to-noise ratio (SNR) estimation
DocCmd: sflocalsnr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   en rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  niter int  -  100 		number of inversion iterations 
Param:  nw int  -   -  		window length
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  stack enum-bool  -  y 		if y, window centre point, whereas window average
Param:  verb enum-bool  -  y 		verbosity flag 

