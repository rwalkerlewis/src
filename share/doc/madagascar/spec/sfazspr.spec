[sfazspr]
Cat:    RSF/user/dmerzlikin
Desc:   Combining Sprays: Simply Input Sprays in In-line And Cross-line
DocCmd: sfazspr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   az rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   spry rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  nj1 int  -  1 		antialiasing iline 
Param:  nj2 int  -  1 		antialiasing xline 
Param:  order int  -  1 		accuracy order 
Param:  sm enum-bool  -  y 		if perform AzPWD filtering 

