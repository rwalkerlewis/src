[sffftfwi_sparse_2d]
Cat:    RSF/user/zhiguang
Desc:   2D frequency domain full waveform inversion with sparsity regularization
DocCmd: sffftfwi_sparse_2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dip string  -   -  		auxiliary input file name
Param:  misfit string  -   -  		auxiliary output file name
Param:  niter int  -  10 		number of iteration 
Param:  npml int  -  20 		PML width 
Param:  order string  -   -  		discretization scheme (default optimal 9-point) 
Param:  par int  -  1 		seislet transform accuracy order 
Param:  pclip float  -  8. 		soft thresholding parameter 
Param:  receiver string  -   -  		auxiliary input file name
Param:  record string  -   -  		auxiliary input file name
Param:  source string  -   -  		auxiliary input file name
Param:  sparsity enum-bool  -  y 		if true, sparsity constriant; if false, normal FWI 
Param:  type string  -   -  		[haar,linear,biorthogonal] wavelet type, the default is biorthogonal 
Param:  uts int  -  0 		
Param:  vout string  -   -  		auxiliary output file name

