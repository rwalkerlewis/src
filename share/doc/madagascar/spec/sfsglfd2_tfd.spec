[sfsglfd2_tfd]
Cat:    RSF/user/fangg
Desc:   2-D 4th-order Staggered Grid Finite-difference wave extrapolation
DocCmd: sfsglfd2_tfd | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsource data)
Port:   stdout rsf w req 	RSF standard output (containing fwf data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  oo int  -  4 		
Param:  spx int  -   -  		source point in x 
Param:  spz int  -   -  		source point in z 
Param:  verb enum-bool  -  n 		verbosity

