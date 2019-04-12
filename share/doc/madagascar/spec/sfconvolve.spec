[sfconvolve]
Cat:    RSF/user/luke
Desc:   
DocCmd: sfconvolve | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  adj enum-bool  -  n 		if y adjoint convolution, if n, convolution 
Param:  ker string  -   -  		convolution kernel file (auxiliary input file name)
Param:  wrap enum-bool  -  n 		if y, perform doughnut wrapping.  if n, no wrapping 

