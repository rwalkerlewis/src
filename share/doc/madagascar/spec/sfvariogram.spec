[sfvariogram]
Cat:    RSF/user/yliu
Desc:   Compute a variogram of data values
DocCmd: sfvariogram | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dh int  -  1 		interval (number) of variogram lag 
Param:  nh int  -   -  		number of variogram lag 
LDesc:  (defaults to: n1/dh-oh)
Param:  oh int  -  0 		origin (number) of variogram lag 
Param:  semi enum-bool  -  y 		if y, output semivariogram 

