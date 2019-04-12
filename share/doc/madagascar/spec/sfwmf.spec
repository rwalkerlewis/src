[sfwmf]
Cat:    RSF/user/yliu
Desc:   1D weighted median filtering
DocCmd: sfwmf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive and odd integer)
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weights string  -   -  		auxiliary input file name

