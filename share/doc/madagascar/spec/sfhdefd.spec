[sfhdefd]
Cat:    RSF/user/psava
Desc:   Heat diffusion equation FD modeling
DocCmd: sfhdefd | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   con rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  free enum-bool  -  n 		free surface flag
Param:  jdata int  -  1 		# of t steps at which to save receiver data 
Param:  jsnap int  -   -  		# of t steps at which to save wavefield 
LDesc:  (defaults to: nt)
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  verb enum-bool  -  n 		verbosity flag 

