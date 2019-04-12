[sfclrmatrix]
Cat:    RSF/user/lexing
Desc:   Lowrank matrix decomposition for a complex matrix
DocCmd: sfclrmatrix | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   name rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

