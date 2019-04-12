[sfhwt3d]
Cat:    RSF/user/psava
Desc:   
DocCmd: sfhwt3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fv data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Param:  dg float  -  1 		
Param:  dh float  -  1 		
Param:  dt float  -  0.001 		
Param:  forceray enum-bool  -  n 		
Param:  ng int  -  360 		
Param:  nh int  -  360 		
Param:  nt int  -  100 		
Param:  og float  -  -180 		
Param:  oh float  -  -180 		
Param:  ot float  -  0 		
Param:  scaleray int  -  1. 		velocity file 
Param:  verb enum-bool  -  n 		
Param:  xsou float  -   -  		
LDesc:  (defaults to: sf_o(ax) + sf_n(ax)*sf_d(ax)/2)
Param:  ysou float  -   -  		
LDesc:  (defaults to: sf_o(ay) + sf_n(ay)*sf_d(ay)/2)
Param:  zsou float  -   -  		
LDesc:  (defaults to: sf_o(az) + sf_n(az)*sf_d(az)/2)

