[sfcpxeikonal]
Cat:    RSF/user/llisiw
Desc:   Iterative complex eikonal solver
DocCmd: sfcpxeikonal | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  alpha float  -  1. 		exponential scaling of preconditioning 
Param:  bound string  -   -  		avoid overshoot when update (default add) 
Param:  cgiter int  -  200 		number of conjugate gradient iterations 
Param:  cray string  -   -  		auxiliary input file name
Param:  dwiter string  -   -  		auxiliary output file name
Param:  dwsiter string  -   -  		auxiliary output file name
Param:  eps float  -  1.e-2 		stable division of preconditioner 
Param:  gamiter string  -   -  		auxiliary output file name
Param:  liniter string  -   -  		auxiliary output file name
Param:  maski string  -   -  		auxiliary input file name
Param:  maskr string  -   -  		auxiliary input file name
Param:  matiiter string  -   -  		auxiliary output file name
Param:  matriter string  -   -  		auxiliary output file name
Param:  namda float  -  0.1 		regularization parameter (Ticknov) 
Param:  niter int  -  1 		number of iterations 
Param:  nstep int  -  10 		number of linesearch 
Param:  operiter string  -   -  		auxiliary output file name
Param:  prec string  -   -  		rhs preconditioning (default angle) 
Param:  preciter string  -   -  		auxiliary output file name
Param:  pvar enum-bool  -  y 		allow preconditioning to change over iterations 
Param:  recom enum-bool  -  y 		recompute initial R according to w estimated from I 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  reg enum-bool  -  n 		regularization (Ticknov) 
Param:  repeat int  -  1 		number of smoothings 
Param:  rhsiter string  -   -  		auxiliary output file name
Param:  smooth enum-bool  -  n 		smooth update after conjugate-gradient 
Param:  symm string  -   -  		right-hand side evaluation L_R*I or L_I*R (default both) 
Param:  term enum-bool  -  n 		early termination if line-search failure 
Param:  titer string  -   -  		auxiliary output file name
Param:  tol float  -  1.e-8 		thresholding for gradient scaling 
Param:  upiter string  -   -  		auxiliary output file name
Param:  vel string  -   -  		auxiliary input file name
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness squared 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wght string  -   -  		auxiliary input file name
Param:  witer string  -   -  		auxiliary output file name
Param:  wtiter string  -   -  		auxiliary output file name
Param:  wupg enum-bool  -  y 		compute w for angle preconditioning 
Param:  x0iter string  -   -  		auxiliary output file name

