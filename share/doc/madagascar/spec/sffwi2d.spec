[sffwi2d]
Cat:    RSF/user/pyang
Desc:   Time domain full waveform inversion
DocCmd: sffwi2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing vinit data)
Port:   stdout rsf w req 	RSF standard output (containing vupdates data)
Port:   grads rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   illums rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   objs rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   shots rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		number of iterations 
Param:  precon enum-bool  -  n 		precondition or not 
Param:  rbell int  -  2 		radius of bell smooth 
Param:  verb enum-bool  -  y 		vebosity 

