[sfopame2d]
Cat:    RSF/user/junyan
Desc:   2-D opam for elastic wave modeling and vector field decompostion
DocCmd: sfopame2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsource data)
Port:   stdout rsf w req 	RSF standard output (containing fwavup data)
Port:   Guxxl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guxxr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guxzpl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guxzpr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guxzsl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guxzsr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Guzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxxl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxxr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxzpl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxzpr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxzsl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwxzsr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gwzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavu rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavus rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavw rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavwp rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavws rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  cxl float  -  0.01 		decaying parameter
Param:  cxr float  -  0.01 		decaying parameter
Param:  czb float  -  0.01 		decaying parameter
Param:  czt float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  isx int  -   -  		
Param:  isz int  -   -  		
Param:  nbb int  -  44 		
Param:  nbt int  -  44 		
Param:  nt int  -   -  		
Param:  nxl int  -  44 		
Param:  nxr int  -  44 		assume ABC pars are the same 
Param:  opt int  -  0 		if y, determine optimal size for efficiency 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  1 		

