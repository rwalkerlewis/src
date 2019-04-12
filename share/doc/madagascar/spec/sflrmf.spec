[sflrmf]
Cat:    RSF/user/yliu
Desc:   Local radial median filtering
DocCmd: sflrmf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter window of median filter 
Param:  tmax float  -   -  		zero-offset time for mimumum velocity 
Param:  tmin float  -   -  		zero-offset time for maximum velocity 
Param:  vmax float  -   -  		maximum velocity 
Param:  vmin float  -   -  		minimum velocity 

