[sfpwdchain]
Cat:    RSF/user/pwd
Desc:   Nonstationary Prony by chain of PEFs
DocCmd: sfpwdchain | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  liter int  -  50 		number of linear iterations 
Param:  nc int  -  1 		number of components 
Param:  niter int  -  0 		number of iterations 
Param:  order int  -  1 		PWD order 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing radius 
Param:  verb enum-bool  -   -  		verbosity flag 
LDesc:  (defaults to: (bool) (1 == nt))

