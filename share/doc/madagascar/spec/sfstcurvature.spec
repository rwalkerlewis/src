[sfstcurvature]
Cat:    RSF/user/parvaneh
Desc:   Curvature in stratigraphic coordinates
DocCmd: sfstcurvature | cat
Port:   stdin  rsf r req 	RSF standard input (containing xhor data)
Port:   stdout rsf w req 	RSF standard output (containing cur data)
Port:   yh rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   zh rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  scale float  -  1.0 		scaling (from time to depth) 
Param:  what string  -   -  		what to compute 

