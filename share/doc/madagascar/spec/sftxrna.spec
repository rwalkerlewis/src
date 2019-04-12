[sftxrna]
Cat:    RSF/user/yliu
Desc:   Causal t-x or t-x-y nonstationary regularized autoregression
DocCmd: sftxrna | cat
Port:   stdin  rsf r req 	RSF standard input (containing mat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Param:  a int-list  -   -  		 [mdim]
Param:  niter int  -  20 		number of iterations 
Param:  pred string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

