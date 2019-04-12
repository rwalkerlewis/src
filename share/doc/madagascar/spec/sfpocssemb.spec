[sfpocssemb]
Cat:    RSF/user/chenyk
Desc:   POCS using semblance thresholding or amplitude thresholding
DocCmd: sfpocssemb | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (containing outp data)
Port:   mask rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snr rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  ifsnr int  -  0 		If compute SNR during iteration 
Param:  niter int  -  10 		Get the number of iterations 
Param:  np int  -   -  		number of p 
LDesc:  (defaults to: nx)
Param:  pmin float  -  -2 		minimum p 
Param:  spec1 string  -   -  		auxiliary output file name
Param:  spec2 string  -   -  		auxiliary output file name
Param:  true string  -   -  		auxiliary input file name
Param:  type string  -   -  		[amplitude, semblance] thresholding type, the default is amplitude thresholding  

