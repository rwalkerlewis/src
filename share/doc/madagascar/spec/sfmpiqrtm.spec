[sfmpiqrtm]
Cat:    RSF/user/jsun
Desc:   2-D Low-rank One-step Least Pre-stack Reverse-Time-Migration in the complex domain (both img and data are complex valued)
DocCmd: sfmpiqrtm | cat
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   src rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		migration
Param:  bot int  -  40 		
Param:  eps float  -   -  		padding
LDesc:  (defaults to: SF_EPS)
Param:  freq_scal enum-bool  -  n 		frequency amplitude spectrum scaling
Param:  gpl int  -   -  		
Param:  gpz int  -   -  		
Param:  illum enum-bool  -  n 		if n, no source illumination applied 
Param:  lft int  -  40 		
Param:  mode int  -   -  		
Param:  niter int  -  100 		smooth division maximum iterations
Param:  norm string  -   -  		auxiliary output file name
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  perc float  -  0.1 		percentage of maximum for padding
Param:  rectx int  -  1 		
Param:  rectz int  -  1 		
Param:  reg float  -   -  		regularization
LDesc:  (defaults to: 0.0f)
Param:  repeat int  -  0 		abc parameters 
Param:  rht int  -  40 		shot output id 
Param:  roll enum-bool  -  n 		if n, receiver is independent of source location and gpl=nx
Param:  sdiv enum-bool  -  n 		smooth division
Param:  sht0 int  -   -  		actual shot origin on grid
LDesc:  (defaults to: shtbgn)
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtid int  -  0 		Set I/O file
Param:  shtint int  -   -  		
Param:  snapinter int  -  1 		snap interval 
Param:  spz int  -   -  		
Param:  srctrunc float  -  0.4 		
Param:  stable int  -  0 		stable = 0 -> conventional imaging condition; 1 -> stable imaging condition for Q-compensation with global nomalization; 2 -> shot-by-shot normalization; 3 -> snapshot-by-snapshot compensation (most intensive); 4 -> deconvolution imaging condition 
Param:  tmpwf string  -   -  		auxiliary output file name
Param:  tmpwfb string  -   -  		auxiliary output file name
Param:  top int  -  40 		
Param:  verb enum-bool  -  n 		verbosity

