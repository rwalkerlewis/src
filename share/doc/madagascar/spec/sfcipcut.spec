[sfcipcut]
Cat:    RSF/user/cwp
Desc:   cut at CIPs
DocCmd: sfcipcut | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fcub data)
Port:   stdout rsf w req 	RSF standard output (containing Fcut data)
Port:   cip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  verb enum-bool  -  n 		verbosity flag 

