[sfcicop2d]
Cat:    RSF/user/psava
Desc:   Conventional IC 2D
DocCmd: sfcicop2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fimg data)
Port:   stdout rsf w req 	RSF standard output (containing Fwfl data)
Port:   opr rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  oprcausal enum-bool  -  n 		causal opr? 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  wflcausal enum-bool  -  n 		causal wfl? 

