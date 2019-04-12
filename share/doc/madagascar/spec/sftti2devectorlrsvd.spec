[sftti2devectorlrsvd]
Cat:    RSF/user/chengjb
Desc:   None
DocCmd: sftti2devectorlrsvd | cat
Port:   stdin  rsf r req 	RSF standard input (containing vp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Elasticx data)
Port:   ElasticPx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ElasticPz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ElasticSx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ElasticSz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Elasticz rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt   -   -  		
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-6)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  ns   -   -  		
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

