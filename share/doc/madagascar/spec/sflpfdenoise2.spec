[sflpfdenoise2]
Cat:    RSF/user/yliu
Desc:   2D denoising using edge-preserving local polynomial fitting (ELPF)
DocCmd: sflpfdenoise2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  boundary enum-bool  -  y 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive and odd integer) 
Param:  niter int  -  100 		number of iterations 
Param:  nw int  -   -  		data-window length (positive and odd integer) 
Param:  rect int  -   -  		local smoothing radius 
Param:  verb enum-bool  -  n 		verbosity flag 

