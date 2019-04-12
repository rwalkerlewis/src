[sfstreamiss]
Cat:    RSF/user/fomels
Desc:   Missing data interpolation using streaming PEF
DocCmd: sfstreamiss | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   known rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -   -  		regularization 
Param:  na int  -   -  		PEF filter size (not including leading one) 
Param:  pef string  -   -  		output PEF (optional) (auxiliary output file name)

