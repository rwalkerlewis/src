[sfaweop3d]
Cat:    RSF/user/psava
Desc:   3D AWE modeling
DocCmd: sfaweop3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fm data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dabc enum-bool  -  n 		Absorbing BC 
Param:  fsrf enum-bool  -  n 		free surface  
Param:  rec string  -   -  		auxiliary input file name
Param:  sou string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		verbosity  

