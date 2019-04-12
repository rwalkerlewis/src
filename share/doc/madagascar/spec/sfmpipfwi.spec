[sfmpipfwi]
Cat:    RSF/user/jsun
Desc:   Visco-acoustic Forward Modeling, FWI, and RTM based on SLS model
DocCmd: sfmpipfwi | cat
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fmwt rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fsrc rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  acqui_type int  -  1 		if 1, fixed acquisition; if 2, marine acquisition; if 3, symmetric acquisition 
Param:  c1 float  -  1e-4 		
Param:  c2 float  -  0.9 		
Param:  coef float  -  0.003 		absorbing boundary coefficient 
Param:  conv_error float  -   -  		final convergence error 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: acpar->dx)
Param:  ds float  -   -  		shot interval 
Param:  f0 float  -   -  		reference frequency 
Param:  fhi float  -   -  		
LDesc:  (defaults to: 0.5/acpar->dt)
Param:  flo float  -  0. 		
Param:  function int  -  2 		if 1, forward modeling; if 2, FWI; if 3, RTM 
Param:  grectx int  -  3 		gradient smoothing radius in x 
Param:  grectz int  -  3 		gradient smoothing radius in z 
Param:  interval int  -  1 		wavefield storing interval 
Param:  media int  -  1 		if 1, acoustic media; if 2, visco-acoustic media 
Param:  nb int  -  100 		boundary width 
Param:  niter int  -   -  		iteration number 
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: acpar->nx)
Param:  ns int  -   -  		shot number 
Param:  onlygrad enum-bool  -  n 		only want gradident 
Param:  oreo enum-bool  -  n 		keep oreo or keep cream 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: acpar->x0)
Param:  repeat int  -  1 		repeat resetting alpha 
Param:  rz int  -  1 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  sz int  -  5 		source depth 
Param:  v1 float  -  0. 		
Param:  v2 float  -  10. 		
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  waterz int  -  0 		water layer depth 
Param:  waterzb int  -  0 		water layer depth from bottom up 
Param:  woff1 float  -   -  		
LDesc:  (defaults to: acpar->r0)
Param:  woff2 float  -   -  		
LDesc:  (defaults to: acpar->r0+(acpar->nr-1)*acpar->dr)
Param:  wt1 float  -   -  		
LDesc:  (defaults to: acpar->t0)
Param:  wt2 float  -   -  		
LDesc:  (defaults to: acpar->t0+(acpar->nt-1)*acpar->dt)

