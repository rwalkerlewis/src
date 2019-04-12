[sftraveltimelen]
Cat:    RSF/user/roman
Desc:   Oriented zero-offset migration
DocCmd: sftraveltimelen | cat
Port:   stdin  rsf r req 	RSF standard input (containing dist data)
Port:   stdout rsf w req 	RSF standard output (containing imagt data)
Port:   dept rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   len rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   time rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  interpolate int  -   -  		
Param:  timez0 string  -   -  		
Param:  tolx float  -   -  		
Param:  tolz float  -   -  		
Param:  xsrc float  -   -  		

