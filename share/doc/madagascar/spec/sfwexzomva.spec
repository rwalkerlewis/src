[sfwexzomva]
Cat:    RSF/user/cwp
Desc:   3-D S/R WEMVA with extended split-step
DocCmd: sfwexzomva | cat
Port:   stdin  rsf r req 	RSF standard input (containing Pi data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj int  -   -  		y=ADJ Back-projection; n=FWD Forward Scattering 
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  nrmax int  -  1 		max number of refs 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y 
Param:  tmx int  -  0 		taper on x   
Param:  tmy int  -  0 		taper on y   
Param:  verb enum-bool  -  y 		verbosity flag 

