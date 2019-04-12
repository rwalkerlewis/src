[sfreorder]
Cat:    RSF/user/zgeng
Desc:   Reorder the data according to the path
DocCmd: sfreorder | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   path rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  inv enum-bool  -  n 		if y, do inverse transform 

