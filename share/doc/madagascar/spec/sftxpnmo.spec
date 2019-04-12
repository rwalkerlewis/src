[sftxpnmo]
Cat:    RSF/system/seismic
Desc:   Normal moveout in TXP domain
DocCmd: sftxpnmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  extend int  -  4 		trace extension 
Param:  mute int  -  12 		mute zone 
Param:  str float  -  0.5 		maximum stretch allowed 

