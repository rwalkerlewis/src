[sftranslate]
Cat:    RSF/user/luke
Desc:   
DocCmd: sftranslate | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  adj enum-bool  -  n 		if y reverse translation, if n, translation 
Param:  trans string  -   -  		auxiliary input file name
Param:  x1 float  -  0. 		fixed translation in first dimension 
Param:  x2 float  -  0. 		fixed translation in second dimension 

