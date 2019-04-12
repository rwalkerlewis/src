[sfiwioper]
Cat:    RSF/user/sparse
Desc:   Image-domain waveform tomography (linear operator)
DocCmd: sfiwioper | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  load enum-bool  -  n 		load LU 
Param:  mass enum-bool  -  n 		if y, use discretization-based mass term 
Param:  model string  -   -  		auxiliary input file name
Param:  nh int  -  0 		horizontal space-lag 
Param:  npml int  -  10 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  precon string  -   -  		auxiliary input file name
Param:  ur string  -   -  		auxiliary input file name
Param:  us string  -   -  		auxiliary input file name
Param:  uts int  -  0 		number of OMP threads 
Param:  weight string  -   -  		auxiliary input file name

