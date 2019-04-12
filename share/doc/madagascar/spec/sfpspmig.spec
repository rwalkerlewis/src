[sfpspmig]
Cat:    RSF/user/jsun
Desc:   Pseudo-spectral migration/de-migration adjoint operators using second-order two-way wave equation
DocCmd: sfpspmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  A float-list  -   -  		wavelet amplitude  [n_srcs]
Param:  abc enum-bool  -  n 		absorbing flag 
Param:  adj enum-bool  -  n 		use pseudo-spectral 
Param:  born enum-bool  -  n 		absorbing flag 
Param:  cb float  -   -  		
LDesc:  (defaults to: ct)
Param:  cl float  -   -  		
LDesc:  (defaults to: ct)
Param:  cmplx enum-bool  -  y 		use complex fft 
Param:  cr float  -   -  		
LDesc:  (defaults to: ct)
Param:  ct float  -   -  		
Param:  dat_v string  -   -  		auxiliary input file name
Param:  dt float  -   -  		
Param:  f0 float-list  -   -  		wavelet peak freq  [n_srcs]
Param:  gpl int  -  -1 		geophone length 
Param:  gpl_v int  -  -1 		geophone height 
Param:  gpx int  -  -1 		geophone position x 
Param:  gpx_v int  -  -1 		geophone position x 
Param:  gpz int  -  -1 		geophone position z 
Param:  gpz_v int  -  -1 		geophone position z 
Param:  n_srcs int  -  1 		source type 
Param:  nbb int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbl int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbr int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbt int  -   -  		
Param:  nt int  -   -  		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  ps enum-bool  -  n 		use pseudo-spectral 
Param:  snap int  -  0 		interval for snapshots 
Param:  spx int-list  -   -  		shot position x  [n_srcs]
Param:  spz int-list  -   -  		shot position z  [n_srcs]
Param:  src int  -  0 		source type 
Param:  t0 float-list  -   -  		wavelet time lag  [n_srcs]
Param:  verb enum-bool  -  n 		verbosity 
Param:  vref float  -  1500 		reference velocity (default using water) 

