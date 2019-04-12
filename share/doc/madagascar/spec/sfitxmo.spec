[sfitxmo]
Cat:    RSF/system/seismic
Desc:   Forward and inverse normal moveout with interval velocity
DocCmd: sfitxmo | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dp float  -   -  		slope sampling 
Param:  dx float  -   -  		offset sampling 
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		
Param:  np int  -   -  		slope samples 
Param:  nx int  -   -  		offset samples 
Param:  p0 float  -  0. 		first slope 
Param:  x0 float  -  0. 		first offset 

