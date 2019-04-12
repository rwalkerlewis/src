[sfsmoothcur]
Cat:    RSF/user/lcasasan
Desc:   Convert input slope and time derivative
DocCmd: sfsmoothcur | cat
Port:   stdin  rsf r req 	RSF standard input (containing DATA data)
Port:   stdout rsf w req 	RSF standard output (containing MODEL data)
Port:   dipt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dataout string  -   -  		optionally, output predicted data (auxiliary output file name)
Param:  eps float  -  1.0 		dumping factor
Param:  niter int  -  100 		maximum number of iterations 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))

