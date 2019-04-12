[sfepsf]
Cat:    RSF/user/yliu
Desc:   1-D and 2-D edge-preserving smoothing (EPS) filter
DocCmd: sfepsf | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  boundary enum-bool  -  n 		if y, boundary is data, whereas zero
Param:  nfw1 int  -   -  		filter-window length in n1 direction (positive and odd integer) 
Param:  nfw2 int  -  1 		filter-window length in n2 direction (default=1, 1D case)
Param:  sigma float  -  3. 		Gaussian weight radius (only for stack) 
Param:  type string  -   -  		[stack,median] filter choice, the default is stack (mean) 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight enum-bool  -  n 		Gaussian weight flag (only for stack) 

