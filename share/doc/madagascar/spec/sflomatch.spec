[sflomatch]
Cat:    RSF/user/lcasasan
Desc:   Local Matched filter for coherent noise removal (1-D, 2-D, and 3-D)
DocCmd: sflomatch | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing mcf data)
Param:  a int-list  -   -  		filter size  [dim1]
Param:  center int-list  -   -  		filter center  [dim1]
Param:  dim int  -   -  		matched filter  dimensionality 
LDesc:  (defaults to: dim)
Param:  eps float  -  0.01 		dumping parameter x=(M'M+eps*I)M'd 
Param:  gap int-list  -   -  		filter gap  [dim1]
Param:  k int-list  -   -  		number of windows  [dim1]
Param:  lag string  -   -  		output file for filter lags 
Param:  liter int  -   -  		number of linear iteration
LDesc:  (defaults to: aa->nh)
Param:  mask string  -   -  		auxiliary input file name
Param:  match string  -   -  		auxiliary input file name
Param:  niter int  -  1 		number of POCS iterations: =1 L2 norm ; >1 L1 norm 
Param:  perc float  -  90.0 		percentage for sharpening [L1 norm]
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w int-list  -   -  		window size  [dim1]

