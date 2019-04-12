[sftransconv]
Cat:    RSF/user/luke
Desc:   
DocCmd: sftransconv | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  adj enum-bool  -  n 		if y reverse translation, if n, translation 
Param:  ker string  -   -  		convolution kernel file (auxiliary input file name)
Param:  trans string  -   -  		variable translations file with same sampling as input, added ndim dimension (auxiliary input file name)
Param:  x1 float  -  0. 		fixed translation in first dimension 
Param:  x2 float  -  0. 		fixed translation in second dimension 

