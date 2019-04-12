[sfmpifd2d]
Cat:    RSF/user/zhiguang
Desc:   Acoustic wave equation forward modeling with MPI and OpenMP
DocCmd: sfmpifd2d | cat
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  coef float  -  0.003 		absorbing boundary coefficient 
Param:  dr float  -   -  		receiver interval 
Param:  ds float  -   -  		shot interval 
Param:  nb int  -  80 		boundary width 
Param:  nr int  -   -  		number of receiver 
Param:  ns int  -   -  		shot number 
Param:  r0 float  -   -  		receiver origin 
Param:  rectx int  -  2 		source smooothing parameter 
Param:  rectz int  -  2 		source smooothing parameter 
Param:  rz int  -   -  		receiver depth 
LDesc:  (defaults to: sz)
Param:  s0 float  -   -  		shot origin 
Param:  sz int  -  5 		source depth 
Param:  verb enum-bool  -  n 		verbosity flag 

