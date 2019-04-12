[sfoff2abs3]
Cat:    RSF/user/psava
Desc:   Transform vector-offset to absolute-offset
DocCmd: sfoff2abs3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fm data)
Port:   stdout rsf w req 	RSF standard output (containing Fd data)
Param:  da float  -  2. 		
Param:  db float  -  2. 		
Param:  dh float  -   -  		
LDesc:  (defaults to: dhx)
Param:  na int  -  180 		
Param:  nb int  -  180 		
Param:  nh int  -   -  		
LDesc:  (defaults to: nhx + ohx/dhx)
Param:  nw int  -  4 		spline order 
Param:  oa float  -  0. 		
Param:  ob float  -  0. 		
Param:  oh float  -  0 		
Param:  verb enum-bool  -  n 		verbosity flag 

