[sfzolsrtm2]
Cat:    RSF/user/jsun
Desc:   2-D FFT-based zero-offset exploding reflector modeling/migration linear operator
DocCmd: sfzolsrtm2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if n, modeling; if y, migration 
Param:  dt float  -   -  		time sampling 
Param:  dz float  -   -  		depth sampling 
Param:  gpz int  -  0 		geophone surface 
Param:  nt int  -   -  		time samples 
Param:  nz int  -   -  		depth samples 
Param:  oz float  -  0. 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  taper int  -  0 		tapering in the frequency domain 
Param:  thresh float  -  0.92 		tapering threshold 
Param:  timer enum-bool  -  n 		
Param:  verb enum-bool  -  n 		

