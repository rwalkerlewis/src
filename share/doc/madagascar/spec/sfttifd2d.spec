[sfttifd2d]
Cat:    RSF/user/psava
Desc:   2D TTI time-domain FD modeling
DocCmd: sfttifd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ang rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  atype string  -   -  		
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  expl enum-bool  -  n 		'exploding reflector' 
Param:  free enum-bool  -  n 		free surface 
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
Param:  snap enum-bool  -  n 		wavefield snapshots 
Param:  sout enum-bool  -  n 		stress output 
Param:  uses enum-bool  -  n 		use vsz 
Param:  verb enum-bool  -  n 		verbosity 

