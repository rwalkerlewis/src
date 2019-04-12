[sfhelmmig]
Cat:    RSF/user/sparse
Desc:   2D frequency-domain migration with space-lag imaging condition
DocCmd: sfhelmmig | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  data string  -   -  		auxiliary input file name
Param:  load enum-bool  -  n 		load LU 
Param:  nh int  -  0 		horizontal space-lag 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  save enum-bool  -  n 		save LU 
Param:  source string  -   -  		auxiliary input file name
Param:  timg string  -   -  		auxiliary output file name
Param:  ur string  -   -  		auxiliary output file name
Param:  us string  -   -  		auxiliary output file name
Param:  uts int  -  0 		number of OMP threads 
Param:  verb enum-bool  -  n 		verbosity flag 

