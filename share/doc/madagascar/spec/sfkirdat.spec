[sfkirdat]
Cat:    RSF/user/llisiw
Desc:   2-D Pre-stack Kirchhoff redatuming
DocCmd: sfkirdat | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   rgreen rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sgreen rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  aperture int  -  50 		aperture (number of traces) 
Param:  datum float  -   -  		datum depth 
Param:  interm string  -   -  		auxiliary output file name
Param:  length float  -  0.025 		filter length (in seconds) 
Param:  taper int  -  10 		taper (number of traces) 
Param:  verb enum-bool  -  n 		verbosity flag 

