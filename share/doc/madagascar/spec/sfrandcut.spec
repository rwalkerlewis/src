[sfrandcut]
Cat:    RSF/user/psava
Desc:   cut a random dataset from a 3D cube
DocCmd: sfrandcut | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   rr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  axis int  -  2 		stack axis 
Param:  verb enum-bool  -  n 		verbosity flag 

