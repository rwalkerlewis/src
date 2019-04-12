[sfvelinv]
Cat:    RSF/user/fomels
Desc:   Velocity transform for generating velocity spectra and its corresponding hyperbolic modeling
DocCmd: sfvelinv | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing vtr data)
Param:  adj enum-bool  -  n 		adj = 0: from velocity-domain(t,s) to cmp-gather(t,x)
LDesc:         adj = 1: from cmp-gather(t,x) to velocity-domain(t,s) 
Param:  ds float  -  0.001 		slowness sampling 
Param:  dx float  -  10. 		offset sampling 
Param:  eps float  -  1. 		regularization parameter for robust inversion 
Param:  niter int  -  0 		number of iterations (invoked if adj=y) 
Param:  nliter int  -  10 		number of POCS iterations for robust inversion 
Param:  ns int  -   -  		number of slowness values 
LDesc:  (defaults to: nx)
Param:  nx int  -   -  		number of offset values 
LDesc:  (defaults to: ns)
Param:  os float  -  0.00000001 		slowness origin 
Param:  ox float  -  0. 		offset origin 
Param:  perc float  -  90. 		threshold percentage for robust inversion 
Param:  robust enum-bool  -  n 		robust inversion 

