[sfistinterp]
Cat:    RSF/user/pyang
Desc:   n-D IST interpolation using a generalized shrinkage operator
DocCmd: sfistinterp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mask string  -   -  		auxiliary input file name
Param:  mode string  -   -  		thresholding mode: 'hard', 'soft','pthresh','exp';
LDesc:         'hard', hard thresholding;	'soft', soft thresholding; 
LDesc:         'pthresh', generalized quasi-p; 'exp', exponential shrinkage 
Param:  n# int  -   -  		size of #-th axis 
Param:  niter int  -  100 		total number of iterations 
Param:  normp float  -  0.9 		quasi-norm: normp<2 
Param:  pclip float  -  10. 		starting data clip percentile (default is 10)
Param:  verb enum-bool  -  n 		verbosity 

