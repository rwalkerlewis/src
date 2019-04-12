[sffkoclet3]
Cat:    RSF/user/yliu
Desc:   2-D seislet transform using frequency-wavenumber offset-azimuth continuation
DocCmd: sffkoclet3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		if y, do adjoint transform 
Param:  amp enum-bool  -  n 		if y, true amplitudes continuation 
Param:  dir string  -   -  		[azimuth,offset,both] direction, the default is both directions  
Param:  dwt enum-bool  -  n 		if y, do wavelet transform 
Param:  eps float  -  0.01 		regularization 
Param:  inv enum-bool  -  n 		if y, do inverse transform 
Param:  maxe float  -  10. 		stability constraint 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  
Param:  verb enum-bool  -  y 		verbosity flag 

