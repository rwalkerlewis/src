[sfsvmf]
Cat:    RSF/user/chenyk
Desc:   Space varying median filtering
DocCmd: sfsvmf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   similarity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  L string  -   -  		auxiliary output file name
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  l1 int  -  4 		space-varying window parameter 'l1' (default=4)
Param:  l2 int  -  2 		space-varying window parameter 'l2' (default=2)
Param:  l3 int  -  2 		space-varying window parameter 'l3' (default=2)
Param:  l4 int  -  4 		space-varying window parameter 'l4' (default=4)
Param:  lambda1 float  -  0.15 		space-varying window parameter 'lambda1' (default=0.15)
Param:  lambda2 float  -  0.25 		space-varying window parameter 'lambda2' (default=0.25)
Param:  lambda3 float  -  0.75 		space-varying window parameter 'lambda3' (default=0.75)
Param:  lambda4 float  -  0.85 		space-varying window parameter 'lambda4' (default=0.85)
Param:  ne int  -   -  		processing window ending point, corresponding to the temporal axis, n2 means transposed first-axis dimension. 
LDesc:  (defaults to: n2-1)
Param:  nfw int  -   -  		reference filter-window length (>l4, positive and odd integer)
Param:  ns int  -  0 		processing window starting point, corresponding to the temporal axis 

