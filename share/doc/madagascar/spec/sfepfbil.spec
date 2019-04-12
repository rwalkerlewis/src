[sfepfbil]
Cat:    RSF/user/chen
Desc:   Bilateral filter
DocCmd: sfepfbil | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  sigmad float  -  1.0 		sigma for domain filter 
Param:  sigmar float  -  1.0 		sigma for range filter 
Param:  twod enum-bool  -  n 		y, 2D smoothing 

