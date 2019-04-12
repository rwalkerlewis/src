[sfdomf]
Cat:    RSF/user/yliu
Desc:   2D dip-oriented median/mean filter (DOMF)
DocCmd: sfdomf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  boundary enum-bool  -  y 		if y, boundary is data, whereas zero
Param:  nw int  -   -  		data-window length (positive and odd integer) 
Param:  stack enum-bool  -  n 		if y, mean filter, whereas median filter
Param:  verb enum-bool  -  n 		verbosity flag 

