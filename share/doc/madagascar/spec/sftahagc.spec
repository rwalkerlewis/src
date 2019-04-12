[sftahagc]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input, MUTE
DocCmd: sftahagc | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ntaper int  -  12 		
Param:  tstart float-list  -   -  		 [numtstart]
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      
Param:  wagc float  -   -  		
Param:  xstart float-list  -   -  		 [numxstart]

