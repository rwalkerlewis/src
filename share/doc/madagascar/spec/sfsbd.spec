[sfsbd]
Cat:    RSF/user/songxl
Desc:   1-D finite-difference wave extrapolation
DocCmd: sfsbd | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   grad rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  what int  -  2 		2nd or 4th order for FD

