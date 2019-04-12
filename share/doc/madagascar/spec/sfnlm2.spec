[sfnlm2]
Cat:    RSF/user/chenyk
Desc:   2D non-local median filtering
DocCmd: sfnlm2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  f1 int  -  2 		radio of similarity window 
Param:  f2 int  -  2 		radio of similarity window 
Param:  h float  -  0.5 		degree of filtering 
Param:  t1 int  -  5 		radio of search window 
Param:  t2 int  -  5 		radio of search window 

