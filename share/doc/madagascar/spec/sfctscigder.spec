[sfctscigder]
Cat:    RSF/user/zhiguang
Desc:   Get the derivative of time-shift gathers
DocCmd: sfctscigder | cat
Port:   stdin  rsf r req 	RSF standard input (containing Ftg data)
Port:   stdout rsf w req 	RSF standard output (containing Fder data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  pad int  -  30 		

