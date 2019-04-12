[sfwexwfl]
Cat:    RSF/user/cwp
Desc:   3-D wavefield extrapolation with extended SSF
DocCmd: sfwexwfl | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fd data)
Port:   stdout rsf w req 	RSF standard output (containing Fw data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  causal enum-bool  -  n 		causality flag 
Param:  datum int  -  0 		datuming flag 
Param:  dtmax float  -  0.004 		max time error 
Param:  eps float  -  0.01 		stability parameter 
Param:  inv int  -  1 		down/upward flag 
Param:  nrmax int  -  1 		maximum references 
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y
Param:  tmx int  -  0 		taper on x
Param:  tmy int  -  0 		taper on y 
Param:  verb enum-bool  -  n 		verbosity flag 

