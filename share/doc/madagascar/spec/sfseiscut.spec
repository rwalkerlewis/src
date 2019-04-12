[sfseiscut]
Cat:    RSF/user/chenyk
Desc:   Seislet Transform Denoising using Mask Operator
DocCmd: sfseiscut | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  cut int  -   -  		cut threshold value 
LDesc:  (defaults to: n2/4)
Param:  eps float  -  0.01 		regularization 
Param:  order1 int  -  1 		accuracy order for seislet transform
Param:  slet string  -   -  		seismic domain (auxiliary output file name)
Param:  sletcut string  -   -  		cutted seislet domain (auxiliary output file name)
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  

