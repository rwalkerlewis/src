[sfazpwd]
Cat:    RSF/user/dmerzlikin
Desc:   Azimuthal Plane-Wave Destruction
DocCmd: sfazpwd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   az rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  nj1 int  -  1 		antialiasing iline 
Param:  nj2 int  -  1 		antialiasing xline 
Param:  order int  -  1 		accuracy order 
Param:  sm enum-bool  -  y 		if perform AzPWD filtering 

