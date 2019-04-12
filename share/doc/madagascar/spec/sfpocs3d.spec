[sfpocs3d]
Cat:    RSF/user/pyang
Desc:   POCS for 3D missing data interpolation
DocCmd: sfpocs3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		total number of POCS iterations 
Param:  pclip float  -  99. 		starting data clip percentile (default is 99)
Param:  verb enum-bool  -  n 		verbosity 

