[sfoff2abs]
Cat:    RSF/user/psava
Desc:   Transform vector-offset to absolute-offset
DocCmd: sfoff2abs | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fm data)
Param:  dh float  -   -  		
LDesc:  (defaults to: dhx)
Param:  nh int  -   -  		
LDesc:  (defaults to: nhx + ohx/dhx)
Param:  nw int  -  4 		spline order 
Param:  oh float  -  0 		
Param:  verb enum-bool  -  n 		verbosity flag 

