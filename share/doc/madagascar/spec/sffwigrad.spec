[sffwigrad]
Cat:    RSF/user/zhiguang
Desc:   2D Gradient Calculation in Full Waveform Inversion
DocCmd: sffwigrad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   misfit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   receiver rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   record rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   source rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  npml int  -  20 		
Param:  omega float  -   -  		
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 

