[sfovc]
Cat:    RSF/system/seismic
Desc:   Oriented velocity continuation
DocCmd: sfovc | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.1 		stretch regularization 
Param:  lagrange enum-bool  -  n 		Use Lagrangian method 
Param:  nv int  -  1 		number of velocity steps 
Param:  v0 float  -  0. 		starting velocity 
Param:  vmax float  -   -  		end velocity 

