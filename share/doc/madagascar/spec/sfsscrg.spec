[sfsscrg]
Cat:    RSF/user/chen
Desc:   Extract common reciever gathers from simultaneous data
DocCmd: sfsscrg | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   delay rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  jt int  -  1 		subsampling [nps] in observation 
Param:  nt int  -   -  		
LDesc:  (defaults to: n1)

