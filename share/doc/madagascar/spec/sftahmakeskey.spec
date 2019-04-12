[sftahmakeskey]
Cat:    RSF/user/karl
Desc:   Trace And Header MAKE Secondary KEY
DocCmd: sftahmakeskey | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  pkey string  -   -  		
LDesc:  
LDesc:       A comma seperated list of primary header keys to monitor to determine 
LDesc:       gathers.  The trace number in the gather is counted and put in the
LDesc:       skey header location.
LDesc:       
LDesc:  
LDesc:    ([numkeys])
Param:  skey string  -   -  		The name of the secondary key created by the program. 
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

