[sflum2]
Cat:    RSF/user/yliu
Desc:   2D LUM filter
DocCmd: sflum2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw1 int  -   -  		filter-window length in n1 direction (positive and odd integer)
Param:  nfw2 int  -   -  		filter-window length in n2 direction (default=nfw1)
LDesc:  (defaults to: nfw1)
Param:  shnclip int  -   -  		sharpener tuning parameter (1 <= shnclip <= (nfw1*nfw2+1)/2, the default is (nfw1*nfw2+1)/2)
LDesc:  (defaults to: (nfw1*nfw2+1)/2)
Param:  smnclip int  -   -  		smoother tuning parameter (1 <= smnclip <= (nfw1*nfw2+1)/2, the default is (nfw1*nfw2+1)/2)
LDesc:  (defaults to: (nfw1*nfw2+1)/2)
Param:  type string  -   -  		[rectangular,cross] 2-D window type, the default is rectangular  
Param:  verb enum-bool  -  n 		verbosity flag 

