[sfofd2_test]
Cat:    RSF/user/jsun
Desc:   2-D Fourth-order Optimized Finite-difference wave extrapolation
DocCmd: sfofd2_test | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   G rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  isx int  -   -  		
Param:  isz int  -   -  		
Param:  nt int  -   -  		

