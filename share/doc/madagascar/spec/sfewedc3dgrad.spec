[sfewedc3dgrad]
Cat:    RSF/user/jsun
Desc:   3D elastic recursive integral time extrapolation of decomposed wave modes using KISS-FFT
DocCmd: sfewedc3dgrad | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ltp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   lts rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rkp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rks rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rtp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rts rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfp rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wfs rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  back enum-bool  -  n 		backward extrapolation flag (for rtm) 
Param:  esou enum-bool  -  n 		explosive force source 
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  nb int  -   -  		
LDesc:  (defaults to: NOP)
Param:  nbell int  -   -  		bell size 
LDesc:  (defaults to: NOP)
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqy int  -   -  		
LDesc:  (defaults to: sf_n(ay))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqy float  -   -  		
LDesc:  (defaults to: sf_o(ay))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  verb enum-bool  -  n 		verbosity flag 

