[sfvelmap]
Cat:    RSF/user/browaeys
Desc:   2-D mapping from moving-object velocity to plane-wave slowness
DocCmd: sfvelmap | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dt float  -  0.5 		line parameter increment 
Param:  nt int  -  360 		number of line parameter for integration in [0,180]. 
Param:  osx float  -   -  		
LDesc:  (defaults to: -0.5/dvx)
Param:  osy float  -   -  		
LDesc:  (defaults to: -0.5/dvy)
Param:  ot float  -  0. 		line parameter origin 

