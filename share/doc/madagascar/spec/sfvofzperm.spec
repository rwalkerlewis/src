[sfvofzperm]
Cat:    RSF/user/fomels
Desc:   V(z) prestack exploditing reflector
DocCmd: sfvofzperm | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   middle rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   size rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dh float  -   -  		offset sampling (if modeling) 
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		time sampling (if migration) 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nh int  -   -  		offset samples (if modeling) 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		time samples (if migration) 

