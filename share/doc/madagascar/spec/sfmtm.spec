[sfmtm]
Cat:    RSF/user/yliu
Desc:   1-D and 2-D modified-trimmed-mean (MTM) filtering
DocCmd: sfmtm | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw1 int  -   -  		filter-window length in n1 direction (positive and odd integer)
Param:  nfw2 int  -  1 		filter-window length in n2 direction (default=1, 1D case)
Param:  pclip float  -   -  		0.0 <= pclip <= 100.0: median filter (pclip=0.); mean filter (pclip=100.) 
Param:  type string  -   -  		[rectangular,cross] 2-D window type, the default is rectangular  
Param:  verb enum-bool  -  n 		verbosity flag 

