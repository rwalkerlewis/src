[sftahmute]
Cat:    RSF/user/karl
Desc:   Read Trace And Header (tah) from standard input, MUTE
DocCmd: sftahmute | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ntaper int  -  12 		
LDesc:  
LDesc:         number of samples in the taper of the mute.
LDesc:      
Param:  tmute float-list  -   -  		
LDesc:  
LDesc:  	   List of floats the same length as list of floats in the xmute
LDesc:  	   parameter.  The (xmute,tmute) pairs are interpolated using the
LDesc:  	   trace headers offset to determine trace start time. The mute is
LDesc:  	   NOT moved based on the first live sample.
LDesc:  	   
LDesc:    [numtmute]
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      
Param:  xmute float-list  -   -  		
LDesc:  
LDesc:  	   List of floats the same length as list of floats in the tmute
LDesc:  	   parameter.  The (xmute,tmute) pairs are interpolated using the
LDesc:  	   trace headers offset to determine trace start time.  The mute is
LDesc:  	   NOT moved based on the first live sample.
LDesc:  	   
LDesc:    [numxmute]

