[sfaimplfd1]
Cat:    RSF/user/petsc
Desc:   Implicit solution of 1-D acoustic wave equation
DocCmd: sfaimplfd1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing usol data)
Param:  niter int  -  10 		Number of solver iterations 
Param:  src string  -   -  		Source wavelet (auxiliary input file name)

