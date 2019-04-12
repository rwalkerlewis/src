[sfseisavf]
Cat:    RSF/user/yliu
Desc:   1-D amplitude versus frequency (AVF) analysis with 1-D seislet frames
DocCmd: sfseisavf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   thr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ncycle int  -  0 		number of iterations 
Param:  niter int  -  1 		number of Bregman iterations 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb enum-bool  -  y 		verbosity flag 

