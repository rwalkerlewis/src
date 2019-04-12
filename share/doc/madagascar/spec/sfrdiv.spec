[sfrdiv]
Cat:    RSF/user/fomels
Desc:   Rough division
DocCmd: sfrdiv | cat
Port:   stdin  rsf r req 	RSF standard input (containing fnum data)
Port:   stdout rsf w req 	RSF standard output (containing frat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  niter int  -  100 		number of iterations 
Param:  niter2 int  -  1 		number of outer iterations 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  verb enum-bool  -  y 		verbosity 

