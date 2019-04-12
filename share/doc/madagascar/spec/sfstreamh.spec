[sfstreamh]
Cat:    RSF/user/gee
Desc:   Streaming PEF on a helix
DocCmd: sfstreamh | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  a int-list  -   -  		filter shape  [dim]
Param:  adj enum-bool  -  n 		adjoint flag (for linear operator) 
Param:  eps float  -   -  		regularization 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  jump int  -  1 		jump > 1 is used for trace interpolation 
Param:  lag string  -   -  		auxiliary input file name
Param:  n int-list  -   -  		 [dim]
Param:  na int  -  0 		PEF filter size (not including leading one) 
Param:  pattern string  -   -  		pattern data (for linear operator) (auxiliary input file name)

