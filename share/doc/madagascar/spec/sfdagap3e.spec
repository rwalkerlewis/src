[sfdagap3e]
Cat:    RSF/user/luke
Desc:   Reflection event apex protector/removal for dip-angle gathers
DocCmd: sfdagap3e | cat
Port:   stdin  rsf r req 	RSF standard input (containing dagFile data)
Port:   stdout rsf w req 	RSF standard output (containing taperFile data)
Param:  ddep enum-bool  -  y 		if y, taper depends on depth; if n, no 
Param:  dips string  -   -  		dips esitimated in the image domain (in degree) (auxiliary input file name)
Param:  dz float  -   -  		half of a migrated wave length 
LDesc:  (defaults to: 20.f)
Param:  greyarea1 float  -   -  		
LDesc:  (defaults to: 10.f)
Param:  greyarea2 float  -   -  		width of event tail taper (in degree) 
LDesc:  (defaults to: 10.f)
Param:  pwidth1 float  -   -  		
LDesc:  (defaults to: 10.f)
Param:  pwidth2 float  -   -  		protected width (in degree) 
LDesc:  (defaults to: 10.f)

