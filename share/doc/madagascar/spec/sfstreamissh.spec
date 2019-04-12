[sfstreamissh]
Cat:    RSF/user/gee
Desc:   Missing data interpolating using streaming PEF on a helix
DocCmd: sfstreamissh | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   known rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a int-list  -   -  		filter shape  [dim]
Param:  eps float  -   -  		regularization 
Param:  lag string  -   -  		auxiliary input file name
Param:  n int-list  -   -  		 [dim]
Param:  na int  -  0 		PEF filter size (not including leading one) 
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))
Param:  var float  -   -  		noise variance 
LDesc:  (defaults to: 0.0f)

