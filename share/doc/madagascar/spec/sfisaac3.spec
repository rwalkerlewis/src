[sfisaac3]
Cat:    RSF/user/zone
Desc:   3D Bending ray tracing in Multi-layered media
DocCmd: sfisaac3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing refl data)
Port:   stdout rsf w req 	RSF standard output (containing xrefl data)
Port:   aniso rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  debug enum-bool  -  n 		Debug flag
Param:  ds float  -  1 		Step increment
Param:  layer float-list  -   -  		Layer sequence [nr3+1]
Param:  niter int  -   -  		The number of iterations
Param:  ns int  -  3  		Dimension of output reflection points (x,y,z) 
Param:  ns2 int  -   -  		Dimension of output reflection points (the number of points)
LDesc:  (defaults to: nr3+2)
Param:  number int  -   -  		Number of reflectors
Param:  order int  -  3 		Interpolation order
Param:  s0 float  -  0 		Staring position
Param:  tol double  -   -  		Assign a default value for tolerance
LDesc:  (defaults to: 0.000001/v_inp[0])
Param:  velocity float-list  -   -  		Assign velocity km/s [N-1]
Param:  vstatus int  -   -  		Velocity status (0 for constant v, 1 for gradient v, and 2 for VTI)
Param:  xgradient float-list  -   -  		Assign x-gradient [N-1]
Param:  xinitial float-list  -   -  		 [nr3]
Param:  xmax float  -   -  		
Param:  xmin float  -   -  		
Param:  xr float  -   -  		x-Receiver
Param:  xref float-list  -   -  		Assign x-reference point [N-1]
Param:  xs float  -   -  		x-Source
Param:  ygradient float-list  -   -  		Assign y-gradient [N-1]
Param:  yinitial float-list  -   -  		 [nr3]
Param:  ymax float  -   -  		
Param:  ymin float  -   -  		
Param:  yr float  -   -  		y-Receiver
Param:  yref float-list  -   -  		Assign y-reference point [N-1]
Param:  ys float  -   -  		y-Source
Param:  zgradient float-list  -   -  		Assign z-gradient  [N-1]
Param:  zref float-list  -   -  		Assign z-reference point [N-1]

