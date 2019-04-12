[sfmpiewertm]
Cat:    RSF/user/jsun
Desc:   2-D two-components elastic wavefield modeling operators with lowrank approximation
DocCmd: sfmpiewertm | cat
Port:   Recordx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   input rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   output rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   pleft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   pright rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sleft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sright rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  A float  -  1.0 		wavelet amplitude 
Param:  ImagePP string  -   -  		auxiliary output file name
Param:  ImagePS string  -   -  		auxiliary output file name
Param:  ImageSP string  -   -  		auxiliary output file name
Param:  ImageSS string  -   -  		auxiliary output file name
Param:  Pwavex string  -   -  		auxiliary output file name
Param:  Pwavez string  -   -  		auxiliary output file name
Param:  Swavex string  -   -  		auxiliary output file name
Param:  Swavez string  -   -  		auxiliary output file name
Param:  abc enum-bool  -  n 		absorbing flag 
Param:  cb float  -   -  		
LDesc:  (defaults to: ct)
Param:  cl float  -   -  		
LDesc:  (defaults to: ct)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  cr float  -   -  		
LDesc:  (defaults to: ct)
Param:  ct float  -   -  		
Param:  dt float  -  0.001 		
Param:  f0 float  -  30.0 		wavelet peak freq 
Param:  gpz int  -   -  		geophone depth 
LDesc:  (defaults to: nbt+5)
Param:  isx int  -   -  		
LDesc:  (defaults to: nx/2)
Param:  isz int  -   -  		
Param:  mig enum-bool  -  n 		migration flag 
Param:  mute enum-bool  -  n 		muting first arrival 
Param:  nbb int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbl int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbr int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbt int  -   -  		
Param:  nt int  -  301 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  shtbgn int  -   -  		
Param:  shtend int  -   -  		
Param:  shtint int  -   -  		
Param:  snpint int  -  10 		absorbing boundary condition
Param:  src int  -  1 		source mode: 1 - exploding force; 2 - equil-energy force 
Param:  t0 float  -  0.04 		wavelet time lag 
Param:  verb enum-bool  -  n 		padding factor on the first axis 
Param:  vref float  -  1500 		water velocity 
Param:  wd int  -  5 		muting width 

