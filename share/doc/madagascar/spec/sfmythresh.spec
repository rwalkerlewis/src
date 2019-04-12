[sfmythresh]
Cat:    RSF/user/pyang
Desc:   Generalized thresholding operator
DocCmd: sfmythresh | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  mode string  -   -  		thresholding mode='hard', 'soft','pthresh' or 'exp';
LDesc:         'hard', hard thresholding;	'soft', soft thresholding; 
LDesc:         'pthresh', generalized quasi-p; 'exp', exponential shrinkage 
Param:  p float  -  0.35 		norm=p, where 0<p<=1 
Param:  pclip float  -  99. 		percentage to clip 

