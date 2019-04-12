[sfpveltran3]
Cat:    RSF/system/seismic
Desc:   Slope-based tau-p 3D velocity transform for elliptical anisotropy
DocCmd: sfpveltran3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing input data)
Port:   stdout rsf w req 	RSF standard output (containing velx data)
Port:   velxy rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vely rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cmp string  -   -  		auxiliary input file name
Param:  dipx string  -   -  		auxiliary input file name
Param:  dipxy string  -   -  		auxiliary input file name
Param:  dipy string  -   -  		auxiliary input file name
Param:  dvx float  -   -  		vx squared velocity sampling 
Param:  dvxy float  -  0.1 		vxy   velocity sampling 
Param:  dvy float  -   -  		vy squared  velocity sampling 
LDesc:  (defaults to: dvx)
Param:  interval enum-bool  -  n 		interval values by 3D stripping equations 
Param:  map enum-bool  -  n 		output maps instead of coherency panels 
Param:  nvx int  -   -  		number of vx squared velocities 
Param:  nvxy int  -  101 		number of vxy velocities 
Param:  nvy int  -   -  		number of vy squared velocities  
LDesc:  (defaults to: nvx)
Param:  nw int  -  4 		interpolator size (2,3,4,6,8) 
Param:  vx0 float  -   -  		vx squared velocity origin 
Param:  vxy0 float  -  -0.1 		vxy   velocity origin 
Param:  vy0 float  -   -  		vy squared  velocity origin 
LDesc:  (defaults to: vx0)

