[sfvti3dpseudosh]
Cat:    RSF/user/chengjb
Desc:   3-D three-components wavefield modeling using pure mode SH-wave equation in 3D VTI media
DocCmd: sfvti3dpseudosh | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   SH rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   SHy rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   gam rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  bd int  -  20 		
Param:  dt float  -  0.001 		
Param:  ns int  -  301 		

