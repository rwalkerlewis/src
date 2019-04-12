[sfcramdd]
Cat:    RSF/user/cram
Desc:   Daemon for distributed storage of prestack data for angle migration
DocCmd: sfcramdd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  data string  -   -  		Grid of supercells of local escape solutions (auxiliary input file name)
Param:  inet int  -  1 		Network interface index 
Param:  ith int  -  0 		Make every ith process a daemon 
Param:  nthreads int  -   -  		Number of threads (connections) per daemon 
LDesc:  (defaults to: 2*ncpu)
Param:  port int  -  18003 		TCP port for listening 
Param:  timeout int  -  10 		Inactivity time before shutdown (mins) 

