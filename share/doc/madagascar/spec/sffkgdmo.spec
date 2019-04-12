[sffkgdmo]
Cat:    RSF/system/seismic
Desc:   FK-domain Gardner's DMO for regularly sampled 2-D data
DocCmd: sffkgdmo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  db float  -  1 		angle increment 
Param:  eps float  -  0.01 		stretch regularization 
Param:  inv enum-bool  -  y 		inversion flag 
Param:  nb int  -  85 		number of angles 
Param:  shot enum-bool  -  n 		if shot gathers instead of midpoint gathers 
Param:  xi float  -  1 		continuation paremeter 

