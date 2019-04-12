[sfmpifwigradlr]
Cat:    RSF/user/zhiguang
Desc:   Conventional FWI misfit and gradient calculation using one-step low-rank wave extrapolation
DocCmd: sfmpifwigradlr | cat
Port:   Fdat rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fgrad rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fleft rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fleftb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fmisfit rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fq rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fres rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fright rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Frightb rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fsrc rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fvel rsf r  -  		auxiliary input file name (containing unspecified data)
Port:   Fwav rsf w  -  		auxiliary output file name (containing unspecified data)
Port:   Fwav2 rsf w  -  		auxiliary output file name (containing unspecified data)
Param:  adjtest enum-bool  -  n 		test of adjointness 
Param:  dr float  -   -  		receiver interval 
LDesc:  (defaults to: dx)
Param:  ds float  -   -  		shot interval 
Param:  function int  -  3 		if 1, forward modeling; if 2, only calculate misfit; if 3, calculate gradient 
Param:  nb int  -   -  		
Param:  nr int  -   -  		number of receiver 
LDesc:  (defaults to: rnx)
Param:  ns int  -   -  		shot number 
Param:  pad1 int  -  1 		padding factor on the first axis 
Param:  r0 float  -   -  		receiver origin 
LDesc:  (defaults to: x0)
Param:  rectx int  -  3 		
Param:  rectz int  -  3 		
Param:  rz int  -  5 		receiver depth 
Param:  s0 float  -   -  		shot origin 
Param:  scalet int  -  1 		time interval 
Param:  scomp enum-bool  -  n 		source wavefield compensation flag 
Param:  sz int  -  5 		source depth 
Param:  verb enum-bool  -  n 		verbosity flag 
Param:  w0 float  -   -  		reference frequency 

