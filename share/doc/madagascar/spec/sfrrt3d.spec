[sfrrt3d]
Cat:    RSF/user/psava
Desc:   
DocCmd: sfrrt3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Ft data)
Param:  dt float  -  0.001 		
Param:  fill int  -  1 		
Param:  gmax float  -  +90 		
Param:  gmin float  -  -90 		
Param:  hmax float  -  180 		
Param:  hmin float  -  0 		
Param:  jray int  -  1 		
Param:  nray int  -  1 		
Param:  nt int  -  100 		
Param:  ot float  -  0 		
Param:  pick int  -  2 		
Param:  scaleray int  -  1. 		
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))
Param:  verb enum-bool  -  n 		
Param:  xsou float  -   -  		
LDesc:  (defaults to: sf_o(ax) + sf_n(ax)*sf_d(ax)/2)
Param:  ysou float  -   -  		
LDesc:  (defaults to: sf_o(ay) + sf_n(ay)*sf_d(ay)/2)
Param:  zsou float  -   -  		
LDesc:  (defaults to: sf_o(az) + sf_n(az)*sf_d(az)/2)

