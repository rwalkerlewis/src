[sflocorr]
Cat:    RSF/user/yliu
Desc:   Local correlation measure between two datasets
DocCmd: sflocorr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,1))
Param:  verb enum-bool  -  n 		verbosity 

