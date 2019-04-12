[sftahspecbal]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input, SPECtral BALance
DocCmd: sftahspecbal | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  finc float  -  5 		frequency band increment 
Param:  fmax float  -  95 		maximum frequency band 
Param:  fmin float  -  5 		minimum frequency band 
Param:  ntaper int  -  12 		
Param:  pnoise float  -  0.01 		relative additive noise level 
Param:  tstart float-list  -   -  		 [numtstart]
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      
Param:  wagc float  -  -1 		
LDesc:  
LDesc:         length of the agc window in seconds
LDesc:      
Param:  xstart float-list  -   -  		 [numxstart]

