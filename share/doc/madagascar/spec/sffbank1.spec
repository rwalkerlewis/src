[sffbank1]
Cat:    RSF/user/chen
Desc:   1d filter bank
DocCmd: sffbank1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 

