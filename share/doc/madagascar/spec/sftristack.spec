[sftristack]
Cat:    RSF/user/fomels
Desc:   Resampling with triangle weights
DocCmd: sftristack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  gauss enum-bool  -  n 		use pseudo-gaussian 
Param:  rect int  -  1 		smoothing radius 

