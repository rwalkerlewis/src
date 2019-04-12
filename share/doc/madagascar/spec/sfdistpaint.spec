[sfdistpaint]
Cat:    RSF/user/pwd
Desc:   Geologic distance painting by plane-wave construction
DocCmd: sfdistpaint | cat
Port:   stdin  rsf r req 	RSF standard input (containing dip data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  eps float  -  0.01 		regularization 
Param:  faultscale float  -  100. 		Fault attribute scaling factor (0.0 ~ factor) 
Param:  flt string  -   -  		auxiliary input file name
Param:  i0 int  -  0 		reference trace 
Param:  order int  -  1 		accuracy order 
Param:  seed string  -   -  		auxiliary input file name
Param:  verb enum-bool  -  n 		

