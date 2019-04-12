[sfcfftexpmig2]
Cat:    RSF/user/jsun
Desc:   Complex 2-D exploding reflector migration (read in initial complex wavefield in depth)
DocCmd: sfcfftexpmig2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing wvfld data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -   -  		
Param:  nt int  -   -  		
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  verb enum-bool  -  n 		verbosity 

