[sfhelmlu]
Cat:    RSF/user/sparse
Desc:   2D Helmholtz solver by LU factorization
DocCmd: sfhelmlu | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  hermite enum-bool  -  n 		Hermite operator 
Param:  load enum-bool  -  n 		load LU 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  save enum-bool  -  n 		save LU 
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  n 		verbosity flag 

