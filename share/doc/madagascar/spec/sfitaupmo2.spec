[sfitaupmo2]
Cat:    RSF/system/seismic
Desc:   Inverse normal moveout in tau-p-x domain
DocCmd: sfitaupmo2 | cat
Port:   stdin  rsf r req 	RSF standard input (containing cmp data)
Port:   stdout rsf w req 	RSF standard output (containing nmod data)
Port:   velocity rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dx float  -   -  		offset sampling 
Param:  nw int  -  4 		interpolator size (2,3,4,6,8) 
Param:  nx int  -   -  		number of offsets 
Param:  x0 float  -  0.0 		first offset 

