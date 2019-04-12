[sfprestolt]
Cat:    RSF/system/seismic
Desc:   Prestack Stolt modeling/migration
DocCmd: sfprestolt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  depth enum-bool  -  n 		y: depth migration, n: time migration 
Param:  dh float  -   -  		offset sampling 
Param:  extend int  -  4 		trace extension 
Param:  inv enum-bool  -  n 		y: modeling, n: migration 
Param:  nh int  -   -  		number of offsets 
Param:  pad int  -   -  		padding on the time axis 
LDesc:  (defaults to: nt)
Param:  stack enum-bool  -  y 		if y: stack migrated image 
Param:  vel float  -   -  		constant velocity 

