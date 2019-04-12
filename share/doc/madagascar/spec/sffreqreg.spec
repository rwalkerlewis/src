[sffreqreg]
Cat:    RSF/user/yliu
Desc:   Local frequency interpolation
DocCmd: sffreqreg | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dw float  -   -  		frequency step 
Param:  mask string  -   -  		auxiliary input file name
Param:  niter int  -  100 		number of inversion iterations 
Param:  nw int  -   -  		number of frequencies 
Param:  rect int  -  10 		smoothing radius 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w0 float  -  0. 		first frequency 

