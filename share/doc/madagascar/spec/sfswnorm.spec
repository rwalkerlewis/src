[sfswnorm]
Cat:    RSF/user/jsun
Desc:   Sliding window normalization
DocCmd: sfswnorm | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  log enum-bool  -  n 		log scaling 
Param:  perc float  -  5 		threshold percentage of the maximum value 
Param:  size int  -  0 		sliding window radius 
Param:  sw enum-bool  -  n 		sliding window 
Param:  var_thres float  -  0. 		variance threshold (normalized) 

