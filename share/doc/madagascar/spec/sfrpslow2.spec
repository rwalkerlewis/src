[sfrpslow2]
Cat:    RSF/user/cram
Desc:   Full angle-dependent slowness volume for 3-D reduced phase space
DocCmd: sfrpslow2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing spdom data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  na int  -  360 		Number of phase angles 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vspl string  -   -  		Spline coefficients for velocity model (auxiliary input file name)

