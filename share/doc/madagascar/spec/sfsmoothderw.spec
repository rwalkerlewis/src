[sfsmoothderw]
Cat:    RSF/user/fomels
Desc:   Convert input to its derivative using LS and shaping regularization
DocCmd: sfsmoothderw | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing modl data)
Param:  niter int  -  100 		maximum number of iterations 
Param:  rect# string  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  weight string  -   -  		auxiliary input file name

