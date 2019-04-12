[vpvrtest]
Cat:    RSF/user/dellinger
Desc:   Plot impulse responses in 2 dimensions
DocCmd: vpvrtest | cat
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  c11 float  -  1. 		
Param:  c13 float  -  .5 		
Param:  c33 float  -  1. 		
Param:  c55 float  -  .25 		
Param:  dash float  -  0.0 		
Param:  flip enum-bool  -  n 		reciprocal of W's used in Francis' approximation 
Param:  francis enum-bool  -  n 		
Param:  groupscale float  -  1. 		scales only the group stuff 
Param:  inc float  -  0.5 		increment of phi sub w in degrees 
Param:  invert enum-bool  -  n 		reciprocal of plotting radius 
Param:  m int  -  -1 		
Param:  norm float  -  1. 		
Param:  phasescale float  -  1. 		scales only the phase stuff 
Param:  which enum-bool  -  n 		transform from phase to group domain or vice versa 

