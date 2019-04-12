[sfdsr2]
Cat:    RSF/system/seismic
Desc:   2-D prestack modeling/migration with split-step DSR
DocCmd: sfdsr2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   slowness rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.004 		time error 
Param:  dw float  -   -  		Frequency sampling (for modeling) 
Param:  eps float  -  0.01 		stability parameter 
Param:  inv enum-bool  -  n 		If y, modeling; if n, migration 
Param:  npad int  -  0 		padding on offset wavenumber 
Param:  nr int  -  1 		maximum number of references 
Param:  nt int  -  1 		taper size 
Param:  nw int  -   -  		Length of frequency axis (for modeling) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w0 float  -  0. 		Frequency origin (for modeling) 

