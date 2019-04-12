[sfshapebin]
Cat:    RSF/system/generic
Desc:   Data binning in 2-D slices by inverse interpolation
DocCmd: sfshapebin | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dx float  -   -  		bin size in x 
Param:  dy float  -   -  		bin size in y 
Param:  eps float  -   -  		regularization parameter 
LDesc:  (defaults to: 1./nd)
Param:  filt1 float  -  3. 		
Param:  filt2 float  -   -  		smoothing length for shaping 
LDesc:  (defaults to: filt1)
Param:  gauss enum-bool  -  n 		if y, use gaussian shaping (estimated from the data) 
Param:  head string  -   -  		
Param:  interp int  -  2 		interpolation length 
Param:  niter int  -   -  		number of iterations 
LDesc:  (defaults to: nm)
Param:  nliter int  -  1 		number of reweighting iterations 
Param:  nx int  -   -  		Number of bins in x 
Param:  ny int  -   -  		Number of bins in y 
Param:  pattern string  -   -  		auxiliary input file name
Param:  pin string  -   -  		auxiliary input file name
Param:  pout string  -   -  		auxiliary output file name
Param:  shape enum-bool  -  y 		if y, use shaping regularization 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  x0 float  -   -  		
LDesc:  (defaults to: xmin)
Param:  xkey int  -   -  		x key number 
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		
Param:  y0 float  -   -  		grid origin 
LDesc:  (defaults to: ymin)
Param:  ykey int  -   -  		y key number 
Param:  ymax float  -   -  		
Param:  ymin float  -   -  		Grid dimensions 

