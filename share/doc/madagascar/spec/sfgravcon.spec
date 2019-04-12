[sfgravcon]
Cat:    RSF/user/yliu
Desc:   Continuation for gravity data by using FFT or intergral iteration
DocCmd: sfgravcon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  iter enum-bool  -  n 		if y, perform iteration method 
Param:  niter int  -  0 		continuation factor allocate memory 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  z float  -   -  		for iteration method 

