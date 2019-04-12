[sfthin]
Cat:    RSF/user/fomels
Desc:   Sparse deconvolution
DocCmd: sfthin | cat
Port:   stdin  rsf r req 	RSF standard input (containing seis data)
Port:   stdout rsf w req 	RSF standard output (containing refl data)
Port:   wave rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  conv string  -   -  		auxiliary output file name
Param:  eps float  -  0.0001 		regularization for Wiener deconvolution 
Param:  niter int  -  100 		maximum number of iterations 
Param:  pclip float  -  4 		percentage to threshold 

