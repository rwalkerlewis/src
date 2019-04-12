[sfdipcoh]
Cat:    RSF/user/chen
Desc:   3D Coherence cube
DocCmd: sfdipcoh | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dip1 string  -   -  		auxiliary input file name
Param:  lag1 int  -  3 		maximal time lag on 2nd axis 
Param:  lag2 int  -  3 		maximal time lag on 3rd axis 
Param:  nw int  -  5 		half window size for coherence 
Param:  twod enum-bool  -  y 		y: only twod coherence 
Param:  verb enum-bool  -  y 		verbosity 

