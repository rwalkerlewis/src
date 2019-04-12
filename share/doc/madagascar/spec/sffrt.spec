[sffrt]
Cat:    RSF/user/chen
Desc:   Frequency domain Radon transform
DocCmd: sffrt | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  curv int  -  0 		0: linear; 1:parabolic 
Param:  dp float  -  0 		stepout interval 
Param:  eta float  -  0.05 		eta: for fhrt, fcrt 
Param:  inv enum-bool  -  n 		if y, perform inverse operation 
Param:  mtd int  -  0 		0: fart; 1:firt; 2:fhrt; 3:fcrt 
Param:  mu float  -  0.05 		mu: for firt, fhrt, fcrt 
Param:  niter int  -  5 		sparse iterations: for fhrt, fcrt 
Param:  np int  -  0 		stepout number 
Param:  op float  -  0 		first stepout (moveout at 'ref') 
Param:  x0 float  -   -  		reference offset 
LDesc:  (defaults to: maxoff)

