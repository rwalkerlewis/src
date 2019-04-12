[sfapefsignoi]
Cat:    RSF/user/yliu
Desc:   Signal and noise separation using adaptive PEFs
DocCmd: sfapefsignoi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   nfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sfilt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  niter int  -  100 		Number of iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

