[sffftexp0test]
Cat:    RSF/user/jsun
Desc:   2-D FFT-based zero-offset exploding reflector modeling/migration (outputs time volume; can be used to generate movies)
DocCmd: sffftexp0test | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   movie rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		time sampling (if migration) 
Param:  jt int  -  1 		time interval 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		time samples (if migration) 
Param:  pad1 int  -  1 		padding factor on the first axis 

