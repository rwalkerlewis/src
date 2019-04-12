[sfnmo3mcmc]
Cat:    RSF/user/zone
Desc:   3D NMO GMA MCMC inversion with Metropolis rule (Mosegaard and Tarantola, 1995)
DocCmd: sfnmo3mcmc | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   rangecoef rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   t0sq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nmodel int  -  1000 		Get the number of MC models
Param:  prior enum-bool  -  n 		generate prior or posterior 
Param:  saveiter int  -  20 		save state every iter  
Param:  seed int  -   -  		random seed 
LDesc:  (defaults to: time(NULL))
Param:  sigma float  -  1.0 		noise variance 

