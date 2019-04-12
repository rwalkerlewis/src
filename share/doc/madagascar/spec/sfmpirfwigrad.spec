[sfmpirfwigrad]
Cat:    RSF/user/zhiguang
Desc:   Calculate acoustic Reflection FWI gradient with the prepared adjoint source (velocity-impedance scale separation)
DocCmd: sfmpirfwigrad | cat
Port:   Fadj rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fd rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fd0 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  acqui_type int  -  1 		acquisition type 
Param:  coef float  -  5. 		maximum velocity of the medium 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: dx)
Param:  ds float  -   -  		shot interval 
Param:  frectx int  -  2 		source smoothing in x 
Param:  frectz int  -  2 		source smoothing in z 
Param:  interval int  -  1 		wavefield storing interval 
Param:  nb int  -  20 		PML boundary width 
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: nx)
Param:  ns int  -   -  		shot number 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: x0)
Param:  rz int  -  3 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  sz int  -  3 		source depth 
Param:  verb enum-bool  -  n 		verbosity flag 

