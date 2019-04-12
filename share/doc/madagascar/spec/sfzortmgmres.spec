[sfzortmgmres]
Cat:    RSF/user/jsun
Desc:   2-D FFT-based zero-offset exploding reflector modeling/migration linear operator
DocCmd: sfzortmgmres | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   leftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   leftf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rightf rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dt float  -   -  		time sampling 
Param:  dz float  -   -  		depth sampling 
Param:  gmres enum-bool  -  n 		
Param:  gpz int  -  0 		geophone surface 
Param:  mem int  -  20 		
Param:  niter int  -  10 		
Param:  nt int  -   -  		time samples 
Param:  nz int  -   -  		depth samples 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  timer enum-bool  -  n 		
Param:  verb enum-bool  -  n 		

