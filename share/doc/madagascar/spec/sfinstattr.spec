[sfinstattr]
Cat:    RSF/user/yliu
Desc:   Estimate of instantaneous attributes
DocCmd: sfinstattr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  der2 enum-bool  -  n 		if y, compute 2nd-order derivative to use with hires=y 
Param:  hertz enum-bool  -  y 		if y, convert output to Hertz 
Param:  hires enum-bool  -  n 		if y, compute high resolution instantaneous attributes 
Param:  order int  -  10 		Hilbert transformer order 
Param:  ref float  -  1. 		Hilbert transformer reference (0.5 < ref <= 1) 
Param:  type string  -   -  		[amplitude,phase,frequency] attribute type, the default is amplitude 
Param:  verb enum-bool  -  n 		verbosity flag 

