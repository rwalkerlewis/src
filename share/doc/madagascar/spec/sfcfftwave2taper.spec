[sfcfftwave2taper]
Cat:    RSF/user/jsun
Desc:   Complex 2-D wave propagation (with multi-threaded FFTW3)
DocCmd: sfcfftwave2taper | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cmplx enum-bool  -  y 		outputs complex wavefield 
Param:  os enum-bool  -  y 		one-step flag 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  sub enum-bool  -  y 		subtraction flag 
Param:  taper int  -  0 		tapering in the frequency domain 
Param:  thresh float  -  0.92 		tapering threshold 
Param:  verb enum-bool  -  n 		verbosity 

