[sflskernel]
Cat:    RSF/user/luke
Desc:   
DocCmd: sflskernel | cat
Port:   stdin  rsf r req 	RSF standard input (containing _in data)
Port:   stdout rsf w req 	RSF standard output (containing _out data)
Param:  adj enum-bool  -  n 		if n takes kernel and outputs function, if y takes function and outputs kernel 
Param:  match string  -   -  		auxiliary input file name
Param:  nk1 int  -  5 		size of kernel in dimension 1
Param:  nk2 int  -  5 		size of kernel in dimension 2 
Param:  wrap enum-bool  -  n 		if y, perform doughnut wrapping.  if n, no wrapping 

