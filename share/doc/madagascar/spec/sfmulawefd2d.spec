[sfmulawefd2d]
Cat:    RSF/user/chenyk
Desc:   2D multisource acoustic time-domain FD modeling for testing
DocCmd: sfmulawefd2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou1 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cden enum-bool  -  n 		Constant density 
Param:  dabc enum-bool  -  n 		Absorbing BC 
Param:  free enum-bool  -  n 		Free surface flag 
Param:  jdata int  -  1 		# of t steps at which to save receiver data 
Param:  jsnap int  -   -  		# of t steps at which to save wavefield 
LDesc:  (defaults to: nt)
Param:  nqx int  -   -  		Saved wfld window nx 
LDesc:  (defaults to: sf_n(ax))
Param:  nqz int  -   -  		Saved wfld window nz 
LDesc:  (defaults to: sf_n(az))
Param:  oqx float  -   -  		Saved wfld window ox 
LDesc:  (defaults to: sf_o(ax))
Param:  oqz float  -   -  		Saved wfld window oz 
LDesc:  (defaults to: sf_o(az))
Param:  snap enum-bool  -  n 		Wavefield snapshots flag 
Param:  verb enum-bool  -  n 		Verbosity flag 

