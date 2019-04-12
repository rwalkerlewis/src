[sffftone]
Cat:    RSF/user/fomels
Desc:   Test 1-D Fourier transform
DocCmd: sffftone | cat
Port:   stdin  rsf r req 	RSF standard input (containing freq data)
Port:   stdout rsf w req 	RSF standard output (containing space data)
Param:  inv enum-bool  -  n 		inverse flag 
Param:  n1 int  -   -  		dimension (for inv=y) 

