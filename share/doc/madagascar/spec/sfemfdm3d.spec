[sfemfdm3d]
Cat:    RSF/user/ditthara
Desc:   3D Electromagnetic time-domain FD modeling
DocCmd: sfemfdm3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   cdt rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ele rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mag rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dabc enum-bool  -  n 		Absorbing BC 
Param:  dqx float  -   -  		Saved wfld window dx 
LDesc:  (defaults to: sf_d(ax))
Param:  dqy float  -   -  		Saved wfld window dy 
LDesc:  (defaults to: sf_d(ay))
Param:  dqz float  -   -  		Saved wfld window dz 
LDesc:  (defaults to: sf_d(az))
Param:  expl enum-bool  -  n 		Multiple sources, one wvlt 
Param:  free enum-bool  -  n 		Free surface flag 
Param:  jdata int  -  1 		# of t steps at which to save receiver data 
Param:  jsnap int  -   -  		# of t steps at which to save wavefield 
LDesc:  (defaults to: nt)
Param:  nb int  -  2 		boundary padding in grid points 
Param:  nqx int  -   -  		Saved wfld window nx 
LDesc:  (defaults to: sf_n(ax))
Param:  nqy int  -   -  		Saved wfld window ny 
LDesc:  (defaults to: sf_n(ay))
Param:  nqz int  -   -  		Saved wfld window nz 
LDesc:  (defaults to: sf_n(az))
Param:  oqx float  -   -  		Saved wfld window ox 
LDesc:  (defaults to: sf_o(ax))
Param:  oqy float  -   -  		Saved wfld window oy 
LDesc:  (defaults to: sf_o(ay))
Param:  oqz float  -   -  		Saved wfld window oz 
LDesc:  (defaults to: sf_o(az))
Param:  snap enum-bool  -  n 		Wavefield snapshots flag 
Param:  verb enum-bool  -  n 		Verbosity flag 

