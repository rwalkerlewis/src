[sfsgelfd2dpml]
Cat:    RSF/user/junyan
Desc:   A k-space staggered-grid lowrank finite-difference for elastic and viscoelastic seismic-wave modeling
DocCmd: sfsgelfd2dpml | cat
Port:   stdin  rsf r req 	RSF standard input (containing vpfp data)
Port:   stdout rsf w req 	RSF standard output (containing snapfpx data)
Port:   Gpx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gpz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gsx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gsz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rho rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snappx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   snappz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   snapsx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   snapsz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   snapz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   sxx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sxz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  fpeak float  -  20.0 		
Param:  freesurface int  -  0 		recerver 
Param:  igz int  -  1 		
Param:  isrcx int  -   -  		
Param:  isrcz int  -   -  		
Param:  npml int  -  30 		
Param:  nt int  -   -  		
Param:  order int  -  12 		source 
Param:  snap int  -  1 		
Param:  verb int  -  1 		freesurface 

