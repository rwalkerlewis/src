[sfbeamform]
Cat:    RSF/user/pwd
Desc:   2-D beam forming
DocCmd: sfbeamform | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  gauss enum-bool  -  n 		use pseudo-gaussian 
Param:  order int  -  1 		PWD accuracy order 
Param:  rect int  -  3 		smoothing radius 

