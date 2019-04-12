[sfafd2domp]
Cat:    RSF/user/chenyk
Desc:   2D coustic time-domain FD modeling with different boundary conditions using OpenMP
DocCmd: sfafd2domp | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  free enum-bool  -  n 		
Param:  ifoneway enum-bool  -  y 		
Param:  ifsponge enum-bool  -  y 		
Param:  nb int  -  5 		setup I/O files 
Param:  verb enum-bool  -   -  		
LDesc:  (defaults to: 0)

