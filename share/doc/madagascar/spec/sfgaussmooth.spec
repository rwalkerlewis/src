[sfgaussmooth]
Cat:    RSF/user/fomels
Desc:   Recursive Gaussian smoothing on the fast axis
DocCmd: sfgaussmooth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  der enum-bool  -  n 		compute derivative 
Param:  rect float  -  1 		smoothing radius 
Param:  repeat int  -  1 		repeat filtering several times 

