[sfweigwf]
Cat:    RSF/user/psava
Desc:   3-D wave-equation wavefield continuation with adjoint-source
DocCmd: sfweigwf | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fsou data)
Port:   stdout rsf w req 	RSF standard output (containing Fwfl data)
Port:   coo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  causal enum-bool  -  n 		causality flag 
Param:  down enum-bool  -  y 		up/down   flag 
Param:  verb enum-bool  -  n 		verbosity flag 

