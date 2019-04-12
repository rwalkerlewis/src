[sfvofz]
Cat:    RSF/system/seismic
Desc:   Analytical traveltime in a linear V(z) model
DocCmd: sfvofz | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		vertical sampling 
LDesc:  (defaults to: 0.5/(n1-1))
Param:  d2 float  -   -  		horizontal sampling 
LDesc:  (defaults to: 1./(n2-1))
Param:  g float  -  1. 		velocity gradient 
Param:  intime enum-bool  -  n 		if in vertical time coordinates 
Param:  n int  -   -  		number of samples 
Param:  n1 int  -   -  		vertical samples 
Param:  n2 int  -   -  		horizontal samples 
Param:  o1 float  -  0. 		vertical origin 
Param:  o2 float  -  0. 		horizontal origin 
Param:  s float  -  0.5 		shot location at the surface 
Param:  v0 float  -  0.5 		initial velocity 

