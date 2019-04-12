[sfcigangle]
Cat:    RSF/user/roman
Desc:   src-receiver to angle gathers
DocCmd: sfcigangle | cat
Port:   stdin  rsf r req 	RSF standard input (containing dist data)
Port:   stdout rsf w req 	RSF standard output (containing imag data)
Port:   data rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   dept rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   time rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  nalpha int  -  90 		
Param:  tolz float  -   -  		surface depth 
LDesc:  (defaults to: 1.f)

