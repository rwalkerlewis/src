[sfadjgradient2d_gpu]
Cat:    RSF/user/rweiss
Desc:   2D ISOTROPIC wave-equation finite-difference migration on GPU
DocCmd: sfadjgradient2d_gpu | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel data)
Port:   stdout rsf w req 	RSF standard output (containing Fgrd data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  gpu int  -  0 		ID of the GPU to be used 
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 

