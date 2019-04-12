[sfbilstack]
Cat:    RSF/user/yliu
Desc:   Bilateral stacking
DocCmd: sfbilstack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   weight rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  ax float  -   -  		Gaussian weight for the range distance 
Param:  bilat enum-bool  -  n 		if y, bilateral smoothing 
Param:  bx float  -   -  		Exponential weight for the domain distance 
Param:  niter int  -  20 		number of iterations 
Param:  verb enum-bool  -  n 		verbosity 

