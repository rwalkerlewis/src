[sfpcrsurv3]
Cat:    RSF/user/cram
Desc:   Prepare survey info for 3-D angle-domain migration
DocCmd: sfpcrsurv3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing survey data)
Param:  ehmax float  -  0.1 		Maximum edge length in the receiver triangulation 
Param:  esmax float  -  0.2 		Maximum edge length in the shot triangulation 
Param:  gxgy string  -   -  		File with receiver coordinates (auxiliary input file name)
Param:  sxsy string  -   -  		File with shot coordinates (auxiliary input file name)
Param:  tri enum-bool  -  n 		triangulation flag 
Param:  verb enum-bool  -  n 		verbosity flag 

