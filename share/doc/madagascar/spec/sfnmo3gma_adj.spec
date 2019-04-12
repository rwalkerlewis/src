[sfnmo3gma_adj]
Cat:    RSF/system/seismic
Desc:   Fwd-Adj of 3D NMO GMA for iterative LS coefficient solve
DocCmd: sfnmo3gma_adj | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   gather rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mod rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   t0sq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		
Param:  nw int  -  16 		16 parameters of 3D GMA

