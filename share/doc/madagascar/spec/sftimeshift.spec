[sftimeshift]
Cat:    RSF/user/pwd
Desc:   Apply variable time shifts using plane-wave construction
DocCmd: sftimeshift | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 

