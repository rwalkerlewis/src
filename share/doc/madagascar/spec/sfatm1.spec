[sfatm1]
Cat:    RSF/user/yliu
Desc:   1D alpha-trimmed-mean filtering
DocCmd: sfatm1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha float  -   -  		0.0 <= alpha <= 0.5: median filter (alpha=0.5); mean filter (alpha=0.) 
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive and odd integer)

