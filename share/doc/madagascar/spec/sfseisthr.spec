[sfseisthr]
Cat:    RSF/user/chenyk
Desc:   Seislet Transform Denoising using Thresholding
DocCmd: sfseisthr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0.01 		regularization 
Param:  order1 int  -  1 		accuracy order for seislet transform
Param:  pclip float  -  99. 		data clip percentile (default is 99)
Param:  slet string  -   -  		seismic domain (auxiliary output file name)
Param:  sletthr string  -   -  		thresholded seislet domain (auxiliary output file name)
Param:  thrtype string  -   -  		[soft,hard] thresholding type, the default is soft  
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  

