[sfthreshold3]
Cat:    RSF/user/yliu
Desc:   Automatic soft or hard thresholding
DocCmd: sfthreshold3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dist string  -   -  		[gaussian,rayleigh] distribution type, the default is gaussian 
Param:  type string  -   -  		[soft,hard] thresholding type, the default is soft  

