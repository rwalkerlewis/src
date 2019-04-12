[sfiwinlcg]
Cat:    RSF/user/sparse
Desc:   Image-domain waveform tomography (Non-linear CG)
DocCmd: sfiwinlcg | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  cost string  -   -  		cost functional type (default Weibull) 
Param:  data string  -   -  		auxiliary input file name
Param:  delta float  -  1.e-5 		Nonlinear-CG convergence criteria 
Param:  dorder int  -  6 		image derivative accuracy order 
Param:  geps float  -  0. 		regularization parameter for Gauss-Newton 
Param:  gliter int  -  5 		# of Gauss-Newton iterations 
Param:  grad string  -   -  		auxiliary output file name
Param:  grect1 int  -  5 		gradient smoothing radius on axis 1 
Param:  grect2 int  -  5 		gradient smoothing radius on axis 2 
Param:  gscale float  -  0.1 		gradient re-scale 
Param:  imag string  -   -  		auxiliary output file name
Param:  imask string  -   -  		auxiliary input file name
Param:  liter int  -  5 		Nonlinear-CG maximum # of line searches 
Param:  load enum-bool  -  n 		load LU 
Param:  lower float  -  1.5 		lower bound of feasible set 
Param:  miter int  -  10 		Nonlinear-CG maximum # of iterations 
Param:  nh int  -  0 		horizontal space-lag 
Param:  npml int  -  10 		PML width 
Param:  objt string  -   -  		auxiliary output file name
Param:  order string  -   -  		discretization scheme (default optimal 25-point) 
Param:  pliter int  -  20 		slope estimation # of linear iterations 
Param:  plower float  -  0.1 		slope thresholding lower limit 
Param:  precon string  -   -  		auxiliary input file name
Param:  prect1 int  -  5 		slope smoothing radius on axis 1 
Param:  prect2 int  -  1 		slope smoothing radius on axis 2 
Param:  prect3 int  -  5 		slope smoothing radius on axis 3 
Param:  pupper float  -  3. 		slope thresholding upper limit 
Param:  source string  -   -  		auxiliary input file name
Param:  update enum-bool  -  y 		y, nonlinear CG; n, Gauss-Newton 
Param:  upper float  -  7.5 		upper bound of feasible set 
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  weight string  -   -  		auxiliary input file name

