[vpvr3d]
Cat:    RSF/user/dellinger
Desc:   Plot impulse responses in 3 dimensions
DocCmd: vpvr3d | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  bottom float  -  -90. 		latitude start 
Param:  coslimit float  -  25. 		aximum deviation in particle motion angle 
Param:  end float  -  360. 		longitude end 
Param:  inc int  -  4 		density of gridding (How many tiles to cover 90 degree of longitude in initial tiling.) 
Param:  inc2 int  -   -  		tiles bigger than 90 deg / iinc2 in any dimension will be subdivided to fit 
LDesc:  (defaults to: iinc)
Param:  maxlevel int  -  5 		maximum number of re-subdivisions 
Param:  norm float  -  1. 		amount to divide everything by 
Param:  or enum-bool  -  n 		modifier: if or=y ORs instead of ANDS the clips. 
Param:  order enum-bool  -  n 		try to swap around the surfaces to make them continuous 
Param:  sing string  -   -  		Log file 
Param:  skip int  -  -1 		modifier: skip=-1 don't clip this surface (-1 for none skipped)
LDesc:       			0 = fastest
LDesc:       			1 = intermediate
LDesc:       			2 = slowest
LDesc:       			3 = red (SH)
LDesc:       			4 = green (SV)
LDesc:       			5 = blue (P) 
Param:  start float  -  0. 		longitude start 
Param:  top float  -  90. 		latitude end 
Param:  what int-list  -   -  		 [3]
Param:  which enum-bool  -  y 		if y, plot impulse response; if n, plot slowness surface 
Param:  xmax float  -  100. 		
Param:  xmin float  -  -100. 		
Param:  xxmax float  -  100. 		
Param:  xxmin float  -  -100. 		
Param:  ymax float  -  100. 		
Param:  ymin float  -  -100. 		
Param:  yymax float  -  100. 		
Param:  yymin float  -  -100. 		
Param:  zmax float  -  100. 		
Param:  zmin float  -  -100. 		
Param:  zzmax float  -  100. 		
Param:  zzmin float  -  -100. 		

