[sfswell]
Cat:    RSF/user/yliu
Desc:   Add swell noise to the data
DocCmd: sfswell | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  den float  -  10. 		noise density (percent, default=10, Min=0, Max=100) 
Param:  inten float  -  0.1 		noise intensity (multiple peak value of data, default=0.1) 
Param:  length int  -  30 		max noise length (default=30) 
Param:  noise enum-bool  -  n 		if y, output noise only 
Param:  num int  -  5 		noise number (default=5) 
Param:  rep enum-bool  -  n 		if y, replace data with noise 
Param:  slope float  -  0.1 		noise slope (default=0.1) 
Param:  width int  -  4 		max noise width (default=4) 

