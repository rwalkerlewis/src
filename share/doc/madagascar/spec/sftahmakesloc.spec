[sftahmakesloc]
Cat:    RSF/user/karl
Desc:   Trace And Header MAKE SLOC KEY
DocCmd: sftahmakesloc | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  slockey string  -   -  		The name of the sloc key created by the program. 
Param:  slocxy string  -   -  		
LDesc:  
LDesc:       two keys that are the trace headers names of the x,y coordinate 
LDesc:       to use to identify surface locations and compute the trace header
LDesc:       value for slockey 
LDesc:   
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    

