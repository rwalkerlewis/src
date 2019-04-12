[sfimpl3]
Cat:    RSF/system/generic
Desc:   3-D anisotropic diffusion
DocCmd: sfimpl3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dist string  -   -  		inverse distance file (input) 
Param:  nsnap int  -  1 		number of snapshots 
Param:  pclip float  -  50. 		percentage clip for the gradient 
Param:  rect1 float  -   -  		
Param:  rect2 float  -   -  		
Param:  rect3 float  -   -  		smoothing radius 
Param:  snap string  -   -  		snapshot file (output) 
Param:  tau float  -  0.1 		smoothing time 
Param:  up enum-bool  -  n 		smoothing style 
Param:  verb enum-bool  -  n 		verbosity flag 

