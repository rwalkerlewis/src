[sfsclet]
Cat:    RSF/user/yliu
Desc:   2-D SC-seislet: Seislet transform with differential shot continuation
DocCmd: sfsclet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		if y, do adjoint transform 
Param:  eps float  -  0.1 		regularization parameter 
Param:  inv enum-bool  -  y 		if y, do inverse transform 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  unit enum-bool  -  n 		if y, use unitary scaling 
Param:  verb enum-bool  -  n 		verbosity flag 

