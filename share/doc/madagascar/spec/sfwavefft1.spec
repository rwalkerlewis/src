[sfwavefft1]
Cat:    RSF/user/songxl
Desc:   1-D finite-difference wave extrapolation
DocCmd: sfwavefft1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   grad rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  nt int  -   -  		if y, determine optimal size for efficiency 
Param:  opt enum-bool  -  y 		

