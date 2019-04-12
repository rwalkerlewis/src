[sftti2de]
Cat:    RSF/user/chengjb
Desc:   2-D two-components wavefield modeling using original elastic displacement wave equation in TTI media
DocCmd: sftti2de | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fvp0 data)
Port:   stdout rsf w req 	RSF standard output (containing Fo1 data)
Port:   Elasticz rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   del rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   epsi rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   the rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   vs0 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  dt float  -  0.001 		
Param:  ns int  -  301 		

