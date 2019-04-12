[sfoway1]
Cat:    RSF/system/seismic
Desc:   Oriented one-way wave equation
DocCmd: sfoway1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vgrad rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.1 		stretch regularization 
Param:  lagrange enum-bool  -  n 		Use Lagrangian method 

