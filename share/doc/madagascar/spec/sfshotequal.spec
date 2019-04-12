[sfshotequal]
Cat:    RSF/user/salah
Desc:   sfshotequal projects amplitudes of each shot to Z-score distribution
DocCmd: sfshotequal | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  amp float  -   -  		Exclude amplitudes greater than amp && less than -amp for statistics computations
Param:  mask string  -   -  		auxiliary input file name
Param:  scaler string  -   -  		auxiliary output file name
Param:  verb enum-bool  -  n 		verbosity flag 

