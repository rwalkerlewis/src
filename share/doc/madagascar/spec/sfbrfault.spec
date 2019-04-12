[sfbrfault]
Cat:    RSF/user/zhiguang
Desc:   Bridge fault zones with smooth transition
DocCmd: sfbrfault | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   mask rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   shift rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  mode enum-bool  -  y 		
Param:  order int  -  1 		
Param:  replace enum-bool  -  n 		
Param:  width int  -  9 		

