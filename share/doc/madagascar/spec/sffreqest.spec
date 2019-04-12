[sffreqest]
Cat:    RSF/user/fomels
Desc:   Local frequency estimation
DocCmd: sffreqest | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  hertz enum-bool  -  n 		if y, convert output to Hertz 
Param:  niter int  -  100 		number of iterations 

