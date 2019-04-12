[sfsphase]
Cat:    RSF/user/yliu
Desc:   Smooth estimate of instantaneous phase
DocCmd: sfsphase | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  niter int  -  100 		number of iterations 
Param:  order int  -  10 		Hilbert transformer order 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 

