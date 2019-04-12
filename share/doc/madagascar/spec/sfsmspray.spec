[sfsmspray]
Cat:    RSF/user/fomels
Desc:   Smoothing by spraying
DocCmd: sfsmspray | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  ns int  -  0 		smoothing radius 
Param:  type string  -   -  		weight type (triangle, gauss) 

