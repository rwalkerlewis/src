[sfvariogram2]
Cat:    RSF/user/yliu
Desc:   Compute a horizontal variogram of data slice
DocCmd: sfvariogram2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dh1 int  -  1 		interval (jump) of variogram lag in first axis 
Param:  dh2 int  -  1 		interval (jump) of variogram lag in second axis 
Param:  nh1 int  -   -  		number of variogram lag in first axis 
LDesc:  (defaults to: n1/dh1)
Param:  nh2 int  -   -  		number of variogram lag in second axis 
LDesc:  (defaults to: n2/dh2)
Param:  semi enum-bool  -  y 		if y, output semivariogram 
Param:  verb enum-bool  -  n 		verbosity 

