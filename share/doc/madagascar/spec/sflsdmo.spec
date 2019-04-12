[sflsdmo]
Cat:    RSF/user/seisinv
Desc:   Kirchhoff least-squares DMO with antialiasing by reparameterization
DocCmd: sflsdmo | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  h float  -   -  		
Param:  half enum-bool  -  y 		if y, the third axis is half-offset instead of full offset 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  mint int  -  2 		starting time sample 
Param:  n int  -  32 		number of offset samples 
Param:  niter int  -  5 		iterative number 
Param:  type int  -  1 		type of amplitude (0,1,2,3) 
Param:  velhalf float  -  0.75 		half-velocity 

