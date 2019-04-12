[sffrog]
Cat:    RSF/user/gee
Desc:   Simple 2-D wave propagation
DocCmd: sffrog | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  type int  -  0 		Laplacian type 
Param:  verb enum-bool  -  n 		verbosity 

