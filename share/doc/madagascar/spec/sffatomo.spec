[sffatomo]
Cat:    RSF/user/llisiw
Desc:   First-arrival Traveltime Tomography
DocCmd: sffatomo | cat
Port:   stdin  rsf r req 	RSF standard input (containing sinp data)
Port:   stdout rsf w req 	RSF standard output (containing sout data)
Param:  adj enum-bool  -  n 		adjoint flag (for what=linear) 
Param:  eps float  -  0. 		regularization parameter 
Param:  gradient string  -   -  		auxiliary output file name
Param:  l1norm enum-bool  -  n 		norm for minimization (default L2 norm) 
Param:  misnorm string  -   -  		auxiliary output file name
Param:  nfreq int  -  1 		l1-norm weighting nfreq 
Param:  niter int  -  10 		number of slowness inversion iterations 
Param:  nmem int  -  1 		l1-norm weighting nmem 
Param:  order int  -  2 		fast marching accuracy order 
Param:  perc float  -  90. 		
Param:  receiver string  -   -  		auxiliary input file name
Param:  record string  -   -  		auxiliary input file name
Param:  shot string  -   -  		auxiliary input file name
Param:  stiter int  -  200 		number of step iterations 
Param:  time string  -   -  		auxiliary input file name
Param:  topo string  -   -  		auxiliary input file name
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  what string  -   -  		what to compute (default tomography) 

