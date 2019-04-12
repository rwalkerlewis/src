[sftraveltime2d]
Cat:    RSF/user/roman
Desc:   Oriented zero-offset migration
DocCmd: sftraveltime2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing dist data)
Port:   stdout rsf w req 	RSF standard output (containing imagt data)
Port:   dept rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   len rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   time rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eik string  -   -  		
Param:  front string  -   -  		
Param:  frontdt float  -   -  		
Param:  fronteps float  -   -  		
Param:  frontnt int  -   -  		
Param:  frontt0 float  -   -  		
Param:  interpolate int  -   -  		first arrivals 
Param:  minpath string  -   -  		
Param:  timez0 string  -   -  		
Param:  tolx float  -   -  		
Param:  tolz float  -   -  		
Param:  xsrc float  -   -  		

