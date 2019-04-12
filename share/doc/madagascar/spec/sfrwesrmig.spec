[sfrwesrmig]
Cat:    RSF/system/seismic
Desc:   Riemannian Wavefield Extrapolation: shot-record migration
DocCmd: sfrwesrmig | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw_s data)
Port:   stdout rsf w req 	RSF standard output (containing Fw_r data)
Port:   abm rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   abr rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   img rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		y=modeling; n=migration 
Param:  method int  -  0 		extrapolation method 
Param:  verb enum-bool  -  n 		

