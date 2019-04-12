[sfriesz]
Cat:    RSF/user/fomels
Desc:   Compute 2-D Riesz transform
DocCmd: sfriesz | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  order int  -  10 		Hilbert transformer order 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 

