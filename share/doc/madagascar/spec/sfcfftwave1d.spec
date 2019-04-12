[sfcfftwave1d]
Cat:    RSF/user/jsun
Desc:   1-D complex lowrank FFT wave extrapolation using complex to complex fft using initial condition
DocCmd: sfcfftwave1d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   prop rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cft enum-bool  -  y 		
Param:  cmplx enum-bool  -  n 		
Param:  cos enum-bool  -  y 		
Param:  dt float  -   -  		
Param:  nt int  -   -  		
Param:  os enum-bool  -  y 		
Param:  right string  -   -  		auxiliary input file name
Param:  sub enum-bool  -  n 		if -1 is included in the matrix 

