[sfstfchain2]
Cat:    RSF/user/fomels
Desc:   Find a symmetric chain of Fourier weighting and scaling
DocCmd: sfstfchain2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing src data)
Port:   stdout rsf w req 	RSF standard output (containing wht data)
Port:   fweight rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   match rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   target rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  frect1 int  -  1 		
Param:  frect2 int  -  1 		smoothing in frequency 
Param:  liter int  -  50 		number of linear iterations 
Param:  niter int  -  0 		number of iterations 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing in time 

