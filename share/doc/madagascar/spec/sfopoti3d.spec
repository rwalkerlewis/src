[sfopoti3d]
Cat:    RSF/user/junyan
Desc:   Modeling of pure acoustic wave in 3-D transversely isotropic meida using optimized pseudo-Laplacian operator
DocCmd: sfopoti3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   Gxxl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxxl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxxr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxxzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxyyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxyyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxyzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxyzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxxzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyyyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyyyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyyzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyyzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxyzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxzzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gxzzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyyyl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyyyr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyyzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyyzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyyzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyzzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gyzzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gzzzzl rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gzzzzr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   delta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   phi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   seta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sigma rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  cxl float  -  0.01 		decaying parameter
Param:  cxr float  -  0.01 		decaying parameter
Param:  czb float  -  0.01 		decaying parameter
Param:  czt float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  isx int  -   -  		
Param:  isy int  -   -  		
Param:  isz int  -   -  		
Param:  nbb int  -  30 		
Param:  nbt int  -  30 		
Param:  nt int  -   -  		
Param:  nxl int  -  30 		
Param:  nxr int  -  30 		
Param:  nyl int  -  30 		
Param:  nyr int  -  30 		assume ABC pars are the same 
Param:  opt int  -  1 		if y, determine optimal size for efficiency 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  1 		

