[sfawefd2d_fo]
Cat:    RSF/user/fbroggin
Desc:   Finite-difference time-domain (FDTD) wave propagation modeling in lossless acoustic 2D media
DocCmd: sfawefd2d_fo | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   datvz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  expl enum-bool  -  n 		exploding reflector 
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  recvz enum-bool  -  n 		vertical particle velocity data 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  srctype int  -  1 		------------------------------------------------------------
Param:  verb enum-bool  -  n 		verbosity flag 

