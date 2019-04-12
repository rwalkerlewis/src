[sfcfftwave1]
Cat:    RSF/user/fomels
Desc:   1-D complex lowrank FFT wave extrapolation
DocCmd: sfcfftwave1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   prop rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  nt int  -   -  		
Param:  right string  -   -  		auxiliary input file name

