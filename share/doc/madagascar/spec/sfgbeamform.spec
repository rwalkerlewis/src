[sfgbeamform]
Cat:    RSF/user/fomels
Desc:   2-D lateral smoothing
DocCmd: sfgbeamform | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		adjoint flag 
Param:  rect int  -  3 		smoothing radius 
Param:  repeat int  -  2 		triangle convolutions 

