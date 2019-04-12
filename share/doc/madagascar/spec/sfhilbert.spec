[sfhilbert]
Cat:    RSF/user/chenyk
Desc:   Compute hilbert transform using different methods
DocCmd: sfhilbert | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  order int  -  100 		Hilbert transformer order if type=m 
Param:  phase float  -  90. 		phase shift (in degrees) 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) if type=m 
Param:  type string  -   -  		Choosing hilbert transform method, type=t means time domain, 
LDesc:         type=f means freqency domain, type=m means using more robust algorithm
LDesc:         the default is type=m 

