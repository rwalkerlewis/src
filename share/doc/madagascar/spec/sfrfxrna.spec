[sfrfxrna]
Cat:    RSF/user/gchliu
Desc:   Local prediction filter for complex numbers (n-dimensional)
DocCmd: sfrfxrna | cat
Port:   stdin  rsf r req 	RSF standard input (containing dat data)
Port:   stdout rsf w req 	RSF standard output (containing flt data)
Param:  jump int  -  1 		jump 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of iterations 
Param:  ns int  -  1 		shifts of both sides npef=2*ns+1
Param:  pred string  -   -  		auxiliary output file name
Param:  ty string  -   -  		Prediction type: all=backward+forward
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  zdata string  -   -  		auxiliary output file name
Param:  zshift string  -   -  		auxiliary output file name

