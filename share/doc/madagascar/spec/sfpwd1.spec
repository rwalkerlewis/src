[sfpwd1]
Cat:    RSF/user/pwd
Desc:   One side of plane wave destruction
DocCmd: sfpwd1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  left enum-bool  -  y 		if using left or right side of PWD 
Param:  nj1 int  -  1 		in-line aliasing 
Param:  nj2 int  -  1 		cross-line aliasing 
Param:  order int  -  1 		accuracy 

