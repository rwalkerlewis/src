[sfinjop3d]
Cat:    RSF/user/psava
Desc:   inject/extract in/from 3D wavefield
DocCmd: sfinjop3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fwfl data)
Port:   stdout rsf w req 	RSF standard output (containing Ftrc data)
Port:   coo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  dx float  -  1.0 		
Param:  dy float  -  1.0 		
Param:  dz float  -  1.0 		
Param:  nx int  -  1 		
Param:  ny int  -  1 		
Param:  nz int  -  1 		
Param:  ox float  -  0.0 		
Param:  oy float  -  0.0 		
Param:  oz float  -  0.0 		
Param:  verb enum-bool  -  n 		verbosity flag 

