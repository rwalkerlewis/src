[sfradius]
Cat:    RSF/user/sgreer
Desc:   Estimate smoothing radius (min = 1)
DocCmd: sfradius | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  c float  -  1. 		
Param:  maxrad float  -  1000. 		

