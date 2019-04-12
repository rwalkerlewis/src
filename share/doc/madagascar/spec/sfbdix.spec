[sfbdix]
Cat:    RSF/user/fomels
Desc:   Convert RMS to interval velocity using LS and shaping regularization
DocCmd: sfbdix | cat
Port:   stdin  rsf r req 	RSF standard input (containing vrms data)
Port:   stdout rsf w req 	RSF standard output (containing vint data)
Port:   block rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   weight rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  niter int  -  100 		maximum number of iterations 
Param:  perc float  -  50.0 		percentage for sharpening 
Param:  vrmsout string  -   -  		optionally, output predicted vrms (auxiliary output file name)

