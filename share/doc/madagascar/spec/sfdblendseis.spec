[sfdblendseis]
Cat:    RSF/user/chenyk
Desc:   Blending, or Deblending using seislet domain thresholding
DocCmd: sfdblendseis | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   shottime rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  init string  -   -  		auxiliary input file name
Param:  lambda float  -  0.5 		update step size 
Param:  mode string  -   -  		[b-blending,d-deblending] function mode, the default is d  
Param:  niter int  -  30 		number of iterations 
Param:  order int  -  1 		accuracy order for seislet transform
Param:  thr float  -  10 		threshold value (coefficients preserved in percentage) 
Param:  thrtype string  -   -  		[soft,hard] thresholding type, the default is soft  
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  
Param:  verb int  -  0 		output verbosity information 

