[sfspiralsort]
Cat:    RSF/user/yunzhi
Desc:   Sort microseismic surface array recording traces with a given epicenter along a spiral shape R = r0 + d(a-a0)
DocCmd: sfspiralsort | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dist rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   theta rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   x rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   y rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  angle0 float  -  0.0 		Starting angle of spiral. 
Param:  dr float  -   -  		Spiral interval parameter. 
Param:  epi_x float  -   -  		referenced epicenter coordinate x. 
Param:  epi_y float  -   -  		referenced epicenter coordinate y. 
Param:  radius0 float  -  1.0 		Starting radius of spiral. 

