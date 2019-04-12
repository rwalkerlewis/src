[sfmvo1]
Cat:    RSF/user/yliu
Desc:   Calculate MVO and PVO curve of CSEM data (another version)
DocCmd: sfmvo1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  f float  -  0.08 		calculate frequency 
Param:  log enum-bool  -  y 		if y, calculate logarithm of MVO 
Param:  mvo enum-bool  -  y 		if y, MVO curve; otherwise, PVO curve 
Param:  n int  -  1 		number of window period 
Param:  nnw int  -  1600 		sample window 
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 

