[sflegacy]
Cat:    RSF/user/fomels
Desc:   Merging legacy and hires datasets
DocCmd: sflegacy | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   hweight rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   lweight rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   rect rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 

