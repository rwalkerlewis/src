[sfiwigrad]
Cat:    RSF/user/sparse
Desc:   Image-domain waveform tomography (gradient)
DocCmd: sfiwigrad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  cost string  -   -  		cost functional type (default classic DSO) 
Param:  data string  -   -  		auxiliary input file name
Param:  dorder int  -  6 		image derivative accuracy order 
Param:  geps float  -  0. 		regularization parameter for Gauss-Newton 
Param:  gliter int  -  1 		# of Gauss-Newton iterations 
Param:  grect1 int  -  5 		gradient smoothing radius on axis 1 
Param:  grect2 int  -  5 		gradient smoothing radius on axis 2 
Param:  gscale float  -  0.5 		gradient re-scale 
Param:  imask string  -   -  		auxiliary input file name
Param:  load enum-bool  -  n 		load LU 
Param:  lower float  -  1.5 		lower bound of feasible set 
Param:  miter int  -  10 		Nonlinear-CG maximum # of iterations 
Param:  nh int  -  0 		horizontal space-lag 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  pliter int  -  20 		slope estimation # of linear iterations 
Param:  plower float  -  0.1 		slope thresholding lower limit 
Param:  precon string  -   -  		auxiliary input file name
Param:  prect1 int  -  5 		slope smoothing radius on axis 1 
Param:  prect2 int  -  1 		slope smoothing radius on axis 2 
Param:  prect3 int  -  5 		slope smoothing radius on axis 3 
Param:  pupper float  -  3. 		slope thresholding upper limit 
Param:  source string  -   -  		auxiliary input file name
Param:  update enum-bool  -  y 		Non-linear CG update 
Param:  upper float  -  7.5 		upper bound of feasible set 
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight string  -   -  		auxiliary input file name

