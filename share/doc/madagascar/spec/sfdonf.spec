[sfdonf]
Cat:    RSF/user/yliu
Desc:   2D dip-oriented nonlocal (bilateral) smoothing
DocCmd: sfdonf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  ax float  -   -  		Gaussian weight for the range distance 
Param:  boundary enum-bool  -  y 		if y, boundary is data, whereas zero
Param:  bx float  -   -  		exponential weight for the domain distance (different if gaussian)
Param:  gauss enum-bool  -  n 		if y, Gaussian weight, whereas Triangle weight 
Param:  nfw int  -   -  		filter-window length (positive and odd integer) 
Param:  nw int  -   -  		data-window length (positive and odd integer) 
Param:  repeat int  -  1 		repeat filtering several times 
Param:  verb enum-bool  -  n 		verbosity flag 

