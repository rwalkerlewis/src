[sflfftexp0]
Cat:    RSF/user/fomels
Desc:   2-D FFT-based zero-offset exploding reflector modeling/migration as linear operator
DocCmd: sflfftexp0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if n, modeling; if y, migration 
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		time sampling (if migration) 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		time samples (if migration) 
Param:  pad1 int  -  1 		padding factor on the first axis 

