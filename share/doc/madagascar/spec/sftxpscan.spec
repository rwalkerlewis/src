[sftxpscan]
Cat:    RSF/system/seismic
Desc:   Velocity analysis using T-X-P domain
DocCmd: sftxpscan | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing scan data)
Param:  dv float  -   -  		step in velocity 
Param:  extend int  -  4 		trace extension 
Param:  mute int  -  12 		mute zone 
Param:  nv int  -   -  		number of scanned velocities 
Param:  smax float  -  2.0 		maximum heterogeneity 
Param:  smin float  -  1.0 		minimum heterogeneity 
Param:  str float  -  0.5 		maximum stretch allowed 
Param:  v0 float  -   -  		first scanned velocity 

