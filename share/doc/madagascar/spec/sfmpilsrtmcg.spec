[sfmpilsrtmcg]
Cat:    RSF/user/jsun
Desc:   2-D Low-rank One-step Least-square Pre-stack Reverse-Time-Migration using CG in the complex domain (both img and data are complex valued)
DocCmd: sfmpilsrtmcg | cat
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   src rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  bot int  -  40 		
Param:  gpl int  -   -  		
Param:  gpz int  -   -  		
Param:  illum enum-bool  -  n 		if n, no source illumination applied 
Param:  lft int  -  40 		
Param:  mode int  -  0 		
Param:  niter int  -  1 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  rectx int  -  1 		
Param:  rectz int  -  1 		
Param:  repeat int  -  0 		abc parameters 
Param:  rht int  -  40 		Set I/O file
Param:  roll enum-bool  -  n 		if n, receiver is independent of source location and gpl=nx
Param:  sht0 int  -   -  		actual shot origin on grid
LDesc:  (defaults to: shtbgn)
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtint int  -   -  		
Param:  snapinter int  -  1 		snap interval 
Param:  spz int  -   -  		
Param:  srctrunc float  -  0.4 		
Param:  start string  -   -  		auxiliary input file name
Param:  top int  -  40 		
Param:  verb enum-bool  -  n 		verbosity

