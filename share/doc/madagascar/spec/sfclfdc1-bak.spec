[sfclfdc1-bak]
Cat:    RSF/user/jsun
Desc:   1D 10th-order Lowrank Onestep FD coefficient
DocCmd: sfclfdc1-bak | cat
Port:   stdin  rsf r req 	RSF standard input (containing velf data)
Port:   stdout rsf w req 	RSF standard output (containing outm data)
Param:  dt   -   -  		time step
Param:  eps   -   -  		tolerance
LDesc:  (defaults to: 1.e-4)
Param:  npk   -   -  		maximum rank
LDesc:  (defaults to: 20)
Param:  seed   -   -  		
LDesc:  (defaults to: time(NULL)

