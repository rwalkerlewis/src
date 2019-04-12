[sfhelm2D_fwi]
Cat:    RSF/user/hzhu
Desc:   2D Frequency Domain Full Waveform Inversion
DocCmd: sfhelm2D_fwi | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dip string  -   -  		auxiliary input file name
Param:  niter int  -  0 		
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  precond enum-bool  -  n 		
Param:  radius int  -   -  		
Param:  receiver string  -   -  		auxiliary input file name
Param:  record string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  uts int  -  0 		

