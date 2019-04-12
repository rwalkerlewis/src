[sfepfbe]
Cat:    RSF/user/chen
Desc:   Bi-Exponential Edge Preserving Smoothing
DocCmd: sfepfbe | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  kernel string  -   -  		similarity: gaussian 
Param:  lamda float  -  0.8 		lamda 
Param:  sigma float  -  1.0 		normalizing parameter 
Param:  twod enum-bool  -  n 		y, 2D smoothing 

