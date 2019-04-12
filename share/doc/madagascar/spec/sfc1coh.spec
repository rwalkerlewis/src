[sfc1coh]
Cat:    RSF/user/yliu
Desc:   C1 coherency algorithm
DocCmd: sfc1coh | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  lag1 int  -  3 		Inline time lag (default=3) 
Param:  lag2 int  -  3 		Crossline time lag (default=3) 
Param:  ntw int  -  3 		Temporal length of the correlation window (default=3) 
Param:  verb enum-bool  -  y 		verbosity flag 

