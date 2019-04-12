[sfboxfilter]
Cat:    RSF/user/psava
Desc:   3D convolution with arbitrary filter
DocCmd: sfboxfilter | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fx data)
Port:   stdout rsf w req 	RSF standard output (containing Fy data)
Port:   flt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  stat enum-bool  -  y 		stationary flag 
Param:  verb enum-bool  -  n 		verbosity flag 

