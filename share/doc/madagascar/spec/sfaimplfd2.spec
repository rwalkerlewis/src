[sfaimplfd2]
Cat:    RSF/user/petsc
Desc:   Implicit solution of 2-D acoustic wave equation
DocCmd: sfaimplfd2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing usol data)
Param:  fourth enum-bool  -  y 		Higher order flag 
Param:  niter int  -  10 		Number of solver iterations 
Param:  src string  -   -  		Source wavelet (auxiliary input file name)

