[sfmpisfwi]
Cat:    RSF/user/zhiguang
Desc:   Acoustic Forward Modeling, FWI, and RTM (FWI has the options of seislet regularization, smoothing kernels, simultaneous source, and static phase encoding)
DocCmd: sfmpisfwi | cat
Port:   Fcode rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fdip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Ferr rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fmod rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  acqui_type int  -  1 		if 1, fixed acquisition; if 2, marine acquisition; if 3, symmetric acquisition 
Param:  coef float  -  0.002 		absorbing boundary coefficient 
Param:  conv_error float  -   -  		final convergence error 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: acpar->dx)
Param:  drectx int  -  1 		smoothing kernel radius in x 
Param:  drectz int  -  1 		smoothing kernel radius in z 
Param:  ds float  -   -  		shot interval 
Param:  dsource int  -  0 		interval of sources in a supershot 
Param:  encode int  -  0 		if 0, no phase encoding; if 1, phase encoding 
Param:  eps float  -  0.1 		seislet regularization parameter 
Param:  err_type int  -  0 		if 0, true misfit function; if 1, both smoothing kernel and original L2 norm misfits 
Param:  factor float  -  10 		step length increase factor 
Param:  fhi float  -   -  		high frequency in band, default is Nyquist 
LDesc:  (defaults to: 0.5/acpar->dt)
Param:  flo float  -  0. 		low frequency in band, default is zero 
Param:  frectx int  -  2 		source smoothing in x 
Param:  frectz int  -  2 		source smoothing in z 
Param:  function int  -  2 		if 1, forward modeling; if 2, FWI; if 3, RTM 
Param:  gain float  -  1 		vertical gain power of data residual 
Param:  grectx int  -  3 		gradient smoothing radius in x 
Param:  grectz int  -  3 		gradient smoothing radius in z 
Param:  interval int  -  1 		wavefield storing interval 
Param:  nb int  -  100 		boundary width 
Param:  niter int  -   -  		iteration number 
Param:  nls int  -  20 		line search number 
Param:  npair int  -  20 		number of l-BFGS pairs 
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: acpar->nx)
Param:  nrepeat int  -  1 		smoothing kernel repeat number 
Param:  ns int  -   -  		shot number 
Param:  nsource int  -  1 		number of sources in a supershot 
Param:  onlygrad enum-bool  -  n 		only calculate gradident or not 
Param:  order int  -  1 		accuracy order of seislet transform 
Param:  pclip float  -  15 		soft thresholding parameter 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: acpar->x0)
Param:  repeat int  -  5 		after how many iterations the step length goes back to 1 
Param:  rz int  -  5 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  seislet int  -  0 		if 0, no seislet regularization; if 1, seislet regularization 
Param:  seislet_type string  -   -  		[haar, linear, biorthogonal] 
Param:  sigma1 float  -  -1 		smoothing kernel radius moving step in z 
Param:  sigma2 float  -  -1 		smoothing kernel radius moving step in x 
Param:  sz int  -  5 		source depth 
Param:  tangent int  -  0 		if 1, calculate prediction corrector 
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

