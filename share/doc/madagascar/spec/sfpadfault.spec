[sfpadfault]
Cat:    RSF/user/zhiguang
Desc:   Horizontally pad fault
DocCmd: sfpadfault | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   bound rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   mask rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   newdip rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   ppbig rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   shift rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  conf int  -  1 		
Param:  extend enum-bool  -  y 		
Param:  mode enum-bool  -  y 		
Param:  order int  -  2 		

