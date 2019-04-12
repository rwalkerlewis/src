[sfnnint]
Cat:    RSF/user/fomels
Desc:   Natural neighbor interpolation (2-D)
DocCmd: sfnnint | cat
Port:   stdin  rsf r req 	RSF standard input (containing ord data)
Port:   stdout rsf w req 	RSF standard output (containing grid data)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 float  -   -  		
Param:  d2 float  -   -  		sampling 
Param:  dist enum-bool  -  n 		if output distance 
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		dimensions 
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		origin 
Param:  order int  -  2 		Accuracy order for distance calculation 
Param:  repeat int  -  1 		
Param:  vel enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  velocity string  -   -  		auxiliary input file name
Param:  voro enum-bool  -  n 		if output Voronoi diagram 

