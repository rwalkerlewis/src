[sfmiss2]
Cat:    RSF/system/generic
Desc:   2-D missing data interpolation
DocCmd: sfmiss2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.0001 		regularization parameter 
Param:  filt1 float  -  3. 		
Param:  filt2 float  -   -  		smoothing radius 
LDesc:  (defaults to: filt1)
Param:  force enum-bool  -  y 		if y, keep known values 
Param:  mask string  -   -  		optional input mask file for known data (auxiliary input file name)
Param:  niter int  -  100 		Number of iterations 
Param:  nliter int  -  1 		Number of reweighting iterations 
Param:  shape enum-bool  -  n 		if y, estimate shaping 

