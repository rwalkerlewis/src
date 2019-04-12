[sftimecont]
Cat:    RSF/user/fomels
Desc:   Forward or reverse time continuation using fast marching
DocCmd: sftimecont | cat
Port:   stdin  rsf r req 	RSF standard input (containing vel data)
Port:   stdout rsf w req 	RSF standard output (containing time data)
Port:   surf rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  forwd enum-bool  -  n 		continue forward or backward 
Param:  order int  -  2 		Accuracy order 
Param:  vel enum-bool  -  y 		if y, the input is velocity; n, slowness squared 

