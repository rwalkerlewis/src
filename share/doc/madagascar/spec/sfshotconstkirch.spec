[sfshotconstkirch]
Cat:    RSF/system/seismic
Desc:   Prestack shot-profile Kirchhoff migration in constant velocity
DocCmd: sfshotconstkirch | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  aal enum-bool  -  y 		if y, apply antialiasing 
Param:  dx float  -   -  		
LDesc:  (defaults to: ds)
Param:  nx int  -   -  		
LDesc:  (defaults to: ns)
Param:  offset enum-bool  -  n 		if y, the output is in offset 
Param:  vel float  -   -  		velocity 
Param:  x0 float  -   -  		
LDesc:  (defaults to: s0)

