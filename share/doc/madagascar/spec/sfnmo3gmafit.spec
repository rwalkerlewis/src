[sfnmo3gmafit]
Cat:    RSF/user/zone
Desc:   3D NMO GMA  linearized operator preparation for lsfit
DocCmd: sfnmo3gmafit | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   coef rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   fit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   offsetx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   offsety rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  gather enum-bool  -  n 		Memory allocation
Param:  verb enum-bool  -  n 		

