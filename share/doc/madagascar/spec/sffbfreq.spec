[sffbfreq]
Cat:    RSF/user/chen
Desc:   frequency response of linear phase filter bank
DocCmd: sffbfreq | cat
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  interp string  -   -  		interpolation method: maxflat lagrange bspline 
Param:  m int  -  1 		b[-m, ... ,n] 
Param:  n int  -  1 		b[-m, ... ,n] 
Param:  n1 int  -  50 		samples in frequency domain is 2*n1+1 
Param:  nd int  -  1 		nd dimensional filter bank, nd should not be large, or you will need to buy a new disk array 

