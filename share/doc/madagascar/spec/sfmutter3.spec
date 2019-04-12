[sfmutter3]
Cat:    RSF/user/jsun
Desc:   3D muting of scalor or vector data
DocCmd: sfmutter3 | cat
Port:   stdin  rsf r req 	RSF standard input (containing Finp data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   rec rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   sou rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  1000. 		decay parameter 
Param:  t0 float  -  0 		source delay time 
Param:  velw float  -  1.5 		water velocity 
Param:  verb enum-bool  -  n 		verbosity flag 

