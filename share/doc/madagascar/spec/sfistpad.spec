[sfistpad]
Cat:    RSF/user/pyang
Desc:   n-D IST interpolation using a generalized shrinkage operator and zero-padding
DocCmd: sfistpad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mask string  -   -  		auxiliary input file name
Param:  mode string  -   -  		thresholding mode: 'hard', 'soft','pthresh','exp';
LDesc:         'hard', hard thresholding;	   'soft', soft thresholding; 
LDesc:         'pthresh', generalized quasi-p;  'exp', exponential shrinkage 
Param:  n# int  -   -  		size of #-th axis 
Param:  niter int  -  100 		total number of iterations 
Param:  normp float  -  1. 		quasi-norm: normp<2 
Param:  pad int-list  -   -  		number of zeros to be padded for each axis  [dim]
Param:  pclip float  -  10. 		starting data clip percentile (default is 10)
Param:  pow2 enum-bool  -  n 		round up the length of each axis to be power of 2 
Param:  verb enum-bool  -  n 		verbosity 

