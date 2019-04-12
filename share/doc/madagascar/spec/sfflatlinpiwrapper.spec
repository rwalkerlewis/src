[sfflatlinpiwrapper]
Cat:    RSF/user/dmerzlikin
Desc:   pi operator building wrapping test function flat gaussian weighting smoothing after pi
DocCmd: sfflatlinpiwrapper | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  adj enum-bool  -  n 		if perform derivative filtering 
Param:  diff# enum-bool  -   -  		differentiation on #-th axis 
LDesc:  (defaults to: (n,n,...))
Param:  domod enum-bool  -  y 		if y, apply half-derivative filter 
Param:  eps float  -  0.001 		
Param:  epst2 float  -  0.001 		
Param:  hd enum-bool  -  y 		
Param:  pad int  -   -  		output time samples 
LDesc:  (defaults to: nt)
Param:  passthr float  -  0.001 		
Param:  pifk string  -   -  		auxiliary output file name
Param:  rect# int  -   -  		smoothing radius on #-th axis 
LDesc:  (defaults to: (1,1,...))
Param:  repeat int  -  1 		repeat filtering several times 
Param:  sm enum-bool  -  y 		if y, do adjoint integration 
Param:  sw int  -  0 		if > 0, select a branch of the antialiasing operation 
Param:  v0 float  -   -  		constant velocity (if no velocity=) 
Param:  v_1 float  -   -  		
Param:  v_2 float  -   -  		
Param:  v_3 float  -   -  		
Param:  v_4 float  -   -  		
Param:  velocity string  -   -  		velocity file (auxiliary input file name)

