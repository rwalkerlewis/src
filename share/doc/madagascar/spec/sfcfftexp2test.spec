[sfcfftexp2test]
Cat:    RSF/user/jsun
Desc:   2-D FFT-based zero-offset exploding reflector modeling/migration (outputs time volume, not just last image; can be used to generate movie)
DocCmd: sfcfftexp2test | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		depth sampling (if migration) 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		depth samples (if migration) 
Param:  pad1 int  -  1 		padding factor on the first axis 

