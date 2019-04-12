[sfpolyfit]
Cat:    RSF/user/fomels
Desc:   Fitting a polynomial by least-squares
DocCmd: sfpolyfit | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  coef string  -   -  		(optional) coefficients (auxiliary output file name)
Param:  coord string  -   -  		coordinates (auxiliary input file name)
Param:  d1 float  -   -  		sampling for regularly sampled 
Param:  eps float  -   -  		regularization parameter 
LDesc:  (defaults to: 0.0f)
Param:  n1 int  -   -  		number of samples for regularly sampled 
Param:  np int  -  1 		polynomial order 
Param:  o1 float  -   -  		origin for regularly sampled 
Param:  reg string  -   -  		(optional) regularly sampled (auxiliary output file name)

