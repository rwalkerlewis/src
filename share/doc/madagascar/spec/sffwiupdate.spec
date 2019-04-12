[sffwiupdate]
Cat:    RSF/user/zhiguang
Desc:   Update model with search direction and step length in FWI
DocCmd: sffwiupdate | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   direction rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  alpha string  -   -  		auxiliary input file name
Param:  alpha0 float  -   -  		
Param:  max float  -  0. 		if max=0, no normalization; if max!=0, normalization by alpha*max/dmax 

