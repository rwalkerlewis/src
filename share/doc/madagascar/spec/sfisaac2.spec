[sfisaac2]
Cat:    RSF/user/zone
Desc:   2D Bending ray tracing in multi-layered media
DocCmd: sfisaac2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing refl data)
Port:   stdout rsf w req 	RSF standard output (containing xrefl data)
Port:   aniso rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  debug enum-bool  -  n 		Debug flag
Param:  ds float  -  1 		Step increment
Param:  layer float-list  -   -  		Layer sequence [nr2+1]
Param:  max float  -   -  		The maximum boundary if not entered, set to max(xs,xr)
LDesc:  (defaults to: (xx[0]>xx[nr2+1])? xx[0]:xx[nr2+1])
Param:  min float  -   -  		The minimum boundary if not entered, set to min(xs,xr)
LDesc:  (defaults to: (xx[0]<xx[nr2+1])? xx[0]:xx[nr2+1])
Param:  niter int  -  100 		The number of iterations
Param:  ns int  -  2 		Dimension of output reflection points (x,z)
Param:  ns2 int  -   -  		Dimension of output reflection points (the number of points)
LDesc:  (defaults to: nr2+2)
Param:  number int  -   -  		Number of intersecting points [nr2]
Param:  order int  -  3 		Interpolation order
Param:  s0 float  -  0 		Staring position
Param:  tol double  -   -  		Assign a default value for tolerance
LDesc:  (defaults to: 0.000001/v_inp[0])
Param:  velocity float-list  -   -  		Assign velocity km/s [N-1]
Param:  vstatus int  -   -  		Velocity status (0 for constant v, 1 for gradient v, and 2 for VTI)
Param:  xgradient float-list  -   -  		Assign x-gradient [N-1]
Param:  xinitial float-list  -   -  		 [nr2]
Param:  xr float  -   -  		Receiver
Param:  xref float-list  -   -  		Assign x-reference point [N-1]
Param:  xs float  -   -  		Source
Param:  zgradient float-list  -   -  		Assign z-gradient  [N-1]
Param:  zref float-list  -   -  		Assign z-reference point [N-1]

