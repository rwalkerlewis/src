[sffpow]
Cat:    RSF/user/fomels
Desc:   Time/frequency power estimation
DocCmd: sffpow | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   beta rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  bmax float  -  1.0 		maximum value of beta 
Param:  bmin float  -  -1.0 		minimum value of beta 
Param:  fmax float  -   -  		maximum frequency 
LDesc:  (defaults to: o1+(n1-1)*d1)
Param:  fmin float  -   -  		minimum frequency 
LDesc:  (defaults to: o1)
Param:  nb int  -  10 		
Param:  niter int  -  10 		number of Newton iterations 
Param:  time enum-bool  -  n 		time axis 
Param:  tol float  -   -  		accuracy tolerance for beta 
LDesc:  (defaults to: SF_EPS)
Param:  verb enum-bool  -  y 		verbosity flag 

