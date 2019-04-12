[sfdistance]
Cat:    RSF/user/fomels
Desc:   Computing distance function by fast marching eikonal solver (3-D)
DocCmd: sfdistance | cat
Port:   stdin  rsf r req 	RSF standard input (containing points data)
Port:   stdout rsf w req 	RSF standard output (containing dist data)
Param:  d1 float  -   -  		
Param:  d2 float  -   -  		
Param:  d3 float  -   -  		sampling 
LDesc:  (defaults to: d2)
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  n3 int  -  1 		dimensions 
Param:  o1 float  -  0. 		
Param:  o2 float  -  0. 		
Param:  o3 float  -  0. 		origin 
Param:  order int  -  2 		Accuracy order 
Param:  vel enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  velocity string  -   -  		auxiliary input file name

