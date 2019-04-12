[sfsv2d]
Cat:    RSF/user/yliu
Desc:   Velocity and heterogeneity parameter convert to dip
DocCmd: sfsv2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   anisotropy rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  abs enum-bool  -  y 		if y, use absolute value |x-x0| (available when mute=y) 
Param:  d float  -  12.5 		offset interval 
Param:  half enum-bool  -  n 		if y, half-offset instead of full offset 
Param:  hyper enum-bool  -  n 		if y, do hyperbolic mute (available when mute=y) 
Param:  inner enum-bool  -  n 		if y, do inner muter (available when mute=y) 
Param:  mute enum-bool  -  n 		if y, use mutter 
Param:  n int  -  32 		offset number 
Param:  o float  -  0. 		offset origin 
Param:  t0 float  -  0. 		starting time (available when mute=y) 
Param:  tp float  -  0.150 		end time (available when mute=y) 
Param:  v0 float  -  10000 		velocity (available when mute=y) 
Param:  x0 float  -  0. 		starting space (available when mute=y) 

