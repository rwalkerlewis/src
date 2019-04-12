[sfgroll]
Cat:    RSF/user/yliu
Desc:   Add linear-chirp ground-roll noise to the data
DocCmd: sfgroll | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha float  -  0.1 		width parameter of ground roll 
Param:  beg1 float  -  0. 		radial beginning point at first axis 
Param:  beg2 float  -  0. 		radial beginning point at second axis 
Param:  begf float  -  10. 		beginning frequency of ground roll 
Param:  endf float  -  5. 		ending frequency of ground roll 
Param:  rep enum-bool  -  n 		if y, replace data with noise 
Param:  theta float  -  0.2 		direction of central ground roll 

