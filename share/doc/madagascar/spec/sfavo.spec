[sfavo]
Cat:    RSF/system/seismic
Desc:   Compute intercept and gradient by least squares
DocCmd: sfavo | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing avo data)
Param:  half enum-bool  -  y 		if y, the second axis is half-offset instead of full offset 
Param:  offset string  -   -  		auxiliary input file name

