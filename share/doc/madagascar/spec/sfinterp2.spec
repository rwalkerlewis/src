[sfinterp2]
Cat:    RSF/user/fomels
Desc:   Multiple-arrival interpolation
DocCmd: sfinterp2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   grid rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   size rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nw int  -  4 		Interpolation accuracy 
Param:  plane int  -  0 		0: point-source, 4: plane-wave 
Param:  sx float  -  0. 		
Param:  sz float  -  0. 		Shot coordinates 

