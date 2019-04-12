[sfarrival]
Cat:    RSF/user/fomels
Desc:   Multiple-arrival interpolation from down-marching
DocCmd: sfarrival | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   place rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  depth string  -   -  		auxiliary input file name
Param:  nw int  -  3 		interpolation accuracy 
Param:  sx float  -  0. 		source x position 

