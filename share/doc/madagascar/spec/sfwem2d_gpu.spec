[sfwem2d_gpu]
Cat:    RSF/user/rweiss
Desc:   2D ISOTROPIC wave-equation finite-difference migration on GPU
DocCmd: sfwem2d_gpu | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fxig data)
Port:   stdout rsf w req 	RSF standard output (containing Fxigo data)
Port:   rillum rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rwfout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sillum rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swfout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  gpu int  -  0 		ID of the GPU to be used 
Param:  nh int  -  0 		
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 
Param:  wantillum enum-bool  -  n 		Want output wavefields 
Param:  wantwf enum-bool  -  n 		Want output wavefields 

