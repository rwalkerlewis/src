[sfxcor3d]
Cat:    RSF/user/jsun
Desc:   OpenMP time- or freq-domain reversed cross-correlation on the fourth axes, read entire cube into memory
DocCmd: sfxcor3d | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   uu rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  rev enum-bool  -  n 		reverse the fourth axis of uu 
Param:  verb enum-bool  -  n 		verbosity flag 

