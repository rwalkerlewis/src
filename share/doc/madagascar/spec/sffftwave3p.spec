[sffftwave3p]
Cat:    RSF/user/jsun
Desc:   Simple 3-D wave propagation with multi-threaded fftw3
DocCmd: sffftwave3p | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  verb enum-bool  -  y 		verbosity 

