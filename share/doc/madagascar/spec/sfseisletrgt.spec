[sfseisletrgt]
Cat:    RSF/user/zgeng
Desc:   Seislet transform using rgt
DocCmd: sfseisletrgt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   rgt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, do adjoint transform 
Param:  eps float  -  0.01 		regularization 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  order int  -  1 		accuracy order 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  unit enum-bool  -  n 		if y, use unitary scaling 
Param:  verb enum-bool  -  n 		verbosity flag 

