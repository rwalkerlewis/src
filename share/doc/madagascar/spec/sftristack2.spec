[sftristack2]
Cat:    RSF/user/fomels
Desc:   2-D resampling with triangle weights
DocCmd: sftristack2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  gauss enum-bool  -  n 		use pseudo-gaussian 
Param:  rect1 int  -  1 		
Param:  rect2 int  -  1 		smoothing radius 

