[sfwexzoimg]
Cat:    RSF/user/cwp
Desc:   3-D zero-offset modeling/migration with extended SSF
DocCmd: sfwexzoimg | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fm data)
Port:   slo rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wfl rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adj int  -   -  		y=ADJ migration; n=FWD modeling 
Param:  dtmax float  -  0.004 		max time error 
Param:  dw float  -   -  		
Param:  eps float  -  0.01 		stability parameter 
Param:  nrmax int  -  1 		maximum references 
Param:  nw int  -   -  		
Param:  ow float  -  0. 		
Param:  pmx int  -  0 		padding on x 
Param:  pmy int  -  0 		padding on y
Param:  save int  -  0 		save wfld flag 
Param:  tmx int  -  0 		taper on x
Param:  tmy int  -  0 		taper on y 
Param:  verb enum-bool  -  n 		verbosity flag 

