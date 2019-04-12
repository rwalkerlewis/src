[sfwem2d_iso]
Cat:    RSF/user/jeff
Desc:   2D ISOTROPIC wave-equation finite-difference migration
DocCmd: sfwem2d_iso | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fxig data)
Port:   stdout rsf w req 	RSF standard output (containing Fxigo data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rwfout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swfout rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  add enum-bool  -  n 		
Param:  adj enum-bool  -  y 		ADJOINT flag 
Param:  nh int  -  0 		
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 
Param:  wantwf enum-bool  -  n 		Want output wavefields 

