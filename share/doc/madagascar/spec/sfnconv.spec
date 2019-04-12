[sfnconv]
Cat:    RSF/user/fomels
Desc:   Non-stationary convolution
DocCmd: sfnconv | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   filt rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  adj enum-bool  -  n 		adjoint flag 
Param:  lag int  -   -  		filter lag 
LDesc:  (defaults to: (ntau+1)/2)

