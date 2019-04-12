[sfitrack3d]
Cat:    RSF/user/psava
Desc:   Datuming by 3D Green functions in constant media
DocCmd: sfitrack3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwin data)
Port:   stdout rsf w req 	RSF standard output (containing Fwou data)
Port:   cff rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   cnn rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  angMAX float  -  90.0 		
Param:  fast enum-bool  -  y 		fast execution 
Param:  gauANG float  -   -  		
LDesc:  (defaults to: 0.3*angMAX)
Param:  nin enum-bool  -  y 		
Param:  nou enum-bool  -  y 		------------------------------------------------------------
Param:  ox float  -  0.0 		
Param:  oy float  -  0.0 		
Param:  oz float  -  0.0 		
Param:  velo float  -  1.0 		medium velocity 
Param:  verb enum-bool  -  n 		verbosity flag 

