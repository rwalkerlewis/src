[sffftwave2omp]
Cat:    RSF/user/jsun
Desc:   Simple 2-D wave propagation with multi-threaded Kiss-FFT
DocCmd: sffftwave2omp | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  abc enum-bool  -  n 		absorbing flag 
Param:  cb float  -   -  		
LDesc:  (defaults to: ct)
Param:  cl float  -   -  		
LDesc:  (defaults to: ct)
Param:  cr float  -   -  		
LDesc:  (defaults to: ct)
Param:  ct float  -   -  		
Param:  nbb int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbl int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbr int  -   -  		
LDesc:  (defaults to: nbt)
Param:  nbt int  -   -  		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  verb enum-bool  -  n 		verbosity 

