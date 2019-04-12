[sfmpilrrtm]
Cat:    RSF/user/zhiguang
Desc:   2-D Low-rank One-step Reverse-Time-Migration (simultaneous sources data and incomplete data)
DocCmd: sfmpilrrtm | cat
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   src rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tmpwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		migration
Param:  bot int  -  40 		
Param:  choose int  -   -  		Set I/O file
LDesc:  (defaults to: nsource)
Param:  dsource int  -  0 		
Param:  fm enum-bool  -  n 		if n, Born modelling  
Param:  gpl int  -   -  		
Param:  gpz int  -   -  		
Param:  illum enum-bool  -  n 		if n, no source illumination applied 
Param:  incom enum-bool  -  n 		if n, use complete data 
Param:  lft int  -  40 		
Param:  nsource int  -  1 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  rectx int  -  2 		
Param:  rectz int  -  2 		
Param:  repeat int  -  2 		abc parameters 
Param:  rht int  -  40 		simultaneous sources parameter 
Param:  roll enum-bool  -  y 		if n, receiver is independent of source location and gpl=nx
Param:  sht0 int  -   -  		actual shot origin on grid
LDesc:  (defaults to: shtbgn)
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtint int  -   -  		
Param:  snapinter int  -  1 		snap interval 
Param:  spz int  -   -  		
Param:  srctrunc float  -  0.4 		
Param:  tdelay float  -  0 		
Param:  top int  -  40 		
Param:  verb enum-bool  -  n 		verbosity
Param:  wantrecord enum-bool  -  y 		if n, using record data generated by this program 
Param:  wantwf enum-bool  -  n 		output forward and backward wavefield
Param:  wfint int  -  50 		snap interval 

