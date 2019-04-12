[vpvr]
Cat:    RSF/user/dellinger
Desc:   Plot impulse responses in 2 dimensions
DocCmd: vpvr | cat
Port:   stdout vpl w req 	VPL standard output (containing plot data)
Param:  c11 float  -  0. 		
Param:  c13 float  -  0. 		
Param:  c33 float  -  0. 		
Param:  c55 float  -  0. 		
Param:  c66 float  -  0. 		
Param:  color int  -  7 		
Param:  dash float  -  0.0 		
Param:  disp enum-bool  -  y 		if n, give phase velocity instead of dispersion relation 
Param:  edash float  -  0.1 		elliptical approximation dash 
Param:  ellipse enum-bool  -  y 		if use elliptic approximation 
Param:  fat int  -  5 		
Param:  group enum-bool  -  y 		if n, give group slowness instead of group velocity 
Param:  groupscale float  -  1. 		scales only the group stuff 
Param:  inc float  -  0.5 		increment of phi sub w in degrees 
Param:  info enum-bool  -  y 		if print in small letters the elastic constants across the top 
Param:  line enum-bool  -  n 		if draw lines to indicate some important angles. (Angles at
LDesc:       which triplication 'first' occurs, and angles at which pure P
LDesc:       and Sv modes exist) 
Param:  log string  -   -  		
Param:  norm float  -  0. 		
Param:  only string  -   -  		(Pdisp, SVdisp, SHdisp, P, SV, SH) 
Param:  particle enum-bool  -  n 		if show particle motion directions 
Param:  phasescale float  -  .5 		scales only the phase stuff 
Param:  title string  -   -  		
Param:  vrscale float  -  1. 		scales everything by a factor 

