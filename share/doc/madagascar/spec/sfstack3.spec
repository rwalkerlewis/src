[sfstack3]
Cat:    RSF/user/psava
Desc:   OpenMP stack on axis 1,2 or 3
DocCmd: sfstack3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Param:  axis int  -  2 		stack axis 
Param:  nbuf int  -  1 		buffer size 
Param:  verb enum-bool  -  y 		verbosity flag 

