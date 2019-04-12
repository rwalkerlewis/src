[sfencode]
Cat:    RSF/user/psava
Desc:   shot encoding with arbitrary delays
DocCmd: sfencode | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  verb enum-bool  -  n 		verbosity flag 

