[sffdtacc]
Cat:    RSF/user/jsun
Desc:   2-D Fourth-order Finite-difference wave extrapolation with timing option (no ABC)
DocCmd: sffdtacc | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  timer enum-bool  -   -  		setup I/O files 
LDesc:  (defaults to: 0)
Param:  verb enum-bool  -   -  		
LDesc:  (defaults to: 0)

