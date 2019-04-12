[sfrect1]
Cat:    RSF/user/fomels
Desc:   1-D covariance estimator
DocCmd: sfrect1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing rct data)
Param:  eps float  -   -  		regularization 
LDesc:  (defaults to: 0.0f)
Param:  niter int  -  100 		number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  verb enum-bool  -  y 		verbosity 

