[sfmpifwigrad]
Cat:    RSF/user/zhiguang
Desc:   Calculate acoustic FWI gradient with the prepared adjoint source
DocCmd: sfmpifwigrad | cat
Port:   Fadj rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwfl1 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fwfl2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  coef float  -  0.002 		absorbing boundary coefficient 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: dx)
Param:  ds float  -   -  		shot interval 
Param:  frectx int  -  2 		source smoothing in x 
Param:  frectz int  -  2 		source smoothing in z 
Param:  nb int  -  100 		boundary width 
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: nx)
Param:  ns int  -   -  		shot number 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: x0)
Param:  rz int  -  5 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  sz int  -  5 		source depth 

