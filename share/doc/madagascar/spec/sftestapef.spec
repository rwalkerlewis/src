[sftestapef]
Cat:    RSF/user/yliu
Desc:   Test linear adaptive PEF operator
DocCmd: sftestapef | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   nfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		if y, perform adjoint operation 
Param:  sign enum-bool  -  y 		if y, test signal PEF; otherwise, test noise PEF 
Param:  verb enum-bool  -  n 		verbosity flag 

