[sfblur]
Cat:    RSF/user/fomels
Desc:   2-D blurring and deblurring
DocCmd: sfblur | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  eps float  -  1. 		scaling 
Param:  inv enum-bool  -  n 		inversion flag 
Param:  ncycle int  -  1 		number of nonlinear cycles 
Param:  niter int  -  100 		maximum number of iterations 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  rect int  -   -  		blurring radius 
Param:  rect2 float  -  1.0 		smoothing radius 
Param:  repeat int  -  1 		repeat smoothing 
Param:  spk enum-bool  -  y 		spiky inversion 

