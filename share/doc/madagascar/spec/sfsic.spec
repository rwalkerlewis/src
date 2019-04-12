[sfsic]
Cat:    RSF/user/psava
Desc:   Local slant stacks I.C
DocCmd: sfsic | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  da float  -  1.0 		
Param:  dl float  -  1. 		
Param:  na int  -  1 		
Param:  nbuf int  -  1 		buffer size 
Param:  nl int  -  1 		
Param:  oa float  -  0.0 		
Param:  ol float  -  0. 		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  sig float  -  1.0 		
Param:  verb enum-bool  -  n 		verbosity flag 

