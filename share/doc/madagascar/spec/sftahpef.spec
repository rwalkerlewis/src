[sftahpef]
Cat:    RSF/user/karl
Desc:   Trace And Header Prediction Error Filtering
DocCmd: sftahpef | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  maxcorr float  -   -  		end of autocorrelation window in sec 
Param:  maxlag float  -   -  		last lag of prediction filter (sec) 
Param:  mincorr float  -   -  		start of autocorrelation window in sec 
Param:  minlag float  -   -  		first lag of prediction filter (sec) 
Param:  mix float-list  -   -  		weights for moving average of the autocorrelations  [nmix]
Param:  nmix int  -  1 		number of weights (floats) for moving averages 
Param:  pnoise float  -  0.001 		relative additive noise level 
Param:  verbose int  -  1 		
LDesc:  
LDesc:         flag to control amount of print
LDesc:         0 terse, 1 informative, 2 chatty, 3 debug
LDesc:      
Param:  wiener string  -   -  		file to output Wiener filter (auxiliary output file name)

