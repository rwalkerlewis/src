[sfwavemixop]
Cat:    RSF/user/jsun
Desc:   Complex 2-D wave propagation (with kiss-fft)
DocCmd: sfwavemixop | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fw data)
Port:   stdout rsf w req 	RSF standard output (containing Fo data)
Port:   alpha rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   beta rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   left rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   ref rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   right rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   snaps rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  correct enum-bool  -  n 		jingwei's correction
Param:  mode string  -   -  		default mode is pspi 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  snap int  -  0 		interval for snapshots 
Param:  type int  -  0 		type of propagation; 0 means no correction applied, and mode takes effect, 9 enables jjsf
Param:  verb enum-bool  -  n 		verbosity 

