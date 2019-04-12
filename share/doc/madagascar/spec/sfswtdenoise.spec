[sfswtdenoise]
Cat:    RSF/system/generic
Desc:   Denoising using stationary wavelet transform
DocCmd: sfswtdenoise | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  len_filter int  -  2 		filter length 
Param:  n_layer int  -  2 		number of wavelet transform layers 
Param:  ratio float  -  1. 		ratio for denoising 

