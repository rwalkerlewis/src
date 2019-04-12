[sfffd2_den_omp]
Cat:    RSF/user/songxl
Desc:   2-D Fourier finite-difference wave extrapolation
DocCmd: sfffd2_den_omp | cat
Port:   stdin  rsf r req 	RSF standard input (containing source data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ax float  -  2.0 		suppress HF parameter
Param:  az float  -  2.0 		suppress HF parameter
Param:  cb float  -  0.01 		decaying parameter
Param:  cl float  -  0.01 		decaying parameter
Param:  cr float  -  0.01 		decaying parameter
Param:  ct float  -  0.01 		decaying parameter
Param:  dt float  -   -  		
Param:  factor float  -  2.0/3.0 		suppress HF parameter
Param:  irz int  -   -  		
LDesc:  (defaults to: isz)
Param:  isx int  -   -  		
Param:  isz int  -   -  		
Param:  jm int  -  20 		
Param:  nbb int  -  0 		
Param:  nbl int  -  0 		
Param:  nbr int  -  0 		
Param:  nbt int  -  0 		
Param:  nt int  -   -  		
Param:  sht int  -  0 		
Param:  snap enum-bool  -  y 		Output snapshots

