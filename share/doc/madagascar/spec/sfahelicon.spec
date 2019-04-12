[sfahelicon]
Cat:    RSF/user/gee
Desc:   Apply multidimensional nonstationary filter on a helix
DocCmd: sfahelicon | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  dim int  -   -  		number of dimensions 
LDesc:  (defaults to: ndim)
Param:  lag string  -   -  		file with filter lags
Param:  n int-list  -   -  		 [dim]

