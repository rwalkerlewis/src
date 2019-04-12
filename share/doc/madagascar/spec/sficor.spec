[sficor]
Cat:    RSF/user/psava
Desc:   Interferometric cross-correlation of time series (zero-lag output)
DocCmd: sficor | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fs data)
Port:   stdout rsf w req 	RSF standard output (containing Fi data)
Port:   ur rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nht int  -  1 		
Param:  nhx int  -  0 		
Param:  nhz int  -  0 		
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  verb enum-bool  -  n 		verbosity flag 

