[sfconstpermh]
Cat:    RSF/user/fomels
Desc:   Constant-velocity prestack exploding reflector in offset
DocCmd: sfconstpermh | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Param:  dh float  -   -  		offset sampling (if modeling) 
Param:  dt float  -   -  		time sampling (if modeling) 
Param:  dz float  -   -  		depth sampling (if migration) 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nh int  -   -  		offset samples (if modeling) 
Param:  nt int  -   -  		time samples (if modeling) 
Param:  nz int  -   -  		depth samples (if migration) 
Param:  snap int  -  0 		interval for snapshots 
Param:  v float  -   -  		velocity 

