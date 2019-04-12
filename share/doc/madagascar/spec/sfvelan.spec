[sfvelan]
Cat:    RSF/user/ediazp
Desc:   font.size
DocCmd: sfvelan | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsemb data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   cmp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   offset rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  half enum-bool  -  y 		half or full offset?
Param:  useoffset enum-bool  -  y 		if irregular offset, pass it

