[sfctshift]
Cat:    RSF/user/zhiguang
Desc:   Correct time-shift gathers
DocCmd: sfctshift | cat
Port:   stdin  rsf r req 	RSF standard input (containing tgather data)
Port:   stdout rsf w req 	RSF standard output (containing cgather data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  pad int  -  30 		

