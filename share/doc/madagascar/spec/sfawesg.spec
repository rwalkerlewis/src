[sfawesg]
Cat:    RSF/user/cwp
Desc:   Acoustic staggered-gridded time-domain FD modeling,
DocCmd: sfawesg | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   bulk rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  abc enum-bool  -  n 		ABC if the abcpml=n: spongeABC 
Param:  debug enum-bool  -  n 		debug 
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		save wavefield every *jsnap* time steps 
LDesc:  (defaults to: nt)
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqy int  -   -  		
LDesc:  (defaults to: sf_n(ay))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqy float  -   -  		
LDesc:  (defaults to: sf_o(ay))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  pml enum-bool  -  n 		'PML ABC' 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  verb enum-bool  -  n 		verbosity flag 

