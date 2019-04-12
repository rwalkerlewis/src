[sfhcascade]
Cat:    RSF/user/gee
Desc:   Multidimensional convolution cascade
DocCmd: sfhcascade | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  lag string  -   -  		file with filter lags
Param:  n int-list  -   -  		 [dim]
Param:  rect int  -  0 		smoothing radius 

