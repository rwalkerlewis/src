[sfcfftwave2nsps]
Cat:    RSF/user/jsun
Desc:   Complex 2-D wave propagation (NSPS)
DocCmd: sfcfftwave2nsps | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cmplx enum-bool  -  y 		outputs complex wavefield 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  verb enum-bool  -  n 		verbosity 

