[sfdrayinte]
Cat:    RSF/user/llisiw
Desc:   2D Dynamic Ray Tracing
DocCmd: sfdrayinte | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  deriv string  -   -  		auxiliary input file name
Param:  shift float  -  1. 		complex source shift 
Param:  source float  -   -  		source location 
LDesc:  (defaults to: o[1]+(n[1]-1)/2*d[1])
Param:  t0 float  -  0. 		time origin at source 

