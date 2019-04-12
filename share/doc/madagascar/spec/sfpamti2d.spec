[sfpamti2d]
Cat:    RSF/user/junyan
Desc:   Modeling of pure acoustic wave in 3-D transversely isotropic media with psuedo-analytic method
DocCmd: sfpamti2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   delta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   seta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sigma rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
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
Param:  opt int  -  1 		if y, determine optimal size for efficiency 
Param:  snap int  -  1 		

