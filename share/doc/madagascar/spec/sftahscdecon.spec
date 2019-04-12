[sftahscdecon]
Cat:    RSF/user/karl
Desc:   Trace And Header Surface Consistant Decon
DocCmd: sftahscdecon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  key string  -   -  		
LDesc:  
LDesc:       list of keys to watch to determine traces in a gather that 
LDesc:       will have a single decon operator applies.  Typically data
LDesc:       is sorted by gx,gy then sftahscdecon run with key='gx,gy'.
LDesc:       Then a second pass of scdecon is first sorting by sx,sy and 
LDesc:       running sftahscdecon with key='sx,sy'.
LDesc:     ([numkeys])
Param:  maxlag float  -   -  		last lag of prediction filter (sec) 
Param:  minlag float  -   -  		first lag of prediction filter (sec) 
Param:  pnoise float  -  0.001 		relative additive noise level 
Param:  verbose int  -  1 		
LDesc:  
LDesc:       flag to control amount of print
LDesc:       0 terse, 1 informative, 2 chatty, 3 debug
LDesc:    
Param:  wiener string  -   -  		file to output Wiener filter.  never tested!!! (auxiliary output file name)

