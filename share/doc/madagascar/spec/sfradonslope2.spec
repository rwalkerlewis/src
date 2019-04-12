[sfradonslope2]
Cat:    RSF/user/browaeys
Desc:   Directional angle transform for 3-D time image cube I(x,z,t) into G(x,z,d)
DocCmd: sfradonslope2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fimgt data)
Port:   stdout rsf w req 	RSF standard output (containing Fimgd data)
Port:   slowness rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d0 float  -  -80.0 		
Param:  dd float  -   -  		
LDesc:  (defaults to: 160.0/(nt-1))
Param:  nd int  -   -  		
LDesc:  (defaults to: nt)
Param:  verb enum-bool  -  n 		verbosity flag 

