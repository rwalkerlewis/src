[sfzowei]
Cat:    RSF/user/psava
Desc:   3-D zero-offset modeling/migration
DocCmd: sfzowei | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fdat data)
Port:   stdout rsf w req 	RSF standard output (containing Fcic data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adjoint flag, true for migration, false for modeling 
Param:  verb enum-bool  -  n 		verbosity flag 

