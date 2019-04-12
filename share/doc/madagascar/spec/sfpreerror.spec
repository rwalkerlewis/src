[sfpreerror]
Cat:    RSF/user/chenyk
Desc:   Prediction error
DocCmd: sfpreerror | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   predict rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  type int  -  1 		if compute relative error, 1: yes, 0: no, default is yes. 

