[sftxspf]
Cat:    RSF/user/yliu
Desc:   Streaming prediction filter in t-x domain
DocCmd: sftxspf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a int-list  -   -  		Get filter size from input, a0 is 2M+1, a1 is N in equation 3  [dim]
Param:  lambda1 float  -   -  		Regularization in t direction, lambda_t in equations 1 and 5 
Param:  lambda2 float  -   -  		Regularization in x direction, lambda_x in equations 1 and 5 

