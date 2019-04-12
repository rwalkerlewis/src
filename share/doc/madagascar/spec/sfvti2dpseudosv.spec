[sfvti2dpseudosv]
Cat:    RSF/user/chengjb
Desc:   2-D two-components wavefield modeling using pseudo-pure mode qSV-wave equation in VTI media
DocCmd: sfvti2dpseudosv | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   PseudoPureSV rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSVz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSepSV rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   acx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   acxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   acz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   aczz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asvx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asvxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asvz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asvzz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asxx rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   asz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   aszz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  ihomo int  -  0 		if ihomo=1, homogeneous medium 
Param:  isep int  -  0 		if isep=1, separate wave-modes 
Param:  itaper int  -  0 		if itaper=1, taper the wavenumber domain p=operators
Param:  ns int  -  301 		
Param:  nstep int  -  2 		
Param:  tapertype string  -   -  		taper type

