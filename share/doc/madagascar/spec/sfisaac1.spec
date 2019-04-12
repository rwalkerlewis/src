[sfisaac1]
Cat:    RSF/user/zone
Desc:   Pre-stack bending ray tracing in one-layered media
DocCmd: sfisaac1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing refl data)
Port:   stdout rsf w req 	RSF standard output (containing ttime data)
Port:   xrefl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  break enum-bool  -  n 		Go beyond zero or not
Param:  ds float  -   -  		source sampling for midpoint
LDesc:  (defaults to: dr)
Param:  ds2 float  -   -  		source sampling for offset
LDesc:  (defaults to: dr)
Param:  ns int  -   -  		number of sources for midpoint
LDesc:  (defaults to: nr)
Param:  ns2 int  -   -  		number of sources for offset
LDesc:  (defaults to: nr)
Param:  order int  -  4 		Interpolation order if choose to use sf_eno
Param:  s0 float  -   -  		origin for midpoint
LDesc:  (defaults to: r0)
Param:  s02 float  -   -  		origin for offset
LDesc:  (defaults to: r0)
Param:  tol float  -   -  		Assign a default value for tolerance
LDesc:  (defaults to: 1/(1000000*velocity))
Param:  type int  -  1 		Interpolation type 0=sf_eno and 1=central finite difference
Param:  velocity float  -  2.0 		Assign velocity km/s

