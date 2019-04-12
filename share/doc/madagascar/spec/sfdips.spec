[sfdips]
Cat:    RSF/user/pwd
Desc:   Estimate a number of constant dips using plane-wave destruction
DocCmd: sfdips | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dips float-list  -   -  		initial dips  [nd]
Param:  nd int  -   -  		number of dips 
Param:  niter int  -  10 		number of iterations 
Param:  nj int  -  1 		antialiasing 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity flag 

