[sfisaac0]
Cat:    RSF/user/zone
Desc:   Zero-offset bending ray tracing in one-layered media
DocCmd: sfisaac0 | cat
Port:   stdin  rsf r req 	RSF standard input (containing refl data)
Port:   stdout rsf w req 	RSF standard output (containing ttime data)
Port:   xrefl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  ds float  -   -  		source sampling 
LDesc:  (defaults to: dr)
Param:  ns int  -   -  		Number of sources 
LDesc:  (defaults to: nr)
Param:  order int  -  3 		interpolation order 
Param:  s0 float  -   -  		source origin 
LDesc:  (defaults to: r0)
Param:  tol float  -   -  		assign a default value for tolerance
LDesc:  (defaults to: 0.0001/velocity)
Param:  velocity float  -  2.0 		assign velocity km/s

