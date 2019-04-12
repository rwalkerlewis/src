[sfhelm2D_rtm]
Cat:    RSF/user/hzhu
Desc:   2D Frequency Domain Reverse Time Migration
DocCmd: sfhelm2D_rtm | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nh int  -  0 		
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  receiver string  -   -  		auxiliary input file name
Param:  record string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		

