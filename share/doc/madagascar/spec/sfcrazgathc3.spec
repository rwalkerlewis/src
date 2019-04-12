[sfcrazgathc3]
Cat:    RSF/user/cram
Desc:   Collapse/stack (partially) azimuthal axis of 3-D angle-domain migration angle gathers
DocCmd: sfcrazgathc3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing gath data)
Port:   stdout rsf w req 	RSF standard output (containing rgath data)
Param:  norm enum-bool  -  n 		y - normalize after stacking 
Param:  nth int  -  10 		leave every nth azimuth 
Param:  verb enum-bool  -  y 		verbosity flag 
Param:  wd int  -  5 		half-width of stacking base (total base is 2*wd + 1) 

