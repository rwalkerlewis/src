[sfpwdtensorh]
Cat:    RSF/user/dmerzlikin
Desc:   structure tensor estimation based on plane wave destruction
DocCmd: sfpwdtensorh | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   in2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   in3 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   out2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ux rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   uy rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vy rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eps float  -  0.00001 		
Param:  normalize enum-bool  -  n 		

