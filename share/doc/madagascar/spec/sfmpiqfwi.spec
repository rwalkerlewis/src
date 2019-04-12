[sfmpiqfwi]
Cat:    RSF/user/zhiguang
Desc:   Visco-acoustic (SLS) Forward Modeling, FWI, and RTM
DocCmd: sfmpiqfwi | cat
Port:   Ferr rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Ftau rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  acqui_type int  -  1 		if 1, fixed acquisition; if 2, marine acquisition; if 3, symmetric acquisition 
Param:  coef float  -  0.002 		absorbing boundary coefficient 
Param:  conv_error float  -   -  		final convergence error 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: acpar->dx)
Param:  ds float  -   -  		shot interval 
Param:  f0 float  -   -  		reference frequency 
Param:  factor float  -  10 		step length increase factor 
Param:  fhi float  -   -  		high frequency in band, default is Nyquist 
LDesc:  (defaults to: 0.5/acpar->dt)
Param:  flo float  -  0. 		low frequency in band, default is zero 
Param:  frectx int  -  2 		source smoothing in x 
Param:  frectz int  -  2 		source smoothing in z 
Param:  function int  -  2 		if 1, forward modeling; if 2, FWI; if 3, RTM 
Param:  gain float  -  1 		vertical gain power of data residual 
Param:  grad_type int  -  1 		if 1, velocity; if 2, Q; if 3, velocity and Q 
Param:  grectx int  -  3 		gradient smoothing radius in x 
Param:  grectz int  -  3 		gradient smoothing radius in z 
Param:  interval int  -  1 		wavefield storing interval 
Param:  nb int  -  100 		boundary width 
Param:  niter int  -   -  		iteration number 
Param:  nls int  -  20 		line search number 
Param:  npair int  -  20 		number of l-BFGS pairs 
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: acpar->nx)
Param:  ns int  -   -  		shot number 
Param:  onlygrad enum-bool  -  n 		only calculate gradident or not 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: acpar->x0)
Param:  repeat int  -  5 		after how many iterations the step length goes back to 1 
Param:  rz int  -  5 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  sz int  -  5 		source depth 
Param:  tau1 float  -  0. 		lower limit of estimated tau 
Param:  tau2 float  -  0.2 		upper limit of estimated tau 
Param:  v1 float  -  0. 		lower limit of estimated velocity 
Param:  v2 float  -  10. 		upper limit of estimated velocity 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  waterz int  -  51 		water layer depth 
Param:  woff1 float  -   -  		window data residual: rmin 
LDesc:  (defaults to: acpar->r0)
Param:  woff2 float  -   -  		window data residual: rmax 
LDesc:  (defaults to: acpar->r0+(acpar->nr-1)*acpar->dr)
Param:  wt1 float  -   -  		window data residual: tmin 
LDesc:  (defaults to: acpar->t0)
Param:  wt2 float  -   -  		window data residual: tmax 
LDesc:  (defaults to: acpar->t0+(acpar->nt-1)*acpar->dt)

