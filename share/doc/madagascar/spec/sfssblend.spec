[sfssblend]
Cat:    RSF/user/chen
Desc:   blend reciever gathers (T-S-R) to generate simultaneous data
DocCmd: sfssblend | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   delay rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  jt int  -  1 		subsampling nps 

