[sfemfdm2d_p]
Cat:    RSF/user/ditthara
Desc:   2D EM FD modeling
DocCmd: sfemfdm2d_p | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   cdt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ele rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mag rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  expl enum-bool  -  n 		'exploding reflector' 
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
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  verb enum-bool  -  n 		verbosity flag 

