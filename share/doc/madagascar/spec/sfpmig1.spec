[sfpmig1]
Cat:    RSF/user/lcasasan
Desc:   Slope-based prestack (t,xs,h) time migration
DocCmd: sfpmig1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing csg data)
Port:   stdout rsf w req 	RSF standard output (containing mig data)
Port:   hdip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sdip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  mzo enum-bool  -  n 		do migration to zero offset 
Param:  nw int  -  4 		interpolator size (2,3,4,6,8) 

