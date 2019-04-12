[sfitxmo3]
Cat:    RSF/system/seismic
Desc:   Forward and inverse normal moveout with interval velocity
DocCmd: sfitxmo3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   c11 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c12 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c13 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c22 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c23 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c33 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c44 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c55 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c66 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   time rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   x rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   y rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cij enum-bool  -  n 		
Param:  dpx float  -   -  		x slope sampling 
Param:  dpy float  -   -  		y slope sampling 
Param:  dx float  -   -  		x offset sampling 
Param:  dy float  -   -  		y offset sampling 
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		
Param:  npx int  -   -  		x slope samples 
Param:  npy int  -   -  		y slope samples 
Param:  nx int  -   -  		x offset samples 
Param:  ny int  -   -  		y offset samples 
Param:  px0 float  -  0. 		x first slope 
Param:  py0 float  -  0. 		y first slope 
Param:  x0 float  -  0. 		x first offset 
Param:  y0 float  -  0. 		y first offset 

