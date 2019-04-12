[sftimerev2d]
Cat:    RSF/user/jsun
Desc:   2-D correlative time reversal imaging of passive seismic data
DocCmd: sftimerev2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  abc enum-bool  -  n 		absorbing boundary condition 
Param:  cb float  -   -  		
LDesc:  (defaults to: 0.0f)
Param:  depth int  -  0 		geophone depth 
Param:  ngrp int  -  1 		number of groups 
Param:  snap int  -  0 		wavefield snapshot flag 
Param:  verb enum-bool  -  n 		verbosity flag 

