[sfpp2psang2]
Cat:    RSF/system/seismic
Desc:   Transform PP angle gathers to PS angle gathers
DocCmd: sfpp2psang2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vpvs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  nw int  -  4 		accuracy level 
Param:  verb enum-bool  -  n 		

