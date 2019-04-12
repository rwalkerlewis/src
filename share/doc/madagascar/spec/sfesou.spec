[sfesou]
Cat:    RSF/user/psava
Desc:   source for quasistatic electric potential
DocCmd: sfesou | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fpre data)
Port:   stdout rsf w req 	RSF standard output (containing Feso data)
Port:   qke rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ske rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  zbnd enum-bool  -  n 		boundary flag 

