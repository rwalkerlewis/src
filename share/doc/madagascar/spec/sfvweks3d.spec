[sfvweks3d]
Cat:    RSF/user/jsun
Desc:   3D visco-elastic time-domain pseudo-spectral (k-space) modeling using shared-memory parallel FFT
DocCmd: sfvweks3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwav data)
Port:   stdout rsf w req 	RSF standard output (containing Fdat data)
Port:   ccc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   qqq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  back enum-bool  -  n 		backward extrapolation flag (for rtm) 
Param:  dabc enum-bool  -  n 		absorbing BC 
Param:  fcut float  -  500 		cutoff frequency for Q-compensation 
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
Param:  pcut float  -  0.2 		pcut/2 is tapered portion w.r.t. 1 
Param:  qmod int  -  0 		q modeling switch 
Param:  rfreq float  -  1000 		reference frequency for constant-Q 
Param:  snap enum-bool  -  n 		wavefield snapshots flag 
Param:  ssou int  -  0 		0 -> acceleration source; 1 -> stress source; 2 -> displacement source 
Param:  verb enum-bool  -  n 		verbosity flag 

