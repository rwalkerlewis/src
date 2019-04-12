[sfadjgradient2d]
Cat:    RSF/user/jeff
Desc:   Gradient adjoint-state calculation for image-domain WET
DocCmd: sfadjgradient2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel data)
Port:   stdout rsf w req 	RSF standard output (containing Fgrd data)
Port:   rwf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 

