[sftxsorth]
Cat:    RSF/user/yliu
Desc:   Streaming orthogonalize signal and noise in t-x domain
DocCmd: sftxsorth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing fnoi2 data)
Port:   noise rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sig2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  gamma1 float  -   -  		Regularization in t direction, gamma_t in equations 18 and 20 
Param:  gamma2 float  -   -  		Regularization in x direction, gamma_x in equations 18 and 20 

