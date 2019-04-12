[sfitrace]
Cat:    RSF/user/aklokov
Desc:   
DocCmd: sfitrace | cat
Port:   stdin  rsf r req 	RSF standard input (containing xEscFile data)
Port:   stdout rsf w req 	RSF standard output (containing xResFile data)
Param:  dt float  -   -  		time-range for point detection 
LDesc:  (defaults to: 0.02f)
Param:  dx float  -   -  		x-range for point detection 
LDesc:  (defaults to: 5*xStep)
Param:  esct string  -   -  		escape-time file (auxiliary input file name)
Param:  p0 float  -   -  		migration angle 
LDesc:  (defaults to: 0.f)
Param:  sa0 float  -   -  		scattering-angle 
LDesc:  (defaults to: 0.f)
Param:  x0 float  -   -  		x-coordinate of the diffraction point 
LDesc:  (defaults to: 0.f)
Param:  z0 float  -   -  		z-coordinate of the diffraction point 
LDesc:  (defaults to: 0.f)
Param:  zres string  -   -  		auxiliary output file name

