[sfpermwave2d]
Cat:    RSF/user/hwang
Desc:   Wavefield Extrapolation for 2D PERM
DocCmd: sfpermwave2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing image data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wavelet rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dz float  -   -  		
Param:  imageit int  -  0 		time for extracting image 
Param:  mig enum-bool  -  n 		if n, modeling; if y, migration 
Param:  nz int  -   -  		depth axis 

