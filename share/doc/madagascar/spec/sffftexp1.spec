[sffftexp1]
Cat:    RSF/user/fomels
Desc:   2-D FFT-based prestack exploding reflector modeling/migration
DocCmd: sffftexp1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  dh float  -   -  		offset sampling (if modeling) 
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		time sampling (if migration) 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nh int  -   -  		offset samples (if modeling) 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		time samples (if migration) 
Param:  snap int  -  0 		interval for snapshots 
Param:  sub enum-bool  -  y 		if -1 is included in the matrix 

