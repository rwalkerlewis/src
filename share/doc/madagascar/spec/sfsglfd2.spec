[sfsglfd2]
Cat:    RSF/user/fangg
Desc:   2-D Low Rank Finite-difference wave extrapolation
DocCmd: sfsglfd2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing fsource data)
Port:   stdout rsf w req 	RSF standard output (containing fwf data)
Port:   Gx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Gz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sxx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sxz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   szz rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  spx int  -   -  		source point in x 
Param:  spz int  -   -  		source point in z 
Param:  verb enum-bool  -  n 		verbosity

