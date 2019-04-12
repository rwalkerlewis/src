[sfshape]
Cat:    RSF/user/fomels
Desc:   Non-stationary smoothing by shaping regularization
DocCmd: sfshape | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   limit rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))

