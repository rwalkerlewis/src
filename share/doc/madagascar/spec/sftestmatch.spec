[sftestmatch]
Cat:    RSF/user/yliu
Desc:   Test linear matching operator
DocCmd: sftestmatch | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		if y, perform adjoint operation 
Param:  verb enum-bool  -  n 		verbosity flag 

