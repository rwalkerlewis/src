[sfisin2ang]
Cat:    RSF/system/seismic
Desc:   inverse sin to angle transformation
DocCmd: sfisin2ang | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fstk data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a0 float  -  0. 		angle origin 
Param:  da float  -   -  		angle sampling 
LDesc:  (defaults to: 90/(nt-1))
Param:  extend int  -  4 		tmp extension 
Param:  na int  -   -  		number of angles
LDesc:  (defaults to: nt)
Param:  top enum-bool  -  n 		velocity scaling option 

