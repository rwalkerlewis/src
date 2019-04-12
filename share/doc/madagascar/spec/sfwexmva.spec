[sfwexmva]
Cat:    RSF/user/cwp
Desc:   3-D S/R WEMVA with extended split-step
DocCmd: sfwexmva | cat
Port:   stdin  rsf r req 	RSF standard input (containing Pi data)
Port:   cc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rwfl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   swfl rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj int  -   -  		y=ADJ Back-projection; n=FWD Forward Scattering 
Param:  dht float  -   -  		
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  feic int  -   -  		extended I.C. flag 
Param:  nht int  -  0 		number of lags on the t axis 
Param:  nhx int  -  0 		number of lags on the x axis 
Param:  nhy int  -  0 		number of lags on the y axis 
Param:  nhz int  -  0 		number of lags on the z axis 
Param:  nrmax int  -  1 		max number of refs 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  tmx int  -  0 		taper on x   
Param:  tmy int  -  0 		taper on y   
Param:  verb enum-bool  -  y 		verbosity flag 

