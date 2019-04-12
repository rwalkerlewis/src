[sfrandrefl]
Cat:    RSF/system/seismic
Desc:   Simple synthetics with random reflectivity
DocCmd: sfrandrefl | cat
Port:   stdout rsf w req 	RSF standard output (containing mod data)
Port:   vpvs rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  d1 float  -  0.001 		time sampling 
Param:  fo float-list  -   -  		 [3]
Param:  func string  -   -  		type of vpvs function 
Param:  n1 int  -  3501 		time length 
Param:  nr int  -   -  		number of reflectors 
Param:  o1 float  -  0.0 		time origin 
Param:  tscale float  -  1. 		maximum time 

