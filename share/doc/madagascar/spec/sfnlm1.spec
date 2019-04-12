[sfnlm1]
Cat:    RSF/user/chenyk
Desc:   1D non-local median filtering
DocCmd: sfnlm1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  f int  -  2 		radio of similarity window 
Param:  h float  -  0.5 		degree of filtering 
Param:  t int  -  5 		radio of search window 

