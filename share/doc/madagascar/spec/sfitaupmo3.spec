[sfitaupmo3]
Cat:    RSF/system/seismic
Desc:   3-D Inverse taup normal moveout
DocCmd: sfitaupmo3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		stretch regularization 
Param:  extend int  -  8 		trace extension 
Param:  interval enum-bool  -  y 		use interval velocity 
Param:  slow enum-bool  -  n 		slowness [y] or velocity [n] squared

