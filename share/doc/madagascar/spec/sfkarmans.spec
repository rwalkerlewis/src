[sfkarmans]
Cat:    RSF/user/browaeys
Desc:   Inversion for von Karman autocorrelation 1D spectrum
DocCmd: sfkarmans | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   prm rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  x10 float  -  6. 		initial nonlinear parameter x1 value 
Param:  x20 float  -  -0.5 		initial nonlinear parameter x2 value 
Param:  x30 float  -  200. 		initial nonlinear parameter x3 value 

