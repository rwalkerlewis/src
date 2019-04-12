[sfpp2psang]
Cat:    RSF/system/seismic
Desc:   Transform PP angle gathers to PS angle gathers
DocCmd: sfpp2psang | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vpvs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  nw int  -  4 		accuracy level 

