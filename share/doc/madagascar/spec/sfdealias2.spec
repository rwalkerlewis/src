[sfdealias2]
Cat:    RSF/user/pwd
Desc:   2-D (inline) trace interpolation to a denser grid using PWD
DocCmd: sfdealias2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  both enum-bool  -  n 		if use left and right slopes 
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 

