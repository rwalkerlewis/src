[sfpsefd]
Cat:    RSF/user/chen
Desc:   EFD phase shift wave extrapolation
DocCmd: sfpsefd | cat
Port:   stdin  rsf r req 	RSF standard input (containing data data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   vel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   wave rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  jz int  -  40 		depth step for wave data 
Param:  nz int  -   -  		depth number 
LDesc:  (defaults to: nz0-rz)
Param:  rz int  -  0 		receiver depth 

