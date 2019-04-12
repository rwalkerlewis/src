[sfmtres]
Cat:    RSF/user/yliu
Desc:   Calculate apparent resistivity and phase of MT data
DocCmd: sfmtres | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   Ey rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Hx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Hy rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  comp enum-bool  -  y 		component selection 
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 
Param:  phase enum-bool  -  n 		if y, calculate apparent resistivity, otherwise calculate phase 
Param:  verb enum-bool  -  n 		verbosity flag 

