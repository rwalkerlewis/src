[sfdsmooth]
Cat:    RSF/system/generic
Desc:   Multi-dimensional triangle smoothing - derivative
DocCmd: sfdsmooth | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ider int  -  0 		direction of the derivative (0 means no derivative) 
Param:  nderiv int  -  6 		derivative filter accuracy 
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  repeat int  -  1 		repeat smoothing several times 

