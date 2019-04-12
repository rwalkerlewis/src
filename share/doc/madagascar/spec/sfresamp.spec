[sfresamp]
Cat:    RSF/user/chengjb
Desc:   2D data resampling
DocCmd: sfresamp | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  d1 float  -   -  		sample interval on 1st axis 
LDesc:  (defaults to: d[0])
Param:  d2 float  -   -  		sample interval on 2nd axis 
LDesc:  (defaults to: d[1])
Param:  o1 float  -   -  		first sample sample on 1st axis 
LDesc:  (defaults to: o[0])
Param:  o2 float  -   -  		first sample on 2nd axis 
LDesc:  (defaults to: o[1])

