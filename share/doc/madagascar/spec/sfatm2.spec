[sfatm2]
Cat:    RSF/user/yliu
Desc:   2D alpha-trimmed-mean filtering
DocCmd: sfatm2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha float  -   -  		0.0 <= alpha <= 0.5: median filter (alpha=0.5); mean filter (alpha=0.)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw1 int  -   -  		filter-window length in n1 direction (positive and odd integer)
Param:  nfw2 int  -   -  		filter-window length in n2 direction (default=nfw1)
LDesc:  (defaults to: nfw1)
Param:  type string  -   -  		[rectangular,cross] 2-D window type, the default is rectangular  
Param:  verb enum-bool  -  n 		verbosity flag 

