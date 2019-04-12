[sfpwd2]
Cat:    RSF/user/yliu
Desc:   2-D plane wave destruction
DocCmd: sfpwd2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nj1 int  -  1 		aliasing 
Param:  order int  -  1 		accuracy 
Param:  verb enum-bool  -  n 		verbosity flag 

