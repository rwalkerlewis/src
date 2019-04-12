[sfseislet1]
Cat:    RSF/user/fomels
Desc:   1-D seislet transform
DocCmd: sfseislet1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, do adjoint transform 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  unit enum-bool  -  n 		if y, use unitary scaling 
Param:  verb enum-bool  -  n 		verbosity flag 

