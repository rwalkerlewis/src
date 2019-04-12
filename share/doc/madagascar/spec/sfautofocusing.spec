[sfautofocusing]
Cat:    RSF/user/fbroggin
Desc:   Marchenko-Wapenaar-Broggini iterative scheme
DocCmd: sfautofocusing | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fplus data)
Port:   stdout rsf w req 	RSF standard output (containing FGp data)
Port:   G rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Gm rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   H rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   p rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   q rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   window rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  Gtot enum-bool  -  n 		Gtot=true: returns G=Gp+Gm 
Param:  Htot enum-bool  -  n 		Htot=true: returns H=Gp-Gm 
Param:  conj enum-bool  -  n 		complex conjugation (time-reversal) flag 
Param:  eps float  -  1e-4 		threshold for the timewindow 
Param:  niter int  -  1 		number of iterations 
Param:  nshots int  -  1 		number of shots 
Param:  pandq enum-bool  -  n 		pandq=true: returns p and q 
Param:  refl string  -   -  		000.rsf are 7 characters (auxiliary input file name)
Param:  scale float  -  1.0 		scale factor 
Param:  shift int  -  5 		shift in samples for the timewindow 
Param:  twin enum-bool  -  n 		returns the timewindow as one of the outputs 
Param:  verb enum-bool  -  n 		verbosity flag 

