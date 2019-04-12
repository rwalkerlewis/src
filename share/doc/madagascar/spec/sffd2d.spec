[sffd2d]
Cat:    RSF/user/jsun
Desc:   2-D Fourth-order Finite-difference wave extrapolation with ABC
DocCmd: sffd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  c float  -  0.01 		decaying parameter 
Param:  nb int  -  30 		boundary length 
Param:  verb enum-bool  -   -  		setup I/O files 
LDesc:  (defaults to: 0)

