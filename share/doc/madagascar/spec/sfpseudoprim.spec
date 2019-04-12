[sfpseudoprim]
Cat:    RSF/user/yliu
Desc:   Generate pseudoprimaries using multiples
DocCmd: sfpseudoprim | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  both enum-bool  -  n 		receiver flag, if y, receiver with both sides 
Param:  jumpo int  -  1 		jump in offset dimension, only for stack=n 
Param:  jumps int  -  1 		jump in shot dimension, only for stack=n  
Param:  mul string  -   -  		auxiliary input file name
Param:  stack enum-bool  -  y 		stack flag, if y, no common pseudoprimary gather 
Param:  verb enum-bool  -  n 		verbosity flag 

