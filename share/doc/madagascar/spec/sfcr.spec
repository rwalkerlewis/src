[sfcr]
Cat:    RSF/user/fomels
Desc:   Column-row matrix decomposition
DocCmd: sfcr | cat
Port:   stdin  rsf r req 	RSF standard input (containing row_in data)
Port:   stdout rsf w req 	RSF standard output (containing row_out data)
Port:   col_in rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   col_out rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  niter int  -  10 		number of iterations 
Param:  prec enum-bool  -  y 		If apply preconditioning 
Param:  tol float  -   -  		CG tolerance 
LDesc:  (defaults to: 0.0f)

