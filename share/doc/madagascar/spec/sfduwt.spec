[sfduwt]
Cat:    RSF/user/yliu
Desc:   1-D digital undecimated (stationary) wavelet transform by lifting scheme
DocCmd: sfduwt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		if y, do adjoint transform 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  scale int  -  max 		decomposition scale 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  unit enum-bool  -  n 		if y, use unitary scaling 

