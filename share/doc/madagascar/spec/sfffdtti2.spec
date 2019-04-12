[sfffdtti2]
Cat:    RSF/user/songxl
Desc:   2-D Fourier finite-difference wave extrapolation
DocCmd: sfffdtti2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   seta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   yita rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  alpha float  -  -0.7 		
Param:  cb float  -  0.002 		decaying parameter
Param:  cl float  -  0.002 		decaying parameter
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  cr float  -  0.002 		decaying parameter
Param:  ct float  -  0.002 		decaying parameter
Param:  dt float  -   -  		
Param:  err float  -  0.0001 		
Param:  isx int  -   -  		
Param:  isz int  -  0 		
Param:  nbb int  -  126 		
Param:  nbl int  -  128 		
Param:  nbr int  -  128 		
Param:  nbt int  -  126 		
Param:  nt int  -   -  		
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 
Param:  pad1 int  -  1 		padding factor on the first axis 

