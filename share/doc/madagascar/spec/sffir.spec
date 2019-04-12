[sffir]
Cat:    RSF/user/chen
Desc:   FIR filter
DocCmd: sffir | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   fir rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  axis int  -  1 		apply fir filter on which dimension 

