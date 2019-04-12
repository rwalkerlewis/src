[sfdecibel]
Cat:    RSF/user/psava
Desc:   Decibel
DocCmd: sfdecibel | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fou data)
Param:  aref float  -  1.0 		reference amplitude 
Param:  inv enum-bool  -  n 		inverse transform 
Param:  verb enum-bool  -  n 		verbosity flag 

