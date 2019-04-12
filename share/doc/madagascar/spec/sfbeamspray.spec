[sfbeamspray]
Cat:    RSF/system/seismic
Desc:   2-D beam spraying
DocCmd: sfbeamspray | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   cur rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dip rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1.0 		experimental 
Param:  rect int  -  3 		smoothing radius 

