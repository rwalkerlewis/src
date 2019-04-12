[sfwexmig]
Cat:    RSF/user/cwp
Desc:   3-D modeling/migration with extended SSF
DocCmd: sfwexmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fm data)
Port:   cc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   cip rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swfl rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dht float  -   -  		
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  fdrv enum-bool  -  n 		image derivative flag 
Param:  feic enum-bool  -  n 		extended I.C. flag 
Param:  fnew enum-bool  -  n 		phase-shift flag 
Param:  nht int  -  0 		number of lags on the t axis 
Param:  nhx int  -  0 		number of lags on the x axis 
Param:  nhy int  -  0 		number of lags on the y axis 
Param:  nhz int  -  0 		number of lags on the z axis 
Param:  nrmax int  -  1 		maximum references 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  tmx int  -  0 		taper on x 
Param:  tmy int  -  0 		taper on y 
Param:  verb enum-bool  -  n 		verbosity flag 

