[sfvelinvnew]
Cat:    RSF/user/seisinv
Desc:   None
DocCmd: sfvelinvnew | cat
Port:   stdin  rsf r req 	RSF standard input (containing infile data)
Port:   stdout rsf w req 	RSF standard output (containing outfile data)
Port:   mres rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   res rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel0 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velout rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  alpha   -   -  		smoothing parameter, typical value: 1 to 10 times estimated norm(x,inf)
Param:  delta   -   -  		delta controls update step and convergent, small delta ensure convergence but with small decrease in data fit error
LDesc:  (defaults to: 0.0001)
Param:  dv   -   -  		
LDesc:  (defaults to: 0.01)
Param:  eps   -   -  		
LDesc:  (defaults to: 0.01)
Param:  flag   -   -  		
LDesc:  (defaults to: 0)
Param:  huber   -   -  		
LDesc:  (defaults to: 0)
Param:  irls   -   -  		
LDesc:  (defaults to: 0)
Param:  lamda   -   -  		lamda controls sparsity, bigger lamda, more sparsity
LDesc:  (defaults to: 1000.)
Param:  lip   -   -  		the estimated Lipschitz constrant of the dual objective, default: alpha*normest(A*A',1e-2)
Param:  mflag   -   -  		
LDesc:  (defaults to: 0)
Param:  mwt   -   -  		
LDesc:  (defaults to: 0.)
Param:  niter   -   -  		
LDesc:  (defaults to: 20)
Param:  nstep   -   -  		
LDesc:  (defaults to: 1)
Param:  nv   -   -  		
LDesc:  (defaults to: nhx)
Param:  ov   -   -  		
LDesc:  (defaults to: 1.5)
Param:  reset   -   -  		Nesterov's acceleration restart (theta is reset) or skip (theta is not reset)
Param:  rwt   -   -  		
LDesc:  (defaults to: 0.)
Param:  savevel   -   -  		Flag to choose the algorithm
LDesc:  (defaults to: 0)
Param:  srate   -   -  		
LDesc:  (defaults to: 0.01)
Param:  step   -   -  		step is very important in convergence and sparsity
LDesc:  (defaults to: 0.000005)

