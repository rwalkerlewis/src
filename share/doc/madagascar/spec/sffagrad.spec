[sffagrad]
Cat:    RSF/user/yliu
Desc:   Calculating frequency attenuation gradient
DocCmd: sffagrad | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  freq float  -   -  		Frequency corresponding to energy ratio, valid when type=ratio 
Param:  grad enum-bool  -  y 		If y, output attenuation gradient; if n, output absorption factor 
Param:  hperc float  -  85. 		High percentage of total energy 
Param:  lperc float  -  65. 		Low percentage of total energy 
Param:  type string  -   -  		[low,full,ratio,attenuation] attribute type, the default is attenuation  

