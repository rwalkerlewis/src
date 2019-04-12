[sfawefd3dgpu]
Cat:    RSF/user/hwang
Desc:   3D acoustic wave equation finite difference time domain modeling
DocCmd: sfawefd3dgpu | cat
Port:   stdin  rsf r req 	RSF standard input (containing file_wav data)
Port:   stdout rsf w req 	RSF standard output (containing file_dat data)
Port:   den rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  cden enum-bool  -  y 		
Param:  jsnap int  -  1 		
Param:  nbd int  -  20 		
Param:  snap enum-bool  -  n 		
Param:  verb enum-bool  -  n 		

