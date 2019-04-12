[sflrtti2de]
Cat:    RSF/user/jsun
Desc:   2-D two-components wavefield modeling using original elastic displacement wave equation in TTI media by lowrank method
DocCmd: sflrtti2de | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   Elasticz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   pleft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   pright rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sleft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sright rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  A float  -  1.0 		wavelet amplitude 
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
Param:  dt float  -  0.001 		absorbing boundary condition
Param:  f0 float  -  30.0 		wavelet peak freq 
Param:  isx int  -   -  		
LDesc:  (defaults to: nx/2)
Param:  isz int  -   -  		
LDesc:  (defaults to: nz/2)
Param:  nbb int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbl int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbr int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbt int  -   -  		
Param:  nt int  -  301 		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  sep enum-bool  -  n 		output separated wavefields 
Param:  src int  -  1 		source mode: 1 - exploding force; 2 - equil-energy force 
Param:  t0 float  -  0.04 		wavelet time lag 

