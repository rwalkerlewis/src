[sfpwsmooth3]
Cat:    RSF/user/yliu
Desc:   3-D structural-oriented smoothing using plane-wave spray and weighted stacking
DocCmd: sfpwsmooth3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ax float  -   -  		Gaussian weight for the range distance 
Param:  bilat enum-bool  -  n 		if y, bilateral smoothing 
Param:  bx float  -   -  		exponential weight for the domain distance 
Param:  eps float  -  0.01 		regularization 
Param:  gauss enum-bool  -  n 		if y, gaussian weight; otherwise, triangle weight 
Param:  ns2 int  -   -  		spray radius (inline) 
Param:  ns3 int  -   -  		spray radius (crossline) 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		verbosity 

