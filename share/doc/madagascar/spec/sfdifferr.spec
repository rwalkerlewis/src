[sfdifferr]
Cat:    RSF/user/browaeys
Desc:   Error by substituting numerical solution into equation
DocCmd: sfdifferr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   slow rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowx rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   slowz rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  err_cutoff float  -  0.2 		
Param:  iq int  -  2 		switch for escape variable 0=x, 1=a, 2=t, 3=z 

