[sffreqint]
Cat:    RSF/system/seismic
Desc:   1-D data regularization using freqlet transform
DocCmd: sffreqint | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coord rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   freq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 float  -   -  		output sampling 
Param:  eps float  -  1.0 		regularization parameter 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  n1 int  -   -  		output samples 
Param:  ncycle int  -  1 		number of IRLS iterations 
Param:  niter int  -  10 		number of iterations for inversion 
Param:  o1 float  -   -  		output origin 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  

