[sfmatch]
Cat:    RSF/system/generic
Desc:   Simple matching filtering
DocCmd: sfmatch | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  nf int  -   -  		filter size 

