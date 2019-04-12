[sfgeoconvert]
Cat:    RSF/user/yliu
Desc:   2-D regular geometry conversion
DocCmd: sfgeoconvert | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  dr float  -  0.025 		receiver interval 
Param:  ds float  -  0.05 		shot interval 
Param:  nr int  -   -  		receiver number per shot 
Param:  ns int  -   -  		shot number 
Param:  or float  -  0. 		receiver origin 
Param:  os float  -  0. 		shot origin 

