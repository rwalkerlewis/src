[sfmpirtmop]
Cat:    RSF/user/jsun
Desc:   2-D Low-rank One-step Least Pre-stack Reverse-Time-Migration in the complex domain (both img and data are complex valued)
DocCmd: sfmpirtmop | cat
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   src rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   tmpwf rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		migration
Param:  born enum-bool  -  n 		use exact born approximation
Param:  bot int  -  40 		
Param:  gpl int  -   -  		
Param:  gpz int  -   -  		
Param:  illum enum-bool  -  n 		if n, no source illumination applied 
Param:  justrec enum-bool  -  n 		just model for the seismic record
Param:  lft int  -  40 		
Param:  mute enum-bool  -  y 		muting direct arrival
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  rectx int  -  1 		
Param:  rectz int  -  1 		
Param:  repeat int  -  0 		abc parameters 
Param:  rht int  -  40 		muting for migration after modeling 
Param:  roll enum-bool  -  n 		if n, receiver is independent of source location and gpl=nx
Param:  sht0 int  -   -  		actual shot origin on grid
LDesc:  (defaults to: shtbgn)
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtint int  -   -  		
Param:  snapinter int  -  1 		snap interval 
Param:  spz int  -   -  		
Param:  srctrunc float  -  0.4 		
Param:  top int  -  40 		
Param:  verb enum-bool  -  n 		verbosity
Param:  vref float  -  1500 		
Param:  wantwf enum-bool  -  n 		output forward and backward wavefield
Param:  wd int  -  5 		

