[sfiwilbfgs]
Cat:    RSF/user/sparse
Desc:   Image-domain waveform tomography (L-BFGS)
DocCmd: sfiwilbfgs | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  beta float  -  0. 		stacking power cost function 
Param:  data string  -   -  		auxiliary input file name
Param:  deriv enum-bool  -  y 		if y, apply derivative in z 
Param:  epsilon float  -  1.e-7 		L-BFGS termination epsilon 
Param:  grad string  -   -  		auxiliary output file name
Param:  grect1 int  -  5 		gradient smoothing radius on axis 1 
Param:  grect2 int  -  5 		gradient smoothing radius on axis 2 
Param:  gscale float  -  -1. 		gradient re-scale (enabled if (0,1)) 
Param:  load enum-bool  -  n 		load LU 
Param:  lower float  -  1.5 		lower bound of feasible set 
Param:  miter int  -  10 		L-BFGS maximum # of iterations 
Param:  mline int  -  5 		L-BFGS maximum # of line search 
Param:  nh int  -  0 		horizontal space-lag 
Param:  nhess int  -  6 		L-BFGS # of Hessian corrections 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  precon string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  upper float  -  7.5 		upper bound of feasible set 
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  wdso string  -   -  		auxiliary input file name
Param:  wstk string  -   -  		auxiliary input file name

