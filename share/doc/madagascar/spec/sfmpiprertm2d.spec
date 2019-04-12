[sfmpiprertm2d]
Cat:    RSF/user/zhiguang
Desc:   2-D prestack reverse-time migration and its adjoint with MPI
DocCmd: sfmpiprertm2d | cat
Port:   input rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   snapshot rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		
Param:  dr float  -   -  		
Param:  ds float  -   -  		
Param:  jt int  -  100 		
Param:  nr int  -   -  		
Param:  ns int  -   -  		
Param:  nx int  -   -  		
Param:  padx int  -   -  		
Param:  padz int  -   -  		
Param:  r0 float  -   -  		
Param:  s0 float  -   -  		
Param:  snap enum-bool  -  n 		
Param:  verb enum-bool  -  n 		
Param:  zr float  -  0.0 		
Param:  zs float  -  0.0 		

