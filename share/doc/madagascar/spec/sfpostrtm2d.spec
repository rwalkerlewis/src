[sfpostrtm2d]
Cat:    RSF/user/zhiguang
Desc:   2-D exploding-reflector RTM and its adjoint
DocCmd: sfpostrtm2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adjoint flag, 0: modeling, 1: migration 
Param:  dt float  -   -  		
Param:  jt int  -  50 		time interval of wavefield snapshot 
Param:  n0 int  -  0 		surface 
Param:  nt int  -   -  		
Param:  padx int  -   -  		
LDesc:  (defaults to: nz/2)
Param:  padz int  -   -  		
LDesc:  (defaults to: nz/2)
Param:  snap enum-bool  -  n 		wavefield snapshot flag 

