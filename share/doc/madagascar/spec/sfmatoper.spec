[sfmatoper]
Cat:    RSF/user/chenyk
Desc:   Matrix algebra operation
DocCmd: sfmatoper | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mat rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  type string  -   -  		[mul, add, sub, dotmul] operation type, the default is mul  

