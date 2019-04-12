[sftahwindow]
Cat:    RSF/user/karl
Desc:   Trace And Header WINDOW
DocCmd: sftahwindow | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  key string  -   -  		
Param:  max int  -   -  		
LDesc:  (defaults to: INT_MAX)
Param:  min int  -   -  		
LDesc:  (defaults to: INT_MIN)
Param:  reject int-list  -   -  		 [numreject]
Param:  tmax float  -   -  		maximum time in seconds to limit the output trace 
LDesc:  (defaults to: (n1_traces-1)*d1+o1)
Param:  verbose int  -  0 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

