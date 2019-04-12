[sfccrsym]
Cat:    RSF/user/jsun
Desc:   determine symmetry using correlation
DocCmd: sfccrsym | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  pad float  -   -  		pad for stable devision 
LDesc:  (defaults to: SF_EPS)
Param:  size int  -  0 		sliding window radius 

