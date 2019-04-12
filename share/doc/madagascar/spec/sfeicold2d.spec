[sfeicold2d]
Cat:    RSF/user/psava
Desc:   Extended IC 3D
DocCmd: sfeicold2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   cc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  gaus enum-bool  -  n 		Gaussian taper flag 
Param:  gst float  -   -  		
LDesc:  (defaults to: nht*sf_d(at))
Param:  gsx float  -   -  		
LDesc:  (defaults to: nhx*sf_d(ax))
Param:  gsz float  -   -  		
LDesc:  (defaults to: nhz*sf_d(az))
Param:  isreversed enum-bool  -  n 		reversed rec wfld? 
Param:  nht int  -  0 		
Param:  nhx int  -  0 		
Param:  nhz int  -  0 		
Param:  verb enum-bool  -  n 		verbosity flag 

