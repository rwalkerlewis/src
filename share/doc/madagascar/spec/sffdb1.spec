[sffdb1]
Cat:    RSF/user/songxl
Desc:   1-D Finite-difference wave extrapolation
DocCmd: sffdb1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  abc int  -  0 		absorbing boundary condition 1: cos 0: exp
Param:  dt float  -   -  		
Param:  nb int  -  20 		
Param:  nt int  -   -  		
Param:  order int  -  2 		FD order: 2,4

