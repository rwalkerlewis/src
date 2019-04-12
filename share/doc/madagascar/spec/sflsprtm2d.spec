[sflsprtm2d]
Cat:    RSF/user/pyang
Desc:   least-squares prestack RTM in 2-D
DocCmd: sflsprtm2d | cat
Port:   stdin  rsf r req 	RSF standard input (containing shots data)
Port:   stdout rsf w req 	RSF standard output (containing imglsm data)
Port:   imgrtm rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  fromBoundary enum-bool  -  y 		if fromBoundary=true, reconstruct source wavefield from stored boundary 
Param:  nb int  -  20 		number (thickness) of ABC on each side 
Param:  niter int  -  10 		totol number of least-squares iteration
Param:  testadj int  -  0 		if testadj = 1 then program only testadj without calculating 
Param:  verb enum-bool  -  y 		verbosity 

