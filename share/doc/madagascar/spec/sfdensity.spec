[sfdensity]
Cat:    RSF/user/jyan
Desc:   Compute density
DocCmd: sfdensity | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   inW rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   inY rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   inZ rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  n1 int  -  20 		verbosity flag 
Param:  n2 int  -  20 		verbosity flag 
Param:  n3 int  -  20 		verbosity flag 
Param:  n4 int  -  20 		verbosity flag 
Param:  verb enum-bool  -  n 		verbosity flag 

