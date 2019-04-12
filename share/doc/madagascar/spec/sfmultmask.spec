[sfmultmask]
Cat:    RSF/user/lcasasan
Desc:   Create a data mask using multiple muting curve from MRKE
DocCmd: sfmultmask | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nw int  -  0 		smoothing window length must be odd
Param:  shift enum-bool  -  n 		shift 
Param:  smooth enum-bool  -  n 		smoothed mask [raised cosine] 
Param:  start enum-bool  -  n 		mask from starting sample to index value in mask 
Param:  verb enum-bool  -  n 		

