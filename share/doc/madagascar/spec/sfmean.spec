[sfmean]
Cat:    RSF/user/yliu
Desc:   1-D sliding-window mean filtering
DocCmd: sfmean | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw int  -   -  		filter-window length (positive integer)

