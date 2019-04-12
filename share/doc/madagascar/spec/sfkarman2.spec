[sfkarman2]
Cat:    RSF/user/browaeys
Desc:   Estimation of von Karman autocorrelation 2D spectrum by nonlinear separable least squares
DocCmd: sfkarman2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -  1000. 		starting correlation length in xx 
Param:  b0 float  -  0. 		starting correlation length in xy 
Param:  c0 float  -  400. 		starting correlation length in yy 
Param:  niter int  -  100 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

