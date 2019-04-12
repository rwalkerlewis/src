[sfpame2d]
Cat:    RSF/user/junyan
Desc:   2-D elasitc wave modeling and vector field decompostion using pseudo-analytical method
DocCmd: sfpame2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsource data)
Port:   stdout rsf w req 	RSF standard output (containing fwavup data)
Port:   vp rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavu rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavus rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavw rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavwp rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   wavws rsf w  -  		auxiliary output file name (containing unspecified data)
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
Param:  snap int  -  1 		

