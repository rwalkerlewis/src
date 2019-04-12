[sfofd1]
Cat:    RSF/user/songxl
Desc:   1-D Optimized finite-difference wave extrapolation
DocCmd: sfofd1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   G rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  isx int  -   -  		
LDesc:  (defaults to: (int)(nx/2))
Param:  nt int  -   -  		

