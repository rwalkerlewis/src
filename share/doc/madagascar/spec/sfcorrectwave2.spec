[sfcorrectwave2]
Cat:    RSF/user/jsun
Desc:   Complex 2-D wave propagation using initial condition
DocCmd: sfcorrectwave2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fi data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   alpha rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   beta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  correct enum-bool  -  n 		jingwei's correction
Param:  dt float  -   -  		
Param:  mode string  -   -  		default mode is pspi 
Param:  nt int  -   -  		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  verb enum-bool  -  y 		verbosity 

