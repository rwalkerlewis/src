[sfpp2pstsic]
Cat:    RSF/system/seismic
Desc:   Compute angle gathers for time-shift imaging condition
DocCmd: sfpp2pstsic | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fstk data)
Port:   stdout rsf w req 	RSF standard output (containing Fang data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vpvs rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  a0 float  -  0. 		
Param:  da float  -   -  		
LDesc:  (defaults to: 1./(nv-1))
Param:  extend int  -  4 		tmp extension 
Param:  na int  -   -  		
LDesc:  (defaults to: nv)

