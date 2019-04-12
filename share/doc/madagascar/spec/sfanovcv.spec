[sfanovcv]
Cat:    RSF/user/dmerzlikin
Desc:   Oriented anisotropy continuation: shifted hyperbola travel-time approximation
DocCmd: sfanovcv | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  clip float  -  0.5 		maximum stretch 
Param:  debug enum-bool  -  y 		Implement debugger: add it later 
Param:  ds float  -   -  		s step size 
Param:  eps float  -  0.1 		stretch regularization 
Param:  epsr float  -  0.001 		damper for root 
Param:  full enum-bool  -  n 		full accuracy flag - considers all (s-1) terms in any power 
Param:  isotr enum-bool  -  n 		Implement debugger: add it later 
Param:  kappa1 string  -   -  		auxiliary output file name
Param:  kappa2 string  -   -  		auxiliary output file name
Param:  kappa3 string  -   -  		auxiliary output file name
Param:  lagrange enum-bool  -  n 		Use Lagrangian method 
Param:  ns int  -  1 		s steps 
Param:  nv int  -  1 		number of velocity steps 
Param:  plus enum-bool  -  y 		Plus or minus in coefficients: I have two versions 
Param:  rootin string  -   -  		auxiliary output file name
Param:  s0 float  -   -  		start 
Param:  smax float  -   -  		
Param:  testwarp enum-bool  -  n 		Implement debugger: add it later 
Param:  v0 float  -   -  		constant velocity (if no velocity=) 
Param:  velocity string  -   -  		velocity file (auxiliary input file name)
Param:  windowtime float  -   -  		maximum time 2 consider 
LDesc:  (defaults to: t0 + (nt-1.0)*dt)

