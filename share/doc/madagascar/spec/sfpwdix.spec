[sfpwdix]
Cat:    RSF/user/pwd
Desc:   Convert RMS to interval velocity using LS and plane-wave construction
DocCmd: sfpwdix | cat
Port:   stdin  rsf r req 	RSF standard input (containing vrms data)
Port:   stdout rsf w req 	RSF standard output (containing vint data)
Port:   slope rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   weight rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0. 		regularization parameter 
Param:  ncycle int  -  10 		number of cycles for anisotropic diffusion 
Param:  niter int  -  100 		maximum number of iterations 
Param:  order int  -  1 		accuracy order 
Param:  rect1 int  -  1 		vertical smoothing radius 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  vrmsout string  -   -  		optionally, output predicted vrms (auxiliary output file name)

