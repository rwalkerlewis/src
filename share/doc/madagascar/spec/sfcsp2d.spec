[sfcsp2d]
Cat:    RSF/user/seisinv
Desc:   2-D common scattering-point gathers mapping and its adjoint
DocCmd: sfcsp2d | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  y 		yes: CSP mapping, no: CMP building 
Param:  apt float  -   -  		aperture 
LDesc:  (defaults to: SF_MAX(fabsf(he0),fabsf(he0+(nhe-1)*dhe)))
Param:  dh float  -   -  		
LDesc:  (defaults to: dhe)
Param:  dhe float  -   -  		
LDesc:  (defaults to: dh)
Param:  dxm float  -   -  		
LDesc:  (defaults to: dxs)
Param:  dxs float  -   -  		
LDesc:  (defaults to: dxm)
Param:  h0 float  -   -  		
LDesc:  (defaults to: he0)
Param:  half enum-bool  -  n 		half offset flag 
Param:  he0 float  -   -  		
LDesc:  (defaults to: h0)
Param:  linear enum-bool  -  n 		yes: linear interpolation, no: nearest-neighbor interpolation 
Param:  nh int  -   -  		
LDesc:  (defaults to: nhe)
Param:  nhe int  -   -  		
LDesc:  (defaults to: nh)
Param:  nxm int  -   -  		
LDesc:  (defaults to: nxs)
Param:  nxs int  -   -  		
LDesc:  (defaults to: nxm)
Param:  ompchunk int  -  1 		OpenMP data chunk size 
Param:  ompnth int  -  0 		OpenMP available threads 
Param:  v float  -  2000. 		velocity 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  weight enum-bool  -  n 		weighting flag 
Param:  xm0 float  -   -  		
LDesc:  (defaults to: xs0)
Param:  xs0 float  -   -  		
LDesc:  (defaults to: xm0)

