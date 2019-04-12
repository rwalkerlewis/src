[sflrwave2]
Cat:    RSF/user/jsun
Desc:   2-D FFT-based (point src) wave propagation and its adjoint
DocCmd: sflrwave2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   src rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if n, modeling; if y, migration 
Param:  dt float  -   -  		time sampling 
Param:  nt int  -   -  		time samples 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  timer enum-bool  -  n 		
Param:  verb enum-bool  -  n 		

