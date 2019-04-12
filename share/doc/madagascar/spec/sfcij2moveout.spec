[sfcij2moveout]
Cat:    RSF/user/zone
Desc:   Converting interval Cij to interval/effective moveout coefficients in 3D layered orthorhombic with possible phimuthal rotation (Sripanich and Fomel, 2016)
DocCmd: sfcij2moveout | cat
Port:   stdin  rsf r req 	RSF standard input (containing C11 data)
Port:   stdout rsf w req 	RSF standard output (containing a11o data)
Port:   a1111o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a1112o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a1122o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a1222o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a12o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a2222o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   a22o rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   c12 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c13 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c22 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c23 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c33 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c44 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c55 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   c66 rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   phi rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eff enum-bool  -  n 		Output effective parameters instead of interval
Param:  scalecij float  -  1 		Scaling of input Cij in case of GPa or km^2/s^2
Param:  scalequartic enum-bool  -  n 		Scaling the output quartic coefficients y--multiplied by 2 t0^2 (t0 = two-way) to look at the property of the layer -> input for GMA

