[sfpwstack]
Cat:    RSF/user/pwd
Desc:   Recursive stacking by plane-wave construction
DocCmd: sfpwstack | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  mode int  -  1 		1: predict backward, 2: predict forward then backward 
Param:  order int  -  1 		accuracy order 
Param:  verb enum-bool  -  n 		

