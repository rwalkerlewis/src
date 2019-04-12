[sfunfault]
Cat:    RSF/user/zhiguang
Desc:   Unfault image
DocCmd: sfunfault | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mask rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   shift rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  inv enum-bool  -  n 		
Param:  lam float  -  1 		regularization 
Param:  mode enum-bool  -  y 		
Param:  niter int  -  100 		number of iterations 
Param:  off int  -  2 		offset to fault 

