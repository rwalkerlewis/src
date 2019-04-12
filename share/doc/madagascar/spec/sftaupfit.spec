[sftaupfit]
Cat:    RSF/user/fomels
Desc:   Fitting tau-p approximations
DocCmd: sftaupfit | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coef rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fit rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  type string  -   -  		Type of approximation (iso,vti) 

