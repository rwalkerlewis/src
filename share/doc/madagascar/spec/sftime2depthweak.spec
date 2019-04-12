[sftime2depthweak]
Cat:    RSF/user/zone
Desc:   Time-to-depth conversion in media with weak lateral variations 2D (Sripanich and Fomel, 2017)
DocCmd: sftime2depthweak | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dvdt0 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dvdx0 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   outdt0 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   outdv rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   outdx0 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   refvelocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nderiv int  -  10 		Derivative filter order 
Param:  nsmooth int  -  10 		Smoothing repeat 
Param:  refderiv float  -  1. 		Deriveative filter reference (0.5 < ref <= 1) 
Param:  smoothlen int  -   -  		Smoothing filter length 
LDesc:  (defaults to: nx/20)
Param:  zsubsample int  -  100 		Additional subsampling in depth for stability 

