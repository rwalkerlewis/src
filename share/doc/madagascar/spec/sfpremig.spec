[sfpremig]
Cat:    RSF/user/jsun
Desc:   Pseudo-spectral pre-stack source-receiver source independent diffraction imaging
DocCmd: sfpremig | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   dat_2 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  A float-list  -   -  		wavelet amplitude  [n_srcs]
Param:  abc enum-bool  -  n 		absorbing flag 
Param:  adj enum-bool  -  n 		use pseudo-spectral 
Param:  born enum-bool  -  n 		born modeling flag 
Param:  cb float  -   -  		
LDesc:  (defaults to: ct)
Param:  cl float  -   -  		
LDesc:  (defaults to: ct)
Param:  cmplx enum-bool  -  y 		use complex fft 
Param:  cr float  -   -  		
LDesc:  (defaults to: ct)
Param:  ct float  -   -  		
Param:  dat_v string  -   -  		auxiliary input file name
Param:  diff enum-bool  -  n 		diffraction imaging flag 
Param:  dt float  -   -  		
Param:  f0 float-list  -   -  		wavelet peak freq  [n_srcs]
Param:  gpl int  -  -1 		geophone length 
Param:  gpl_v int  -  -1 		geophone height 
Param:  gpx int  -  -1 		geophone position x 
Param:  gpx_v int  -  -1 		geophone position x 
Param:  gpz int  -  -1 		geophone position z 
Param:  gpz_v int  -  -1 		geophone position z 
Param:  justrec enum-bool  -  n 		just need full waveform record (no born or rtdm) 
Param:  n_srcs int  -  1 		source type 
Param:  nbb int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbl int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbr int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbt int  -   -  		
Param:  nt int  -   -  		
Param:  offset int  -  0 		nearest offset 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  ps enum-bool  -  n 		use pseudo-spectral 
Param:  roll enum-bool  -  n 		if n, receiver is independent of source location and gpl=nx
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtint int  -   -  		
Param:  snap int  -  0 		interval for snapshots 
Param:  split int  -  1 		receiver split 
Param:  spx int-list  -   -  		shot position x  [n_srcs]
Param:  spz int-list  -   -  		shot position z  [n_srcs]
Param:  src int  -  0 		source type 
Param:  t0 float-list  -   -  		wavelet time lag  [n_srcs]
Param:  verb enum-bool  -  n 		verbosity 
Param:  vref float  -  1500 		reference velocity (default using water) 
Param:  which int  -  0 		

