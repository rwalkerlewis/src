[sfepot]
Cat:    RSF/user/psava
Desc:   compute quasi-static electric potential
DocCmd: sfepot | cat
Port:   stdin  rsf r req 	RSF standard input (containing Feso data)
Port:   stdout rsf w req 	RSF standard output (containing Fepo data)
Port:   con rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cbnd enum-bool  -  y 		conductive boundary 
Param:  csrf enum-bool  -  n 		conductive  surface 
Param:  meth int  -  0 		method flag 
Param:  nit int  -  100000 		Jacobi iterations 
Param:  verb enum-bool  -  n 		verbosity flag 

