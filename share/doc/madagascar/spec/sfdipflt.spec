[sfdipflt]
Cat:    RSF/user/chen
Desc:   2D dip filter
DocCmd: sfdipflt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  filt string  -   -  		filter type: [median],mean 
Param:  interp string  -   -  		interpolation method: [nearest],linear 
Param:  nf int  -  1 		filter length 

