[sfadjgradient2d_coupled]
Cat:    RSF/user/jeff
Desc:   Gradient adjoint-state calculation for image-domain WET
DocCmd: sfadjgradient2d_coupled | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel1 data)
Port:   stdout rsf w req 	RSF standard output (containing Fgr1 data)
Port:   gr2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ur1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ur2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   us1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   us2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 

