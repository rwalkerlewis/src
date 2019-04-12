[sfadjgradient2d_coupled_gpu]
Cat:    RSF/user/rweiss
Desc:   2D ISOTROPIC wave-equation finite-difference migration on GPU
DocCmd: sfadjgradient2d_coupled_gpu | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvel1 data)
Port:   stdout rsf w req 	RSF standard output (containing Fgrd1 data)
Port:   grd2 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ur1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ur2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   us1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   us2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   xig2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps4D float  -   -  		Weighting for 4D penalty 
LDesc:  (defaults to: 0.f)
Param:  epsDSO float  -   -  		Weighting for DSO penalty 
LDesc:  (defaults to: 1.f)
Param:  gpu int  -  0 		ID of the GPU to be used 
Param:  hzero int  -  5 		Number of near offsets to zero 
Param:  nxtap int  -  40 		TAPER size 
Param:  verbose enum-bool  -  n 		VERBOSITY flag 

