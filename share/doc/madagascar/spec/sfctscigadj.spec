[sfctscigadj]
Cat:    RSF/user/zhiguang
Desc:   Correcting time-shift gathers and its adjoint
DocCmd: sfctscigadj | cat
Port:   stdin  rsf r req 	RSF standard input (containing Ftg data)
Port:   stdout rsf w req 	RSF standard output (containing Fcg data)
Port:   Fder0 rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fdertau rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		
Param:  dt float  -  0.001 		
Param:  pad int  -  100 		files 

