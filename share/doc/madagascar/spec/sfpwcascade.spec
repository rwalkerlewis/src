[sfpwcascade]
Cat:    RSF/user/pwd
Desc:   Plane-wave smoothing by box cascade
DocCmd: sfpwcascade | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order int  -  1 		accuracy order 
Param:  rect int  -  0 		smoothing radius 
Param:  verb enum-bool  -  n 		verbosity 

