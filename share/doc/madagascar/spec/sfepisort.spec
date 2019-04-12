[sfepisort]
Cat:    RSF/user/yunzhi
Desc:   Sort microseismic surface array recording traces by their distances or azimuths to a given epicenter
DocCmd: sfepisort | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   dist rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   theta rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   x rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   y rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  epi_x float  -   -  		referenced epicenter coordinate x. 
Param:  epi_y float  -   -  		referenced epicenter coordinate y. 
Param:  sort string  -   -  		sort distance[d] (default) or angle[a] 

