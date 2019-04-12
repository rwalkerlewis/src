[sfepfws]
Cat:    RSF/user/chen
Desc:   Edge preserving (smoothing) filter by window selection
DocCmd: sfepfws | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  filter string  -   -  		filter: mean,median,poly,fir 
Param:  nfw int  -  5 		window size 
Param:  order int  -   -  		filter order (<= nfw, only for polynomial and fir filters) 
LDesc:  (defaults to: nfw-1)

