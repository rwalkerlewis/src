[sffermatrecursion]
Cat:    RSF/user/zone
Desc:   2D traveltime derivatives computation with the recursion from Fermat's principle (Sripanich and Fomel, 2017)
DocCmd: sffermatrecursion | cat
Port:   stdin  rsf r req 	RSF standard input (containing refl data)
Port:   stdout rsf w req 	RSF standard output (containing vnmohet data)
Port:   curv rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slow rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   t0sum rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vnmosq rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dipcurv enum-bool  -  n 		if get dip/curvature from separate files 
Param:  order int  -  3 		Interpolation order

