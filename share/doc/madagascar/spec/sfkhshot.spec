[sfkhshot]
Cat:    RSF/user/effsilva
Desc:   Kirchhoff shot migration
DocCmd: sfkhshot | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Port:   ttfile rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  df float  -  5. 		anti-aliasing sampling 
Param:  dtheta float  -   -  		taper zone 
LDesc:  (defaults to: theta/3)
Param:  dx float  -   -  		
LDesc:  (defaults to: d2t)
Param:  dz float  -   -  		checking dimensions 
LDesc:  (defaults to: d1t)
Param:  fmax float  -   -  		
LDesc:  (defaults to: .5/d1)
Param:  ntaper int  -  11 		
Param:  nx int  -   -  		
LDesc:  (defaults to: n2t)
Param:  nz int  -   -  		
LDesc:  (defaults to: n1t)
Param:  ox float  -   -  		
LDesc:  (defaults to: o2t)
Param:  oz float  -   -  		
LDesc:  (defaults to: o1t)
Param:  theta float  -  30. 		maximum dip 
Param:  tmin float  -   -  		
LDesc:  (defaults to: 3*d1)
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  xs float  -   -  		image parameters 

