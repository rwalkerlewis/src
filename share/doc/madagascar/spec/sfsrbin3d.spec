[sfsrbin3d]
Cat:    RSF/user/psava
Desc:   4-D data binning from traces at irregular coordinates
DocCmd: sfsrbin3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Ftrc data)
Port:   stdout rsf w req 	RSF standard output (containing Fbin data)
Port:   key rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 float  -   -  		
Param:  d2 float  -   -  		
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  o1 float  -   -  		
Param:  o2 float  -   -  		
Param:  od1 float  -   -  		
Param:  od2 float  -   -  		
Param:  on1 int  -   -  		
Param:  on2 int  -   -  		
Param:  oo1 float  -   -  		
Param:  oo2 float  -   -  		
Param:  verb enum-bool  -  n 		verbosity flag 

