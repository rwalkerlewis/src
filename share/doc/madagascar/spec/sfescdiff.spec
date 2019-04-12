[sfescdiff]
Cat:    RSF/user/cram
Desc:   Compute distance and traveltime difference between two escape tables
DocCmd: sfescdiff | cat
Port:   stdin  rsf r req 	RSF standard input (containing esct0 data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  esct string  -   -  		Second set of escape tables (auxiliary input file name)
Param:  mask float  -   -  		Mask for values above maxd= and maxt= thresholds 
LDesc:  (defaults to: SF_HUGE)
Param:  maxd float  -   -  		Maximum allowed distance 
LDesc:  (defaults to: SF_HUGE)
Param:  maxt float  -   -  		Maximum allowed time 
LDesc:  (defaults to: SF_HUGE)

