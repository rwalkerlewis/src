[sfdwtdenoise]
Cat:    RSF/user/chenyk
Desc:   2D Digital Wavelet Transoform Denoising
DocCmd: sfdwtdenoise | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  pclip float  -  99. 		data clip percentile (default is 99)
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is linear  

