[sfvti3dpseudosv]
Cat:    RSF/user/chengjb
Desc:   3-D three-components wavefield modeling using pseudo-pure mode SV-wave equation in 3D VTI media
DocCmd: sfvti3dpseudosv | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   PseudoPureSV rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   PseudoPureSVz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  bd int  -  20 		
Param:  dt float  -  0.001 		
Param:  ns int  -  301 		

