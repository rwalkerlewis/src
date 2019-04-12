[sfpwsfault3]
Cat:    RSF/user/yliu
Desc:   3-D fault detection from plane-wave spray
DocCmd: sfpwsfault3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  niter int  -  20 		number of iterations 
Param:  ns2 int  -   -  		
Param:  ns3 int  -   -  		spray radius 
Param:  order int  -  1 		accuracy order 
Param:  perc float  -  98. 		percentage for sharpen, default is 98
Param:  type string  -   -  		[difference,sharpen_similarity] calculation type, the default is difference  
Param:  verb enum-bool  -  n 		verbosity 

