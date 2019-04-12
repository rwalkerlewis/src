[sfaxplusy]
Cat:    RSF/user/jeff
Desc:   Computes a*x + y, where x and y are datasets, and a is scalar

DocCmd: sfaxplusy | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   afile rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   y rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a double  -   -  		Scaling factor 
LDesc:  (defaults to: 1)
Param:  verb enum-bool  -  n 		Verbosity flag 

