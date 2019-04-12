[sfswvarimax]
Cat:    RSF/user/jsun
Desc:   Sliding window varimax
DocCmd: sfswvarimax | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  f1 int  -  0 		sliding window radius 
Param:  f2 int  -  0 		sliding window radius 
Param:  n1 int  -   -  		sliding window radius 
LDesc:  (defaults to: nz0-fz)
Param:  n2 int  -   -  		sliding window radius 
LDesc:  (defaults to: nx0-fx)
Param:  size int  -  0 		sliding window radius 
Param:  sw enum-bool  -  n 		sliding window 
Param:  term float  -  100. 		variance threshold (normalized) 
Param:  thres float  -  0. 		variance threshold (normalized) 

