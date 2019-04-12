[sfeicop3d]
Cat:    RSF/user/psava
Desc:   Extended IC 2D
DocCmd: sfeicop3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fimg data)
Port:   stdout rsf w req 	RSF standard output (containing Fwfl data)
Port:   cip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   opr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  gaus enum-bool  -  n 		Gaussian taper 
Param:  gst float  -   -  		
LDesc:  (defaults to: 0.25*sf_n(aht)*sf_d(aht))
Param:  gsx float  -   -  		
LDesc:  (defaults to: 0.25*sf_n(ahx)*sf_d(ahx))
Param:  gsy float  -   -  		
LDesc:  (defaults to: 0.25*sf_n(ahy)*sf_d(ahy))
Param:  gsz float  -   -  		
LDesc:  (defaults to: 0.25*sf_n(ahz)*sf_d(ahz))
Param:  nht int  -  0 		t lags 
Param:  nhx int  -  0 		x lags 
Param:  nhy int  -  0 		y lags 
Param:  nhz int  -  0 		z lags 
Param:  oprcausal enum-bool  -  n 		causal opr? 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wflcausal enum-bool  -  n 		causal wfl? 

