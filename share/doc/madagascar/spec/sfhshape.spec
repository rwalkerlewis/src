[sfhshape]
Cat:    RSF/user/gee
Desc:   Multidimensional shaping using helix transform
DocCmd: sfhshape | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		if y, do adjoint operation 
Param:  lag string  -   -  		
Param:  n int-list  -   -  		 [dim]
Param:  ns int  -   -  		scaling 

