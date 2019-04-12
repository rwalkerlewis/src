[sffwipe]
Cat:    RSF/user/zhiguang
Desc:   Phase encoding
DocCmd: sffwipe | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   newrec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   oldrec rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  encoding enum-bool  -  y 		
Param:  nsim int  -   -  		
LDesc:  (defaults to: ns)
Param:  nsource int  -  1 		check 
Param:  seed int  -   -  		
LDesc:  (defaults to: time(NULL))

