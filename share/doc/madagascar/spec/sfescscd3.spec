[sfescscd3]
Cat:    RSF/user/cram
Desc:   Daemon for distributed computation of stitched escape solutions in supercells in 3-D
DocCmd: sfescscd3 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  inet int  -  1 		Network interface index 
Param:  ith int  -  0 		Make every ith process a daemon 
Param:  ma int  -  20 		How many azimuth angles to expect per request 
Param:  mb int  -  20 		How many inclination angles to expect per request 
Param:  nab int  -  1 		Number of angular blocks to keep in memory per daemon 
Param:  nthreads int  -   -  		Number of threads (connections) per daemon 
LDesc:  (defaults to: 2*ncpu)
Param:  port int  -  29542 		TCP port for listening 
Param:  scgrid string  -   -  		Grid of supercells of local escape solutions (auxiliary input file name)
Param:  tdelay int  -  0 		Time delay before accessing data, tdel*icpu (secs) 
Param:  timeout int  -  10 		Inactivity time before shutdown (mins) 

