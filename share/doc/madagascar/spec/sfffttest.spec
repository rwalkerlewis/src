[sfffttest]
Cat:    RSF/user/fomels
Desc:   Test 3-D Fourier transform
DocCmd: sfffttest | cat
Port:   stdin  rsf r req 	RSF standard input (containing freq data)
Port:   stdout rsf w req 	RSF standard output (containing space data)
Param:  cmplx enum-bool  -  n 		use complex FFT 
Param:  inv enum-bool  -  n 		inverse flag 
Param:  n1 int  -   -  		
Param:  n2 int  -   -  		
Param:  n3 int  -   -  		
Param:  pad1 int  -  1 		padding factor on the first axis 

