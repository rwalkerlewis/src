[sfhelm2D_forward]
Cat:    RSF/user/hzhu
Desc:   2D Helmholtz forward solver by LU factorization
DocCmd: sfhelm2D_forward | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  hermite enum-bool  -  n 		Hermite operator 
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		

