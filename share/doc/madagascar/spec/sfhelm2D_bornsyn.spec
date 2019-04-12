[sfhelm2D_bornsyn]
Cat:    RSF/user/hzhu
Desc:   2D Born synthetic based on Helmholtz forward solver
DocCmd: sfhelm2D_bornsyn | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  hermite enum-bool  -  n 		Hermite operator 
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  refl string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		

