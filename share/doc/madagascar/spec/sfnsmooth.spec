[sfnsmooth]
Cat:    RSF/user/fomels
Desc:   N-D non-stationary smoothing
DocCmd: sfnsmooth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  rect# string  -   -  		size of the smoothing stencil in #-th dimension /auxiliary input file/ 
Param:  repeat int  -  1 		repeat filtering several times 
Param:  shift# string  -   -  		shifting of the smoothing stencil in #-th dimension /auxiliary input file/ 

