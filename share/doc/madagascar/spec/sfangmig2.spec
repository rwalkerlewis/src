[sfangmig2]
Cat:    RSF/user/luke
Desc:   Angle-gather constant-velocity time migration
DocCmd: sfangmig2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		if y modeling, if n, migration 
Param:  amax float  -   -  		maximum dip angle 
Param:  dh float  -   -  		offset increment
Param:  dt float  -   -  		time increment 
LDesc:  (defaults to: dtau)
Param:  dtau float  -   -  		output vertical sampling 
LDesc:  (defaults to: dt)
Param:  dx float  -   -  		data domain spatial increment 
LDesc:  (defaults to: dxi)
Param:  dxi float  -   -  		output sampling 
LDesc:  (defaults to: dx)
Param:  eps float  -  0.00001 		epsilon for division in semblance calc
Param:  gmax float  -   -  		maximum reflection angle
LDesc:  (defaults to: amax)
Param:  h0 float  -   -  		initial offset 
Param:  l2 enum-bool  -  y 		if y use l2 norm for semb, if n, use l1 norm 
Param:  mask string  -   -  		input file contining image mask locations, 0 = skip (auxiliary input file name)
Param:  na int  -   -  		number of dip angles 
Param:  ng int  -   -  		number of reflection angles 
LDesc:  (defaults to: na)
Param:  nh int  -   -  		number of offsets 
Param:  nt int  -   -  		number time samples 
LDesc:  (defaults to: ntau)
Param:  ntau int  -   -  		output vertical samples 
LDesc:  (defaults to: nt)
Param:  nx int  -   -  		data domain spatial samples 
LDesc:  (defaults to: nxi)
Param:  nxi int  -   -  		output samples 
LDesc:  (defaults to: nx)
Param:  semb string  -   -  		output file containing Semblance (auxiliary output file name)
Param:  t0 float  -   -  		time orgin 
LDesc:  (defaults to: tau0)
Param:  tau0 float  -   -  		output vertical orgin 
LDesc:  (defaults to: t0)
Param:  vin string  -   -  		input velocity file (auxiliary input file name)
Param:  weighting enum-bool  -  y 		kirchhoff weighting? 
Param:  x0 float  -   -  		data domain spatial orgin 
LDesc:  (defaults to: xi0)
Param:  xi0 float  -   -  		output orgin 
LDesc:  (defaults to: x0)

