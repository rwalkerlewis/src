[sfimpl1]
Cat:    RSF/system/generic
Desc:   1-D anisotropic diffusion
DocCmd: sfimpl1 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  pclip float  -  50. 		percentage clip for the gradient 
Param:  rect1 float  -   -  		smoothing radius 
Param:  tau float  -  0.1 		smoothing time 
Param:  up enum-bool  -  n 		smoothing style 

