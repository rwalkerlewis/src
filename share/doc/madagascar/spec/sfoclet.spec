[sfoclet]
Cat:    RSF/user/yliu
Desc:   Seislet transform in log-stretched frequency-offset-midpoint domain
DocCmd: sfoclet | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		if y, do adjoint transform 
Param:  inv enum-bool  -  y 		if y, do inverse transform 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  unit enum-bool  -  n 		if y, use unitary scaling 
Param:  verb enum-bool  -  n 		verbosity flag 

