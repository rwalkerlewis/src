[sfpsmig]
Cat:    RSF/user/chenyk
Desc:   2-D Phase-shift modeling and migration
DocCmd: sfpsmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag, 0: modeling, 1: migration 
Param:  dw float  -   -  		
Param:  eps float  -   -  		stabilization parameter 
LDesc:  (defaults to: 0.1f)
Param:  nw int  -   -  		

