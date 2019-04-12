[sfeweks3dsecd]
Cat:    RSF/user/jsun
Desc:   3D elastic time-domain pseudo-spectral (k-space) modeling using shared-memory parallel FFT (second-order equation)
DocCmd: sfeweks3dsecd | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  back enum-bool  -  n 		backward extrapolation flag (for rtm) 
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  free enum-bool  -  n 		free surface flag 
Param:  jdata int  -  1 		
Param:  jsnap int  -   -  		
LDesc:  (defaults to: nt)
Param:  kspace enum-bool  -  n 		k-space method (ps) flag 
Param:  nbell int  -  5 		bell size 
Param:  nqx int  -   -  		
LDesc:  (defaults to: sf_n(ax))
Param:  nqy int  -   -  		
LDesc:  (defaults to: sf_n(ay))
Param:  nqz int  -   -  		
LDesc:  (defaults to: sf_n(az))
Param:  opot enum-bool  -  n 		output potentials -> 1*scalar, 3*vector potentials 
Param:  oqx float  -   -  		
LDesc:  (defaults to: sf_o(ax))
Param:  oqy float  -   -  		
LDesc:  (defaults to: sf_o(ay))
Param:  oqz float  -   -  		
LDesc:  (defaults to: sf_o(az))
Param:  secd enum-bool  -  n 		second order weq flag 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou int  -  0 		0 -> acceleration source; 1 -> stress source; 2 -> displacement source 
Param:  verb enum-bool  -  n 		verbosity flag 

