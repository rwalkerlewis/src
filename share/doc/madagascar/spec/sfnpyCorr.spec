[sfnpyCorr]
Cat:    RSF/user/ediazp
Desc:   
DocCmd: sfnpyCorr | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fa data)
Port:   stdout rsf w req 	RSF standard output (containing Fc data)
Port:   flt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nc int  -  100 		number of correlation lags
Param:  norm enum-bool  -  n 		normalize output

