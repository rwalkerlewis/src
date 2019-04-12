[sflpfdenoise1]
Cat:    RSF/user/yliu
Desc:   1D denoising using edge-preserving local polynomial fitting (ELPF)
DocCmd: sflpfdenoise1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive and odd integer) 
Param:  niter int  -  100 		number of iterations 
Param:  rect int  -   -  		local smoothing radius 
Param:  verb enum-bool  -  n 		verbosity flag 

