[sflogwarp]
Cat:    RSF/system/generic
Desc:   Log warping
DocCmd: sflogwarp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: n1)
Param:  t0 float  -   -  		
LDesc:  (defaults to: o1)

