[sfzmarch]
Cat:    RSF/user/fomels
Desc:   Phase-space traveltime (marching in z)
DocCmd: sfzmarch | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a0 float  -   -  		starting velocity 
Param:  da float  -   -  		angle sampling 
Param:  na int  -   -  		angle samples 
Param:  order int  -  3 		interpolation order 
Param:  scheme int  -  2 		finite-difference order 
Param:  verb enum-bool  -  n 		verbosity 
Param:  what string  -   -  		what to compute (t,x,z,a) 

