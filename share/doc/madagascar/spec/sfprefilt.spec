[sfprefilt]
Cat:    RSF/user/chen
Desc:   prefilter bank of pwd
DocCmd: sfprefilt | cat
Port:   stdin  rsf r req 	RSF standard input (containing input data)
Port:   stdout rsf w req 	RSF standard output (containing dip data)
Port:   coef rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   pf rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  eta float  -  0.05 		
Param:  iter int  -  5 		
Param:  nf int  -  1 		

