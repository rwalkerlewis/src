[sfffd2dehf]
Cat:    RSF/user/songxl
Desc:   2-D Fourier finite-difference wave extrapolation, smooth point source, depress high frequency
DocCmd: sfffd2dehf | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ax float  -  5.0 		suppress HF parameter
Param:  az float  -  5.0 		suppress HF parameter
Param:  cb float  -  0.01 		decaying parameter
Param:  cl float  -  0.01 		decaying parameter
Param:  cr float  -  0.01 		decaying parameter
Param:  ct float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  factor float  -  5.0/6.0 		suppress HF parameter
Param:  isx int  -   -  		
Param:  isz int  -   -  		
Param:  nbb int  -  44 		
Param:  nbl int  -  44 		
Param:  nbr int  -  44 		
Param:  nbt int  -  44 		
Param:  nt int  -   -  		
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 

