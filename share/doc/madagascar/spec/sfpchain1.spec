[sfpchain1]
Cat:    RSF/user/fomels
Desc:   Nonstationary Prony by chain of PEFs - linear operator
DocCmd: sfpchain1 | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   pef rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sig rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 

